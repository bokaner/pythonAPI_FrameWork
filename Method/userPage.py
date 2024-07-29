import requests

from TestData import test_data
from Logs import logs_file


class UserPageMethod:
    log = logs_file.get_logs()

    def check_login_api_with_correct_credentials(self):
        """

        :return:
        """
        flag = True
        try:
            r = requests.post('https://reqres.in/api/login', data=test_data.valid_credentials)
            print(r.status_code)
            status_code = r.status_code
            self.log.info(f"Status code is {status_code}")
            if status_code != 200:
                self.log.error(f"Status code is {status_code} not 200")
                flag = False
            else:
                self.log.info(f"correct Status code is {status_code} ")

            if not r.json()['token']:
                self.log.error(f"Token is not presnet")
                flag = False
            else:
                self.log.info(f"Token is present ")
        except Exception as e:
            self.log.error(f"Exception occured:{e}")
            flag =False

        return flag

    def check_login_api_with_Incorrect_credentials(self):
        """

        :return:
        """
        flag = True
        try:

            r = requests.post('https://reqres.in/api/login', data=test_data.Invalid_credentials)
            print(r.status_code)
            status_code = r.status_code
            if status_code != 400:
                flag = False
            if not r.json()['token']:
                flag = False
        except Exception as e:
            self.log.error(f"Exception occured:{e}")
            flag = False

        return flag
