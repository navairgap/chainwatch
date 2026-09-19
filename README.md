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
