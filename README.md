# Apersona 輔助開發外掛

在 Apersona 核心之外選裝。用核心外掛登入同一台電腦，輔助開發另管理對話收錄與代答。

## Claude Code

```sh
claude plugin marketplace add eric80522-prog/apersona-dev-plugin
claude plugin install apersona-dev@apersona-dev
```

- `/apersona-dev:capture` 開關對話收錄，預設關，須本人同意。收本人新打的字與判讀前後文，秘密先遮。已收的資料留在網站。
- `/apersona-dev:on`、`/apersona-dev:off` 管理輔助開發 hooks。加「只開代答」或「只停代答」只改代答。
- `/apersona-dev:rules` 在本機比較規則並列出提案。你選好才改檔案或把流程話做成指令。
- `/apersona-dev:stats` 在本機計算打字與代答推翻次數，只列數字。

代答只在 Claude Code 停下時檢查。重大的事、網站斷線或判不了時交給本人。

## Codex CLI 與其他工具

- Codex CLI 執行 `python plugin/scripts/apersona_dev_codex.py install` 安裝收錄 hooks，重開後在 `/hooks` 信任。只收本人互動輸入，`codex exec`、子代理和模型輸出都不收。
- Cursor 以 `python plugin/scripts/apersona_feed.py setup --platform cursor` 裝收字與送出 hooks，再由本人用同一支程式的 `consent --platform cursor yes` 同意。Gemini CLI、Grok 和其他工具支援本人在終端機明示送入，同樣先同意。

登入、開場包、手動送資料請用 [Apersona 核心外掛](https://github.com/eric80522-prog/apersona-plugins)。原本合在一起安裝的 Codex hooks 請更新核心安裝後再裝輔助開發 hooks。輔助開發使用自己的本機設定，收錄重新由本人開啟。

MIT，見 [LICENSE](LICENSE)。
