# rpc error handling

Apply finite connection and response timeouts to every RPC request. Validate JSON-RPC response IDs and result/error shape. Retry rate limits and temporary server errors with bounded backoff; do not retry malformed requests indefinitely. Never convert an RPC error into a zero balance or empty transaction list. Validate addresses and chain identifiers, redact endpoint credentials from logs, cache only successful responses, and keep the CLI read-only.

## Response correlation

Validate that each JSON-RPC response uses the same request ID as the request that produced it. Treat a missing, mismatched, or duplicated response ID as a protocol error, not as an empty successful result. For batch requests, map responses by ID rather than array position and report missing or unexpected IDs explicitly. Include mock-transport tests for reordered batch responses and mismatched IDs.
