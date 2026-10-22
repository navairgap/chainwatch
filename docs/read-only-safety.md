# read only safety

The CLI should query public chain data only. Never request, persist, or log seed phrases, private keys, or wallet passwords. Redact credentials embedded in RPC endpoint URLs. Use finite timeouts and bounded retries. Distinguish unavailable RPC data from valid zero balances or empty transaction lists. Make chain ID explicit and verify it before interpreting returned data.
