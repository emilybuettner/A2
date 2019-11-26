import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class test_Cust(unittest.TestCase):

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

        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[3]/input").click()
        time.sleep(5)

        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[1]/a").click()
        time.sleep(5)

        # elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[1]/a").click()
        # time.sleep(5)
        cust_name = "Rick"
        elem = driver.find_element_by_id("id_cust_name")
        # time.sleep(5)
        elem.send_keys(cust_name)

        cust_role = "Selenium Test 1"
        elem = driver.find_element_by_id("id_role")
        # time.sleep(5)
        elem.send_keys(cust_role)

        cust_email = "SeleniumTest1@1.com"
        elem = driver.find_element_by_id("id_email")
        # time.sleep(5)
        elem.send_keys(cust_email)

        cust_bldgroom = "PKI 101"
        elem = driver.find_element_by_id("id_bldgroom")
        # time.sleep(5)
        elem.send_keys(cust_bldgroom)

        cust_address = "100 S 100 St"
        elem = driver.find_element_by_id("id_address")
        # time.sleep(5)
        elem.send_keys(cust_address)

        cust_account = "444"
        elem = driver.find_element_by_id("id_account_number")
        # time.sleep(5)
        elem.send_keys(cust_account)

        cust_city = "Omaha"
        elem = driver.find_element_by_id("id_city")
        # time.sleep(5)
        elem.send_keys(cust_city)

        cust_state = "Nebraska"
        elem = driver.find_element_by_id("id_state")
        # time.sleep(5)
        elem.send_keys(cust_state)

        cust_phone = "402-987-4578"
        elem = driver.find_element_by_id("id_phone_number")
        # time.sleep(5)
        elem.send_keys(cust_phone)

        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[12]/div/p/span[1]/a[1]").click()
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[12]/div/p/span[2]/a[1]").click()
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
