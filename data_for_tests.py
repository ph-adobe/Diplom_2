import random

from faker import Faker
from tools import GenerateData as Gd


class GeneratedUserData:
    fake = Faker()
    name = fake.user_name()
    email = fake.email()
    password = fake.password()

    generated_complete_data = Gd.generate_registration_data(name, email, password)

    registration_data_wo_login = Gd.generate_registration_data(None, email, password)
    registration_data_wo_password = Gd.generate_registration_data(name, email, None)
    registration_data_wo_email = Gd.generate_registration_data(name, None, password)

    not_registered_login_data = {"email": fake.email(), "password": fake.password()}

    change_name_field = {"name": fake.user_name()}
    change_email_field = {"email": fake.email()}
    change_full_data = {"name": fake.user_name(), "email": fake.email()}


class GeneratedOrderData:
    fake = Faker()

    buns = [
        "61c0c5a71d1f82001bdaaa6d",
        "61c0c5a71d1f82001bdaaa6c"
    ]

    sauces = [
        "61c0c5a71d1f82001bdaaa72",
        "61c0c5a71d1f82001bdaaa73",
        "61c0c5a71d1f82001bdaaa74",
        "61c0c5a71d1f82001bdaaa75"
    ]
    fillings = [
        "61c0c5a71d1f82001bdaaa6f",
        "61c0c5a71d1f82001bdaaa70",
        "61c0c5a71d1f82001bdaaa71",
        "61c0c5a71d1f82001bdaaa6e",
        "61c0c5a71d1f82001bdaaa76",
        "61c0c5a71d1f82001bdaaa77",
        "61c0c5a71d1f82001bdaaa78",
        "61c0c5a71d1f82001bdaaa7a"
    ]

    ingredients = [
        fake.random_element(buns),
        *fake.random_elements(sauces, random.randint(0, 4), True),
        *fake.random_elements(fillings, random.randint(0, 8), True)
    ]

    ingredients_with_invalid_hash = [
        fake.random_element(buns)[::-1],
        *[el[::-1] for el in fake.random_elements(sauces, random.randint(0, 4), True)],
        *[el[::-1] for el in fake.random_elements(fillings, random.randint(0, 8), True)]
    ]


class ErrorMessages:
    user_already_exists = "User already exists"
    email_name_password_are_required = "Email, password and name are required fields"
    incorrect_email_or_password = "email or password are incorrect"
    ingredient_ids_must_be_provided = "Ingredient ids must be provided"
    incorrect_ids = "One or more ids provided are incorrect"
    you_should_be_authorized = "You should be authorised"
