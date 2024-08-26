import pytest
from data_for_tests import GeneratedUserData as Gud, GeneratedOrderData as God
from tools import GenerateData as Gd
from api_usage import Users, Orders


@pytest.fixture
def registration_data():
    registration_data = Gud.generated_complete_data
    yield registration_data
    login_data = Gd.return_login_data(registration_data)
    api_users = Users()
    api_users.delete_user(login_data)


@pytest.fixture()
def authorization_data(registration_data):
    api_users = Users()
    api_users.register_new_user(registration_data)
    return Gd.return_login_data(registration_data)


@pytest.fixture
def authorization_data_user_with_orders(authorization_data):
    api_orders = Orders()
    for _ in range(5):
        api_orders.make_order(God.ingredients, authorization_data)
    return authorization_data


# Т.к. в результате теста меняются данные логина, создана отдельная фикстура
@pytest.fixture
def authorization_for_update_user_data():
    api_users = Users()
    registration_data_without_deleting_user = Gud.generated_complete_data
    api_users.register_new_user(registration_data_without_deleting_user)
    return Gd.return_login_data(registration_data_without_deleting_user)



