"""Strict JSON-RPC 2.0 response validation for read-only clients."""
from __future__ import annotations

import json
from typing import Any


class RpcProtocolError(ValueError):
    """The response does not match the JSON-RPC request contract."""


class RpcRemoteError(RuntimeError):
    """The JSON-RPC endpoint returned a valid error object."""

    def __init__(self, code: int, message: str, data: Any = None) -> None:
        self.code = code
        self.message = message
        self.data = data
        super().__init__(f"JSON-RPC error {code}: {message}")


def _valid_id(value: object) -> bool:
    return isinstance(value, str) or (
        isinstance(value, int) and not isinstance(value, bool)
    )


def _reject_json_constant(value: str) -> None:
    raise ValueError(f"non-standard JSON constant: {value}")


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict:
    """Reject ambiguous JSON objects before protocol validation."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON object key")
        result[key] = value
    return result


def validate_response(payload: str | bytes | dict, expected_id: str | int) -> Any:
    """Return the result or raise a typed error; a null result is valid.

    This validates one request/response exchange. Batch response correlation
    and method-specific result validation belong to higher-level callers.
    """
    if not _valid_id(expected_id):
        raise ValueError("expected_id must be a string or integer (not boolean)")

    if isinstance(payload, bytes):
        try:
            payload = payload.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise RpcProtocolError("response is not valid UTF-8") from exc

    if isinstance(payload, str):
        try:
            response = json.loads(
                payload,
                parse_constant=_reject_json_constant,
                object_pairs_hook=_reject_duplicate_keys,
            )
        except (ValueError, RecursionError) as exc:
            raise RpcProtocolError("response is not valid JSON") from exc
    else:
        response = payload

    if not isinstance(response, dict):
        raise RpcProtocolError("response must be a JSON object")
    if response.get("jsonrpc") != "2.0":
        raise RpcProtocolError("response jsonrpc field must be '2.0'")
    if "id" not in response or not _valid_id(response["id"]):
        raise RpcProtocolError("response must contain a valid request ID")
    if type(response["id"]) is not type(expected_id) or response["id"] != expected_id:
        raise RpcProtocolError("response ID does not match the request")

    has_result = "result" in response
    has_error = "error" in response
    if has_result == has_error:
        raise RpcProtocolError("response must contain exactly one of result or error")

    if has_error:
        error = response["error"]
        if not isinstance(error, dict):
            raise RpcProtocolError("error must be a JSON object")
        code = error.get("code")
        message = error.get("message")
        if isinstance(code, bool) or not isinstance(code, int):
            raise RpcProtocolError("error code must be an integer")
        if not isinstance(message, str):
            raise RpcProtocolError("error message must be a string")
        raise RpcRemoteError(code, message, error.get("data"))

    return response["result"]


__all__ = ["RpcProtocolError", "RpcRemoteError", "validate_response"]
