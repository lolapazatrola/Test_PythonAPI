from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertioins import Assertions


class TestUserEdit(BaseCase):
    def test_user_just_created_user(self):
        # REGISTER
        register_data = self.prepare_register_data()
        responce1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(responce1, 200)
        Assertions.assert_json_has_key(responce1, "id")

        email = register_data["email"]
        first_name = register_data["firstName"]
        password = register_data["password"]
        user_id = self.get_json_value(responce1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        responce2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(responce2, "auth_sid")
        token = self.get_header(responce2, "x-csrf-token")

        # EDIT
        new_name = "Changed Name"

        responce3 = MyRequests.put(f"/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"firstName": new_name})

        Assertions.assert_code_status(responce3, 200)

        # CHECK OLD NAME AND NEW NAME
        responce4 = MyRequests.get(f"/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid})

        Assertions.assert_json_value_by_name(
            responce4,
            "firstName",
            new_name,
            "Wrong name after user edit"
        )
