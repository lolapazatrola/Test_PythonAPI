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