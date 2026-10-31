#!/usr/bin/env python3
"""Check XTREE wallet balance. Requires XTREE_API_KEY."""

from __future__ import annotations

import json
import sys

from xtree import XTreeClient


def main() -> int:
    client = XTreeClient()
    resp = client.account.balance()
    print(json.dumps(resp.data, ensure_ascii=False, indent=2))
    if client.last_meta:
        print(
            f"# meta request_id={client.last_meta.request_id} "
            f"cost_cny={client.last_meta.cost_cny} balance_cny={client.last_meta.balance_cny}",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
