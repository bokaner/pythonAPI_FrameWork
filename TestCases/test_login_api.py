import requests

from TestCases.BaseTest import BaseTest
from TestData import test_data
from Method.loginPage import LoginPage


class TestLogin(BaseTest):


    def test_login_with_correct_credentials(self):
        """ Login Page : test login Page with correct credentials"""
        self.lp = LoginPage()
        status = self.lp.check_login_api_with_correct_credentials()
        assert status

    def test_login_with_incorrect_credentils(self):
        self.lp = LoginPage()
        flag = self.lp.check_login_api_with_Incorrect_credentials()
        assert flag is False
