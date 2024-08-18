import allure
import pytest
from api_usage import Users
from data_for_tests import GeneratedUserData as Gud, ErrorMessages as Em


class TestUserRegistration:
    api_user = Users()

    @allure.title("Test uniq user registration")
    def test_register_uniq_user(self, registration_data):
        status_code, response_body = self.api_user.register_new_user(registration_data)
        assert status_code == 200
        assert "accessToken" in response_body

    @allure.title("Test registration of the user that already exists")
    def test_register_same_user(self, registration_data):
        self.api_user.register_new_user(registration_data)
        status_code, response_body = self.api_user.register_new_user(registration_data)
        assert status_code == 403
        assert response_body["message"] == Em.user_already_exists

    @allure.title("Test incomplete data")
    @pytest.mark.parametrize(
        "incomplete_registration_data",
        [
            Gud.registration_data_wo_login,
            Gud.registration_data_wo_email,
            Gud.registration_data_wo_password
        ]
    )
    def test_registration_with_incomplete_data(self, incomplete_registration_data):
        status_code, response_body = self.api_user.register_new_user(incomplete_registration_data)
        assert status_code == 403
        assert response_body["message"] == Em.email_name_password_are_required
