import unittest

from chainwatch import RpcProtocolError, RpcRemoteError, validate_response


class JsonRpcResponseTests(unittest.TestCase):
    def test_valid_result_is_returned(self):
        body = b'{"jsonrpc":"2.0","id":7,"result":"0x0"}'
        self.assertEqual(validate_response(body, 7), "0x0")

    def test_null_result_is_not_confused_with_missing_result(self):
        self.assertIsNone(validate_response(
            {"jsonrpc": "2.0", "id": "balance-1", "result": None},
            "balance-1",
        ))

    def test_remote_error_remains_distinct_from_empty_result(self):
        body = {"jsonrpc": "2.0", "id": 4,
                "error": {"code": -32005, "message": "rate limit", "data": {"retry": True}}}
        with self.assertRaises(RpcRemoteError) as caught:
            validate_response(body, 4)
        self.assertEqual(caught.exception.code, -32005)
        self.assertEqual(caught.exception.message, "rate limit")
        self.assertEqual(caught.exception.data, {"retry": True})

    def test_rejects_missing_or_mismatched_id(self):
        for body in (
            {"jsonrpc": "2.0", "result": 1},
            {"jsonrpc": "2.0", "id": 8, "result": 1},
            {"jsonrpc": "2.0", "id": True, "result": 1},
        ):
            with self.subTest(body=body), self.assertRaises(RpcProtocolError):
                validate_response(body, 7)

    def test_rejects_result_and_error_or_neither(self):
        bodies = (
            {"jsonrpc": "2.0", "id": 1, "result": 1, "error": {"code": 1, "message": "x"}},
            {"jsonrpc": "2.0", "id": 1},
        )
        for body in bodies:
            with self.subTest(body=body), self.assertRaises(RpcProtocolError):
                validate_response(body, 1)

    def test_rejects_malformed_error_shapes(self):
        for error in ("failed", {"code": True, "message": "bad"}, {"code": -1}):
            body = {"jsonrpc": "2.0", "id": 1, "error": error}
            with self.subTest(error=error), self.assertRaises(RpcProtocolError):
                validate_response(body, 1)

    def test_rejects_non_standard_json_numeric_constants(self):
        for constant in ("NaN", "Infinity", "-Infinity"):
            body = f'{{"jsonrpc":"2.0","id":1,"result":{constant}}}'
            with self.subTest(constant=constant), self.assertRaises(RpcProtocolError):
                validate_response(body, 1)

    def test_rejects_malformed_json_and_wrong_protocol_version(self):
        with self.assertRaises(RpcProtocolError):
            validate_response("{broken", 1)
        with self.assertRaises(RpcProtocolError):
            validate_response({"jsonrpc": "1.0", "id": 1, "result": 1}, 1)


if __name__ == "__main__":
    unittest.main()
