import allure

from api_usage import Orders
from data_for_tests import ErrorMessages as Em


class TestGetOrder:
    api_orders = Orders()

    @allure.title("Test getting orders as an authorized user")
    def test_get_orders_authorized_user(self, authorization_data_user_with_orders):
        print(authorization_data_user_with_orders)
        status_code, response_body = self.api_orders.get_user_orders(authorization_data_user_with_orders)
        assert status_code == 200
        assert len(response_body["orders"]) == 5

    @allure.title("Test getting orders as an unauthorized user")
    def test_get_orders_unauthorized_user(self):
        status_code, response_body = self.api_orders.get_user_orders()
        assert status_code == 401
        assert response_body["message"] == Em.you_should_be_authorized
