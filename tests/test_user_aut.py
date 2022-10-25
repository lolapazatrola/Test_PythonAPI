import pytest
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertioins import Assertions
import allure


@allure.epic("User Authorization cases")
class TestUserAuth(BaseCase):
    exclude_params = {
        ("no_cookies"),
        ("no_token")
    }

    def setup(self):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }

        responce1 = MyRequests.post("/user/login", data=data)

        self.auth_sid = self.get_cookie(responce1, "auth_sid")
        self.token = self.get_header(responce1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(responce1, "user_id")

    @allure.description("This test successfully authorize user by email and password")
    def test_user_auth(self):
        responce2 = MyRequests.get(
            "/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_json_value_by_name(
            responce2,
            "user_id",
            self.user_id_from_auth_method,
            "Error"
        )

    @allure.description("This test check authorization status w/o sending auth token and headers")
    @pytest.mark.parametrize("condition", exclude_params)
    def test_negative_auth_check(self, condition):
        if condition == "no_cookies":
            responce2 = MyRequests.get("/user/auth",
                                     headers={"x-csrf-token": self.token})

        else:
            responce2 = MyRequests.get("/user/auth", cookies={"auth_sid": self.auth_sid})

        Assertions.assert_json_value_by_name(
            responce2,
            "user_id",
            0,
            "Error"
        )
