from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertioins import Assertions
import pytest
import allure


@allure.epic("User Register cases")
class TestUserRegister(BaseCase):
    missing_field_name = {
        'password',
        'username',
        'firstName',
        'lastName',
        'email'
    }

    @allure.description("This test successfully create user")
    def test_create_user_successfully(self):
        data = self.prepare_register_data()

        responce = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(responce, 200)
        Assertions.assert_json_has_key(responce, "id")

    @allure.description("This test try to create user with existing email")
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_register_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        Assertions.assert_response_content(
            response,
            f"Users with email '{email}' already exists",
            f"Unexpected response content {response.content.decode('utf-8')}"
        )

    @allure.description("This test try to create users with incorrect email")
    def test_create_user_with_incorrect_email(self):
        email = 'emailWithoutAD'
        data = self.prepare_register_data(email)

        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        Assertions.assert_response_content(
            response,
            "Invalid email format",
            f"Unexpected response content {response.content.decode('utf-8')}"
        )

    @allure.description(f"This test try to create user with missing field {missing_field_name}")
    @pytest.mark.parametrize("missing_field", missing_field_name)
    def test_create_user_with_missing_field(self, missing_field):
        data = self.prepare_register_data_with_missing_field(missing_field)

        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        Assertions.assert_response_content(
            response,
            f"The following required params are missed: {missing_field}",
            f"Unexpected missing field {response.content.decode('utf-8')}, expected missing field is {missing_field}"
            )

    @allure.description("This test try to create user with username one symbol")
    def test_create_user_with_username_one_symbol(self):
        username = 't'
        data = self.prepare_register_data(None, username)

        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        Assertions.assert_response_content(
            response,
            "The value of 'username' field is too short",
            f"Unexpected response content {response.content.decode('utf-8')}"
        )

    @allure.description("This test try to create user with username longer then 250 symbol")
    def test_create_user_with_username_longer_250_symbol(self):
        username = 't' * 251
        data = self.prepare_register_data(None, username)

        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        Assertions.assert_response_content(
            response,
            "The value of 'username' field is too long",
            f"Unexpected response content {response.content.decode('utf-8')}"
        )
