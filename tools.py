class GenerateData:
    @staticmethod
    def generate_registration_data(username, email, password):
        registration_data = {}
        if username:
            registration_data["name"] = username
        if password:
            registration_data["email"] = email
        if password:
            registration_data["password"] = password
        return registration_data

    @staticmethod
    def return_login_data(registration_data):
        login_data = {
            "email": registration_data["email"],
            "password": registration_data["password"]
        }
        return login_data
