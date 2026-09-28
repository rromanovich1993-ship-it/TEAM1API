import allure
import requests
from services.users.payloads import Payloads
from config.headers import Headers
from services.users.endpoints import Endpoints


class UsersAPI:

    def __init__(self):
        self.payloads = Payloads()
        self.headers = Headers()
        self.endpoints = Endpoints()


    @allure.step("Create users")
    def create_user(self):
        response = requests.post(
            ...
        )

