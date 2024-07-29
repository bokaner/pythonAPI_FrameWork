import allure
import requests

from TestCases.BaseTest import BaseTest
from TestCases.conftest import allureLogs
from TestData import test_data
from Method.loginPage import LoginPage


class TestLogin(BaseTest):

    @allure.title("Test Authentication")
    @allure.description(
        "This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
    @allure.tag("API", "Credentials", "Authentication")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "UJjwal")
    @allure.link("https://dev.example.com/", name="Website")
    @allure.issue("AUTH-123")
    @allure.testcase("TMS-456")
    def test_login_with_correct_credentials(self):
        """ Login Page : test login Page with correct credentials"""
        allureLogs("Checking the button is displayed ")
        self.lp = LoginPage()
        allureLogs("Checking the status ")

        status = self.lp.check_login_api_with_correct_credentials()
        allureLogs("Status reponse ")

        assert status

    def test_login_with_incorrect_credentils(self):
        """ Login Page : test login Page with correct credentials"""
        self.lp = LoginPage()
        flag = self.lp.check_login_api_with_Incorrect_credentials()
        assert flag is False
