# chainwatch

A planned read-only CLI for inspecting public blockchain data.

> **Status: design stage.** This repository currently contains documentation only; RPC access, caching, and event watching are not implemented yet.

## Goal

Provide a small tool for looking up public chain data and observing confirmed activity without holding private keys or submitting transactions.

## Initial scope

- Query an address balance and recent confirmed transactions on one chain.
- Use an explicitly configured RPC endpoint.
- Add bounded request timeouts and backoff for rate limits.
- Offer JSON output for scripts.
- Keep any local cache and cursor format documented and easy to remove.

Event decoding, multi-chain support, webhooks, and a health endpoint are later milestones, not current features.

## Safety and correctness

- Never request or store seed phrases, private keys, or wallet passwords.
- Do not sign transactions or broadcast transactions.
- Treat RPC responses as untrusted input and validate expected fields.
- Make chain ID and network explicit to avoid confusing testnet and mainnet data.
- Document that RPC providers can be unavailable or return incorrect data.
- If event watching is added, account for chain reorganizations and duplicate deliveries.

## Planned milestones

- [ ] Define configuration and JSON output schemas.
- [ ] Implement a single-chain read-only balance lookup.
- [ ] Add mocked RPC tests for timeouts, malformed responses, and rate limiting.
- [ ] Add transaction history with pagination limits.
- [ ] Consider event watching after reorg handling is designed.

## License

MIT. See [LICENSE](LICENSE).
