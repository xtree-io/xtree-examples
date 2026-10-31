# 03 — WeChat Channels search + feeds

**Slugs:**

- `wechat.channels.search` — find channels by keyword
- `wechat.channels.feeds` — list feeds for a `channel_id`

This script runs **two** billed calls when a channel is found.

```bash
export XTREE_API_KEY=xt_live_...
python main.py "人民日报"
```
