import json.decoder
from requests import Response
from datetime import datetime

class BaseCase:
    def get_cookie(self, responce: Response, cookie_name):
        assert cookie_name in responce.cookies, "error"
        return responce.cookies[cookie_name]

    def get_header(self, responce: Response, headers_name):
        assert headers_name in responce.headers, "error"
        return responce.headers[headers_name]

    def get_json_value(self, responce: Response, name):
        try:
            responce_as_dict = responce.json()
        except json.decoder.JSONDecodeError:
            assert False, "error"

        assert name in responce_as_dict, "error"
        return responce_as_dict[name]

    def prepare_register_data(self, email=None):
        if email is None:
            base_part = "testemail"
            domain = "@example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}{domain}"
        return {
            'password': '123',
            'username': 'testUserName',
            'firstName': 'testFirstName',
            'lastName': 'testLastName',
            'email': email
        }