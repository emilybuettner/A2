import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def login_blog(self):
        user = "one"
        pwd = "12345"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[3]/input").click()
        time.sleep(5)


        # elem.send_keys(Keys.RETURN)
        # driver.get("http://127.0.0.1:8000")
        # assert "Logged In"
        # time.sleep(5)

    # def tearDown(self):
    #     self.driver.close()


if __name__ == "__main__":
    unittest.main()
