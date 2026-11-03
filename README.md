# chainwatch

A read-only CLI prototype for inspecting public blockchain data.

> **Current state: JSON-RPC validation helper.** The first standard-library helper validates JSON-RPC 2.0 response IDs and result/error shape. RPC transport, address lookups, pagination, caching, and event watching are not implemented.

## Response validator

The helper accepts a JSON string, UTF-8 bytes, or an already-decoded object. It rejects missing or mismatched IDs, invalid protocol versions, malformed error objects, and responses containing both result and error (or neither). A valid null result remains distinct from an RPC error. Remote RPC errors raise RpcRemoteError with the provider's code, message, and optional data.

Run the focused tests with:

    python -m unittest discover -s tests -v

## Read-only safety

- Never request or store seed phrases, private keys, or wallet passwords.
- Never sign or broadcast transactions.
- Treat RPC responses as untrusted input and validate method-specific fields separately.
- Keep chain ID and network explicit.
- Use finite connection/response timeouts and bounded retries.
- Redact endpoint credentials from logs.

## Remaining work

- [ ] Add a configured read-only JSON-RPC transport.
- [ ] Add batch response correlation by ID.
- [ ] Validate chain IDs, addresses, and hexadecimal quantities.
- [ ] Add mocked transport tests for timeouts, rate limits, and unexpected networks.
- [ ] Add bounded pagination and an optional removable local cache.

## License

MIT. See [LICENSE](LICENSE).
