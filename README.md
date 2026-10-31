# XTREE examples

Runnable API examples for the [XTREE](https://www.xtree.io) Python SDK. Each folder is one call you can copy. This repository is not the SDK and not the MCP server.

XTREE provides **real-time raw data** (not BI conclusions). Every successful call is billed from your wallet (CNY). Incomplete delivery is not billed. Prices: [API Catalog](https://www.xtree.io/catalog). Field reference: [API docs](https://www.xtree.io/docs/apis).

## Setup

```bash
pip install "git+https://github.com/xtree-io/xtree-python.git"
export XTREE_API_KEY=xt_live_...   # from https://www.xtree.io
```

## Scenarios

| Dir | What it does | Billable slugs (approx.) |
|-----|--------------|--------------------------|
| [01_account_balance](01_account_balance/) | Check wallet balance | `account.balance` |
| [02_wechat_search_articles](02_wechat_search_articles/) | WeChat Sogou-style article search | `wechat.search.articles` |
| [03_wechat_channels_feeds](03_wechat_channels_feeds/) | Search Channels + list feeds | `wechat.channels.search`, `wechat.channels.feeds` |
| [04_wechat_articles_metrics](04_wechat_articles_metrics/) | Article read / like / looking metrics | `wechat.articles.metrics` |

## Docs

- https://www.xtree.io/docs
- OpenAPI: https://api.xtree.io/api/openapi.json
- MCP: https://github.com/xtree-io/xtree-mcp
- Skills: https://github.com/xtree-io/xtree-skills

## Mirror notice

Public mirror. Do not commit API keys. Contact: [business@xtree.io](mailto:business@xtree.io).
