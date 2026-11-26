---
description: 依本人同意開啟或關閉對話收錄
---

Use `CLAUDE_PLUGIN_DATA="${CLAUDE_PLUGIN_DATA}" python3 "${CLAUDE_PLUGIN_ROOT}/scripts/apersona_dev_hook.py" --consent yes` to show consent in the owner's own terminal. The owner must read it and type 「我同意」. An AI may add `--by-agent --owner-words "<his exact words>"` only after explaining what is sent and receiving the owner's explicit instruction in this conversation.

Use `--consent no` to stop capture. Show the resulting message. Previously captured material stays saved.
