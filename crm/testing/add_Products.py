import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class test_Customer(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_mfscrm(self):
        user = "one"
        password = "12345"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(password)
        time.sleep(5)

        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[2]/td[1]/a").click()
        time.sleep(5)




    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

