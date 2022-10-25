from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertioins import Assertions
import allure


@allure.epic("User Delete cases")
class TestUserDelete(BaseCase):
    @allure.description("This test try to delete user with id 2")
    def test_try_to_delete_user_with_id_2(self):
        # Login as user with id 2
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")
        user_id = self.get_json_value(response, "user_id")

        # Try to delete
        response2 = MyRequests.delete(f"/user/{user_id}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid})

        Assertions.assert_code_status(response2, 400)
        Assertions.assert_response_content(
            response2,
            "Please, do not delete test users with ID 1, 2, 3, 4 or 5.",
            f"Unexpected response content '{response2.content.decode('utf-8')}', expected "
            f"'Please, do not delete test users with ID 1, 2, 3, 4 or 5.'"
        )

    @allure.description("This test delete user that just created")
    def test_delete_just_created_user(self):
        # Register new user
        register_data = self.prepare_register_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        email = register_data["email"]
        password = register_data["password"]
        user_id = self.get_json_value(response1, "id")

        # Login as created user
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # Delete created user
        response3 = MyRequests.delete(f"/user/{user_id}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid})

        Assertions.assert_code_status(response3, 200)

        # Try to get deleted user information
        response4 = MyRequests.get(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid})

        Assertions.assert_code_status(response4, 404)
        Assertions.assert_response_content(
            response4,
            "User not found",
            f"Unexpected response content '{response4.content.decode('utf-8')}', expected"
            f" 'User not found'"
        )

#   В этом примере тоже баг!
    # def test_try_to_delete_user_while_authorized_as_another_user(self):
    #     # Register first new user
    #     register_data = self.prepare_register_data()
    #     response1 = MyRequests.post("/user/", data=register_data)
    #     Assertions.assert_code_status(response1, 200)
    #     Assertions.assert_json_has_key(response1, "id")
    #     first_user_email = register_data["email"]
    #     first_user_password = register_data["password"]
    #     first_user_id = self.get_json_value(response1, "id")
    #
    #     # Register second new user
    #     register_data = self.prepare_register_data()
    #     response1 = MyRequests.post("/user/", data=register_data)
    #     Assertions.assert_code_status(response1, 200)
    #     Assertions.assert_json_has_key(response1, "id")
    #     second_user_email = register_data["email"]
    #     second_user_password = register_data["password"]
    #     second_user_id = self.get_json_value(response1, "id")
    #
    #     # Login as first user
    #     login_data = {
    #         'email': first_user_email,
    #         'password': first_user_password
    #     }
    #     response2 = MyRequests.post("/user/login", data=login_data)
    #     auth_sid = self.get_cookie(response2, "auth_sid")
    #     token = self.get_header(response2, "x-csrf-token")
    #
    #     # Try to delete second user, while authorized as first user
    #     response3 = MyRequests.delete(f"/user/{second_user_id}",
    #                                   headers={"x-csrf-token": token},
    #                                   cookies={"auth_sid": auth_sid})
    #
    #     response4 = MyRequests.get(f"/user/{second_user_id}",
    #                                headers={"x-csrf-token": token},
    #                                cookies={"auth_sid": auth_sid})
    #
    #     response5 = MyRequests.get(f"/user/{first_user_id}",
    #                                headers={"x-csrf-token": token},
    #                                cookies={"auth_sid": auth_sid})
