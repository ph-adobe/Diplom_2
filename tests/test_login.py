import allure

from api_usage import Users
from data_for_tests import GeneratedUserData as Gud, ErrorMessages as Em


class TestUserAuthorization:
    api_users = Users()

    @allure.title("Test authorization with valid credentials")
    def test_login_with_valid_credential(self, authorization_data):
        status_code, response_body = self.api_users.login(authorization_data)

        assert status_code == 200
        assert "accessToken" in response_body

    @allure.title("Test authorization of not registered user")
    def test_login_not_registered_user(self):
        status_code, response_body = self.api_users.login(Gud.not_registered_login_data)

        assert status_code == 401
        assert response_body["message"] == Em.incorrect_email_or_password

    @allure.title("Test authorization with incorrect password")
    def test_login_with_incorrect_password(self, authorization_data):
        login_data = {
            "email": authorization_data["email"],
            "password": "123456"
        }
        status_code, response_body = self.api_users.login(login_data)

        assert status_code == 401
        assert response_body["message"] == Em.incorrect_email_or_password

    @allure.title("Test authorization with incorrect email")
    def test_login_with_incorrect_email(self, authorization_data):
        login_data = {
            "email": "test@test.ru",
            "password": authorization_data["password"]
        }
        status_code, response_body = self.api_users.login(login_data)

        assert status_code == 401
        assert response_body["message"] == Em.incorrect_email_or_password
