import json
from pathlib import Path


def test_stop_copies_only_the_masked_terminal_report_from_the_assistants_words(tmp_path, monkeypatch):
    monkeypatch.syspath_prepend(str(Path(__file__).parents[1] / "plugin/scripts"))
    import apersona_dev_hook as hook

    requests, paths = [], []
    monkeypatch.setattr(hook, "data_dir", lambda: tmp_path)
    monkeypatch.setattr(hook, "list_left", lambda rows: (1, "整理測試"))
    def receiving(req, _):
        requests.append(json.loads(req.data))
        paths.append(req.full_url)
        return {"verdict": "asking"}
    monkeypatch.setattr(hook, "fetch_json", receiving)
    key = "sk-" + "a" * 40
    transcript = tmp_path / "chat.jsonl"
    transcript.write_text("", encoding="utf8")
    fields = {"session_id": "test", "transcript_path": str(transcript)}
    for said in ("〈下一步〉是舊範例。\n已完成。", f"已完成。\n〈下一步〉整理測試\n\n〈請決定〉交付 {key} 的版本。"):
        assert hook.stand_in("http://localhost", "test", dict(fields, last_assistant_message=said), 1) == ""
    assert "stopReportV1" not in requests[0]
    assert paths == ["http://localhost/api/dev/stand-in", "http://localhost/api/dev/stand-in/report"]
    shown = requests[1]["stopReportV1"]
    assert shown.startswith("〈下一步〉整理測試\n\n〈請決定〉") and requests[1]["said"].endswith(shown)
    assert key not in json.dumps(requests, ensure_ascii=False)
    monkeypatch.setattr(hook, "fetch_json", lambda *_: {"verdict": "continue", "text": "〈人格代答〉繼續"})
    assert hook.stand_in("http://localhost", "test", dict(fields, last_assistant_message="〈下一步〉發布"), 1) == ""
    plain = hook.stand_in("http://localhost", "test", dict(fields, last_assistant_message="已整理完成。"), 1)
    assert json.loads(plain)["decision"] == "block"
