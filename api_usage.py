import allure
import json
import requests
from endpoints import Endpoints as Ep

URL = "https://stellarburgers.nomoreparties.site"


class Users:
    @allure.step("User registration")
    def register_new_user(self, registration_data):
        payload = json.dumps(registration_data)
        response = requests.post(
            f"{URL}{Ep.create_user_path}",
            data=payload,
            headers={
                "Content-type": "application/json"
            }
        )
        return response.status_code, response.json()

    @allure.step("User login")
    def login(self, login_data):
        payload = json.dumps(login_data)
        response = requests.post(
            f"{URL}{Ep.login_path}",
            data=payload,
            headers={
                "Content-type": "application/json"
            }
        )
        return response.status_code, response.json()

    @allure.step("Get access token")
    def get_access_token(self, login_data):
        status_code, response_body = self.login(login_data)
        access_token = response_body["accessToken"]
        return access_token

    @allure.step("Update user data")
    def update_user_data(self, changed_data, login_data=None):
        payload = json.dumps(changed_data)
        headers = {"Content-type": "application/json"}
        if login_data:
            access_token = self.get_access_token(login_data)
            headers["Authorization"] = access_token

        response = requests.patch(
            f"{URL}{Ep.users_path}",
            data=payload,
            headers=headers
        )
        return response.status_code, response.json()

    @allure.step("Delete user")
    def delete_user(self, login_data):
        access_token = self.get_access_token(login_data)
        requests.delete(
            f"{URL}{Ep.users_path}",
            headers={
                "Content-type": "application/json",
                "Authorization": access_token
            }
        )


class Orders:
    user = Users()

    @allure.step("Make order")
    def make_order(self, ingredients=None, login_data=None):
        if ingredients:
            order_data = {"ingredients": ingredients}
        else:
            order_data = {"ingredients": []}
        payload = json.dumps(order_data)

        headers = {"Content-type": "application/json"}

        if login_data:
            access_token = self.user.get_access_token(login_data)
            headers["Authorization"] = access_token

        response = requests.post(
            f"{URL}{Ep.orders_path}",
            data=payload,
            headers=headers
        )
        return response.status_code, response.json()

    @allure.step("Get user order")
    def get_user_orders(self, login_data=None):

        headers = {}
        if login_data:
            access_token = self.user.get_access_token(login_data)
            headers["Authorization"] = access_token

        response = requests.get(
            f"{URL}{Ep.orders_path}",
            headers=headers
        )
        return response.status_code, response.json()
