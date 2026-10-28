# read only safety

The CLI should query public chain data only. Never request, persist, or log seed phrases, private keys, or wallet passwords. Redact credentials embedded in RPC endpoint URLs. Use finite timeouts and bounded retries. Distinguish unavailable RPC data from valid zero balances or empty transaction lists. Make chain ID explicit and verify it before interpreting returned data.
## Safe diagnostics

When logging an RPC endpoint, report only its scheme, hostname, and port where available. Strip user-info, query parameters, and fragments before logging; providers sometimes place API tokens in those URL components. Never log authorization headers or raw request bodies. Add tests with credentials in both the URL user-info and query string, and assert that the emitted diagnostic contains neither secret.
## Confirmation and reorganization semantics

Label a transaction as pending, included, or confirmed according to an explicit confirmation threshold. The latest block is not automatically final. If a reorganization changes the canonical block for a previously observed transaction, refresh the result and report the state change rather than presenting a cached confirmation as permanent. Cache keys should include chain ID and relevant block identity, and unavailable RPC data must stay distinct from a valid empty result.
