import allure

import pytest
from api_usage import Users
from data_for_tests import GeneratedUserData as Gud, ErrorMessages as Em


class TestUserDataUpdate:
    api_users = Users()

    @allure.title("Test update user data as an unauthorized user")
    @pytest.mark.parametrize(
        "changed_data",
        [
            Gud.change_name_field,
            Gud.change_email_field,
            Gud.change_full_data
        ]
    )
    def test_update_user_data_unauthorized_user(self, changed_data):
        status_code, response_body = self.api_users.update_user_data(changed_data)

        assert status_code == 401
        assert response_body["message"] == Em.you_should_be_authorized

    @allure.title("Test update a name field as authorized user")
    def test_update_user_name_authorized_user(self, authorization_data):
        changed_data = Gud.change_name_field
        status_code, response_body = self.api_users.update_user_data(changed_data, authorization_data)

        assert status_code == 200
        assert response_body["user"]["name"] == changed_data["name"]

    @allure.title("Test update an email field as authorized user")
    def test_update_user_email_authorized_user(self, authorization_for_update_user_data):
        changed_data = Gud.change_email_field
        login_data = authorization_for_update_user_data
        status_code, response_body = self.api_users.update_user_data(changed_data, login_data)
        login_data["email"] = changed_data["email"]

        assert status_code == 200
        assert response_body["user"]["email"] == changed_data["email"]
        self.api_users.delete_user(login_data)

    @allure.title("Test update full user data as an authorized user")
    def test_update_full_user_data_authorized_user(self, authorization_for_update_user_data):
        full_data = Gud.change_full_data
        login_data = authorization_for_update_user_data
        status_code, response_body = self.api_users.update_user_data(full_data, login_data)
        login_data["email"] = full_data["email"]

        assert status_code == 200
        assert response_body["user"] == full_data
        self.api_users.delete_user(login_data)
