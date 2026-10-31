# JSON-RPC response fixtures (proposed)

ChainWatch should test RPC behavior using deterministic fixtures rather than depending on a public endpoint. Each fixture should capture the request, response, and expected normalized result or error category.

## Protocol checks

For a JSON-RPC 2.0 response, validate the protocol version and request ID. Require the response to contain either a result or an error object, not both. A notification request has no response ID contract and should not be treated like an ordinary request/response exchange.

Reject mismatched IDs, malformed JSON, invalid top-level types, and error objects with invalid shapes. Do not convert an RPC error into a zero balance, empty transaction list, or successful result.

## Quantity and address fields

For methods that return hexadecimal quantities, require the documented encoding and reject negative, malformed, or out-of-range values. Validate address length and hexadecimal form before passing a value to later processing. Keep chain identity explicit in normalized output.

## Fixture catalogue

Include fixtures for:
- valid result with the expected response ID;
- valid null result where the method permits null;
- RPC error object with a stable code and message;
- mismatched response ID;
- result and error supplied together;
- missing protocol version or ID;
- malformed JSON and unexpected array/string response;
- rate limiting and server errors;
- a valid response from an unexpected chain ID.

## Fixture hygiene

Use synthetic addresses and non-secret endpoints. Never include private keys, seed phrases, wallet credentials, or real account data. Keep request and response fixture pairs small and versioned so changes to the RPC client contract can be reviewed.