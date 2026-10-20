# Read-only RPC safety contract (proposed)

ChainWatch is intended to inspect public blockchain data without signing or broadcasting transactions. This contract describes how a future RPC client should behave.

## Configuration

- Require an explicit chain ID and RPC endpoint.
- Use bounded connect/read timeouts and a capped retry policy.
- Never ask for or store seed phrases, private keys, or wallet passwords.
- Do not expose transaction-signing or transaction-broadcast methods in the initial client interface.

## Response validation

- Parse the response as JSON and validate the JSON-RPC version, request ID, result/error exclusivity, and expected result type.
- Treat every remote field as untrusted. Reject malformed hex quantities, invalid addresses, and unexpected response shapes with typed errors.
- Keep chain ID explicit in output to prevent confusing testnet and mainnet observations.
- Do not silently turn RPC errors into zero balances or empty transaction lists.
- Avoid logging full URLs when they may contain embedded credentials; prefer logging the endpoint host and a redacted identifier.

## Retry behavior

Retry only transient transport errors and selected rate-limit/server errors. Do not retry invalid requests or deterministic parse errors. Use bounded exponential backoff and respect a valid server-provided retry delay within configured limits.

## Tests

Use a mocked local transport to cover timeouts, malformed JSON, mismatched request IDs, RPC error objects, invalid quantities, rate limiting, and chain-ID mismatch. Unit tests must not need a real wallet or public RPC endpoint.
