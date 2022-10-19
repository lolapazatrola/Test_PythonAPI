from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertioins import Assertions

class TestUserRegister(BaseCase):
    def test_create_user_successfully(self):
        data = self.prepare_register_data()

        responce = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(responce, 200)
        Assertions.assert_json_has_key(responce, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_register_data(email)

        responce = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(responce, 400)
        assert responce.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Unexpected responce content {responce.content.decode('utf-8')}"
