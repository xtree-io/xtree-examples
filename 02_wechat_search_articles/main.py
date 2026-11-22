#!/usr/bin/env python3
"""Search WeChat articles by keyword. Usage: python main.py [keyword]."""

from __future__ import annotations

import json
import sys

from xtree import XTreeClient


def main() -> int:
    keyword = sys.argv[1] if len(sys.argv) > 1 else "人民日报"
    client = XTreeClient()
    resp = client.wechat.search.articles(keyword=keyword, page=1)
    data = resp.data or {}
    print(json.dumps(data, ensure_ascii=False, indent=2))
    session = data.get("session") if isinstance(data, dict) else None
    if session:
        print(f"# next page: pass session={session!r}", file=sys.stderr)
    if client.last_meta:
        print(
            f"# meta cost_cny={client.last_meta.cost_cny} "
            f"balance_cny={client.last_meta.balance_cny}",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
