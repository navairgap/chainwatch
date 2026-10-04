# chainwatch

A passive blockchain explorer CLI

> 🚧 **Status: planning** — architecture and README first, code next.

## Why

Web3 exploration, the safe way: chainwatch only *reads* public chain data — no keys, no transactions, no risk. Follow addresses, watch for movements, learn how chains actually work from the raw data.

## Planned features

- Query balances and transaction history for any address
- Watch an address and notify on new activity
- Decode common contract interactions (ERC-20 transfers)
- Local SQLite cache so repeated queries are instant

## Stack

`python` `web3.py` `ethereum` `sqlite`

## Notes

Read-only by design — that's the whole point.

## License

MIT, see [LICENSE](LICENSE).

---
maintained · verified 2026-09-30
---
maintained · verified 2026-10-01
---
maintained · verified 2026-10-02

## Supported chains

- Ethereum mainnet + Sepolia
- Polygon
- Arbitrum One

Adding a chain means one entry in `chains.toml`: an RPC endpoint, confirmation depth, and the events you want indexed. PRs welcome.

## Webhook payload

Registered webhooks receive a POST per matched event:

```json
{
  "chain": "ethereum",
  "block": 20938471,
  "event": "0xddf252ad…",
  "tx": "0x94d2…",
  "confirmations": 12
}
```

Non-2xx responses retry with exponential backoff, max 5 attempts.
