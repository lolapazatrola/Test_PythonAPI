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

    @staticmethod
    def assert_response_content_for_missing_field(response: Response, expected_missing_field):
        assert response.content.decode("utf-8") == f"The following required params are missed: {expected_missing_field}", \
            f"Unexpected missing field {response.content.decode('utf-8')}, expected missing field is {expected_missing_field} "

    @staticmethod
    def assert_response_content_for_existing_email(response: Response, expected_existing_email):
        assert response.content.decode("utf-8") == f"Users with email '{expected_existing_email}' already exists", \
            f"Unexpected response content {response.content.decode('utf-8')}"

    @staticmethod
    def assert_response_content_for_invalid_email_format(response: Response):
        assert response.content.decode("utf-8") == "Invalid email format", \
            f"Unexpected response content {response.content.decode('utf-8')}"