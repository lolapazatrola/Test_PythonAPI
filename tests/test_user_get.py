from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertioins import Assertions

class TestUserGet(BaseCase):
    def test_get_user_details_not_auth(self):
        responce = MyRequests.get("/user/2")

        Assertions.assert_json_has_key(responce, "username")
        Assertions.assert_json_has_not_key(responce, "email")
        Assertions.assert_json_has_not_key(responce, "firstName")
        Assertions.assert_json_has_not_key(responce, "lastName")

    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        responce1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(responce1, "auth_sid")
        token = self.get_header(responce1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(responce1, "user_id")

        responce2 = MyRequests.get(
            f"/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(responce2, expected_fields)
