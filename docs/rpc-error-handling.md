# rpc error handling

Apply finite connection and response timeouts to every RPC request. Validate JSON-RPC response IDs and result/error shape. Retry rate limits and temporary server errors with bounded backoff; do not retry malformed requests indefinitely. Never convert an RPC error into a zero balance or empty transaction list. Validate addresses and chain identifiers, redact endpoint credentials from logs, cache only successful responses, and keep the CLI read-only.
