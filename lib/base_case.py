import json.decoder
from requests import Response
from datetime import datetime

class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, "error"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, "error"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, "error"

        assert name in response_as_dict, "error"
        return response_as_dict[name]

    def prepare_register_data(self, email=None, username=None):
        if email is None:
            base_part = "testemail"
            domain = "@example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}{domain}"
        if username is None:
            username = "testUserName"
        return {
            'password': "123",
            'username': username,
            'firstName': "testFirstName",
            'lastName': "testLastName",
            'email': email
        }

    def prepare_register_data_with_missing_field(self, field):
        if field == "password":
            return {
                'username': "testUserName",
                'firstName': "testFirstName",
                'lastName': "testLastName",
                'email': "test@mail.com"
            }
        elif field == "username":
            return {
                'password': '123',
                'firstName': "testFirstName",
                'lastName': "testLastName",
                'email': "test@mail.com"
            }
        elif field == "firstName":
            return {
                'username': "testUserName",
                'password': '123',
                'lastName': "testLastName",
                'email': "test@mail.com"
            }
        elif field == "lastName":
            return {
                'username': "testUserName",
                'password': '123',
                'firstName': "testFirstName",
                'email': "test@mail.com"
            }
        elif field == 'email':
            return {
                'username': "testUserName",
                'password': '123',
                'firstName': "testFirstName",
                'lastName': "testLastName",
            }
        else:
            raise Exception(f"Unknown field name {field}")