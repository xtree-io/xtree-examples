#!/usr/bin/env python3
"""Fetch WeChat article engagement metrics by URL."""

from __future__ import annotations

import json
import sys

from xtree import XTreeClient


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: python main.py <article_url>", file=sys.stderr)
        return 2
    url = sys.argv[1]
    client = XTreeClient()
    resp = client.wechat.articles.metrics(url=url)
    print(json.dumps(resp.data, ensure_ascii=False, indent=2))
    if client.last_meta:
        print(
            f"# meta cost_cny={client.last_meta.cost_cny} "
            f"balance_cny={client.last_meta.balance_cny}",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
