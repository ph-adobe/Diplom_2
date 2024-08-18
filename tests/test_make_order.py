import allure
from api_usage import Orders
from data_for_tests import GeneratedOrderData as God, ErrorMessages as Em


class TestMakeOrder:
    api_orders = Orders()

    @allure.title("Test making order with ingredients as an authorized user")
    def test_make_order_with_ingredients_and_login(self, authorization_data):
        status_code, response_body = self.api_orders.make_order(ingredients=God.ingredients,
                                                                login_data=authorization_data)
        assert status_code == 200
        assert response_body["order"]["owner"]["email"] == authorization_data["email"]
        assert response_body["order"]["status"] == "done"

    @allure.title("Test making order with ingredients as an unauthorized user")
    def test_make_order_with_ingredients_wo_login(self):
        status_code, response_body = self.api_orders.make_order(ingredients=God.ingredients)
        assert status_code == 200
        assert response_body["order"]["number"]

    @allure.title("Test making order without ingredients as an authorized user")
    def test_make_order_wo_ingredients_with_login(self, authorization_data):
        status_code, response_body = self.api_orders.make_order(login_data=authorization_data)
        assert status_code == 400
        assert response_body["message"] == Em.ingredient_ids_must_be_provided

    @allure.title("Test making order without ingredients as an unauthorized user")
    def test_make_order_wo_ingredients_wo_login(self):
        status_code, response_body = self.api_orders.make_order()
        assert status_code == 400
        assert response_body["message"] == Em.ingredient_ids_must_be_provided

    @allure.title("Test making order with invalid ingredients as an authorized user")
    def test_make_order_invalid_ingredients_with_login(self, authorization_data):
        status_code, response_body = self.api_orders.make_order(
            ingredients=God.ingredients_with_invalid_hash, login_data=authorization_data)
        assert status_code == 400
        assert response_body["message"] == Em.incorrect_ids

    @allure.title("Test making order without ingredients as an unauthorized user")
    def test_make_order_invalid_ingredients_wo_login(self):
        status_code, response_body = self.api_orders.make_order(ingredients=God.ingredients_with_invalid_hash)
        assert status_code == 400
        assert response_body["message"] == Em.incorrect_ids
