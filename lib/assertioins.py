import json

from requests import Response

class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, "error"

        assert name in response_as_dict, "error"
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, "error"

        assert name in response_as_dict, f"Responce JSON doesn't have key '{name}'"

    @staticmethod
    def assert_json_has_keys(responce: Response, names: list):
        try:
            responce_as_dict = responce.json()
        except json.JSONDecodeError:
            assert False, "error"

        for name in names:
            assert name in responce_as_dict, f"Responce JSON doesn't have key '{name}'"

    @staticmethod
    def assert_json_has_not_key(responce: Response, name):
        try:
            responce_as_dict = responce.json()
        except json.JSONDecodeError:
            assert False, "error"

        assert name not in responce_as_dict, f"Responce JSON shouldn't have key '{name}'"

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code! Expected: {expected_status_code}. Actual: {response.status_code}"
