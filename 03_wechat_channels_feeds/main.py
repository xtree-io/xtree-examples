#!/usr/bin/env python3
"""Search WeChat Channels, then list feeds for the first hit."""

from __future__ import annotations

import json
import sys

from xtree import XTreeClient


def _first_channel_id(payload: object) -> str | None:
    if not isinstance(payload, dict):
        return None
    items = payload.get("items") or payload.get("list") or payload.get("channels")
    if isinstance(items, list) and items:
        first = items[0]
        if isinstance(first, dict):
            for key in ("channel_id", "id", "username"):
                val = first.get(key)
                if val:
                    return str(val)
    return None


def main() -> int:
    keyword = sys.argv[1] if len(sys.argv) > 1 else "人民日报"
    client = XTreeClient()

    search = client.wechat.channels.search(keyword=keyword, page=1)
    print("=== channels.search ===")
    print(json.dumps(search.data, ensure_ascii=False, indent=2))

    channel_id = _first_channel_id(search.data)
    if not channel_id:
        print("# no channel_id in search payload; stop", file=sys.stderr)
        return 0

    feeds = client.wechat.channels.feeds(channel_id, page=1)
    print("=== channels.feeds ===")
    print(json.dumps(feeds.data, ensure_ascii=False, indent=2))
    if client.last_meta:
        print(
            f"# last meta cost_cny={client.last_meta.cost_cny} "
            f"balance_cny={client.last_meta.balance_cny}",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
