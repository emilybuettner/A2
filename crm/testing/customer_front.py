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
        driver.get("http://127.0.0.1:8000/")
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        time.sleep(5)

        user = "one"
        password = "12345"

        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(password)

        time.sleep(2)

        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/input[2]").click()

        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a").click()
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[12]/a").click()
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[14]/a").click()
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[2]/a").click()




        time.sleep(6)


def tearDown(self):
    self.driver.close()



if __name__ == "__main__":
    unittest.main()


