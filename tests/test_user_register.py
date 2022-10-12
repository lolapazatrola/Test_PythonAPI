import requests
from lib.base_case import BaseCase
from lib.assertioins import Assertions
from datetime import datetime


class TestUserRegister(BaseCase):
    def setup(self):
        base_part = "testemail"
        domain = "@example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}{domain}"

    def test_create_user_successfully(self):
        data = {
            'password': '123',
            'username': 'testUserName',
            'firstName': 'testFirstName',
            'lastName': 'testLastName',
            'email': self.email
        }

        responce = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(responce, 200)
        Assertions.assert_json_has_key(responce, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '123',
            'username': 'testUserName',
            'firstName': 'testFirstName',
            'lastName': 'testLastName',
            'email': email
        }

        responce = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(responce, 400)
        assert responce.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Unexpected responce content {responce.content.decode('utf-8')}"
