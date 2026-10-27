# read only safety

The CLI should query public chain data only. Never request, persist, or log seed phrases, private keys, or wallet passwords. Redact credentials embedded in RPC endpoint URLs. Use finite timeouts and bounded retries. Distinguish unavailable RPC data from valid zero balances or empty transaction lists. Make chain ID explicit and verify it before interpreting returned data.
## Safe diagnostics

When logging an RPC endpoint, report only its scheme, hostname, and port where available. Strip user-info, query parameters, and fragments before logging; providers sometimes place API tokens in those URL components. Never log authorization headers or raw request bodies. Add tests with credentials in both the URL user-info and query string, and assert that the emitted diagnostic contains neither secret.
