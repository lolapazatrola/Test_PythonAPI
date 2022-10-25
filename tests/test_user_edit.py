from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertioins import Assertions
import pytest
import allure


@allure.epic("User Edit cases")
class TestUserEdit(BaseCase):
    field_name = {
        'password',
        'username',
        'firstName',
        'lastName',
        'email'
    }

    @allure.description("This test edit user data on user that just created")
    def test_user_just_created_user(self):
        # REGISTER
        register_data = self.prepare_register_data()
        responce1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(responce1, 200)
        Assertions.assert_json_has_key(responce1, "id")
        email = register_data["email"]
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

    @pytest.mark.parametrize("field", field_name)
    @allure.description("This test try to edit data while not authorized")
    def test_change_user_data_while_not_authorized(self, field):
        # Try to change field without auth
        test_user_id = '48450'
        response = MyRequests.put(f"/user/{test_user_id}",
                                  data={field: "test_value"})
        Assertions.assert_code_status(response, 400)
        Assertions.assert_response_content(
            response,
            "Auth token not supplied",
            f"Unexpected response content {response.content.decode('utf-8')}"
        )

    @allure.description("This test try to edit user first name on one symbol")
    def test_change_authorized_user_first_name_on_one_symbol(self):
        # Login as test user
        login_data = {
            'email': 'testemail10242022203338@example.com',
            'password': '123'
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        user_id = self.get_json_value(response2, "user_id")

        # Try to edit first name
        new_name = "T"
        response3 = MyRequests.put(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data={"firstName": new_name})

        Assertions.assert_code_status(response3, 400)
        Assertions.assert_json_value_by_name(
            response3,
            "error",
            "Too short value for field firstName",
            "Unexpected error in json"
        )

    @allure.description("This test try to edit user email on invalid values")
    def test_change_authorized_user_email_on_invalid_values(self):
        # LOGIN
        login_data = {
            'email': 'testemail10242022203338@example.com',
            'password': '123'
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        user_id = self.get_json_value(response2, "user_id")

        # EDIT try to edit email
        new_email = "emailWithoutAD"
        response3 = MyRequests.put(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data={"email": new_email})

        Assertions.assert_code_status(response3, 400)
        Assertions.assert_response_content(
            response3,
            "Invalid email format",
            f"Unexpected response content {response3.content.decode('utf-8')}"
        )

##   В этом кейсе вероятно баг, так как данные изменяются для пользователя, в котором пользователь авторизовался

##
#     def test_change_user_data_while_authorized_as_another_user(self):
#         # LOGIN
#         login_data = {
#             'email': 'testemail10242022203338@example.com',
#             'password': '123'
#         }
#         response2 = MyRequests.post("/user/login", data=login_data)
#         auth_sid = self.get_cookie(response2, "auth_sid")
#         token = self.get_header(response2, "x-csrf-token")
#
#         # Try to change another user data
#         test_user_id_for_change_data = 48451
#         username = 'sssFirstNaimovich'
#         response3 = MyRequests.put(f"/user/{test_user_id_for_change_data}",
#                                    headers={"x-csrf-token": token},
#                                    cookies={"auth_sid": auth_sid},
#                                    data={"username": username})
#
#         print(response3.status_code)
#         print(response3.content.decode("utf-8"))