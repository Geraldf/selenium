# import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv
load_dotenv()


class PythonOrgSearch():

    def setUp(self):
        self.driver = webdriver.Firefox()
        self. delay = 10  # seconds

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get(os.getenv('url'))
        try:
            time.sleep(7)
            wait = WebDriverWait(driver, 10)
            title = driver.title
            if (title == 'Anmelden'):
                username = driver.find_element_by_id("userNameInput")
                username.send_keys(os.getenv('user'))
                driver.find_element_by_id(
                    "passwordInput").send_keys(os.getenv('password'))
                driver.find_element_by_id("submitButton").click()
                time.sleep(7)
            myElem = WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/h3')))
            # clear the filter
            ClearFilter = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="main"]/div/div[3]/div[1]/div[1]/div/div[3]/button[1]')))
            ClearFilter.click()

            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="main"]/div/div[3]/div[1]/div[1]/div/div[1]/button/span'))).click()
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="main"]/div/div[3]/div[1]/div[1]/div/div[1]/ul/li[2]/div[2]/div[1]/div'))).click()
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="main"]/div/div[3]/div[1]/div[1]/div/div[1]/ul/li[16]/div[1]'))).click()
            Filter = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="main"]/div/div[3]/div[1]/div[1]/div/div[1]/ul/li[16]/div[2]/div/div/input')))
            Filter.click()
            Filter.send_keys("Virtual Server")
            Filter.send_keys(Keys.ENTER)
            driver.find_element_by_xpath(
                '//*[@id="main"]/div/div[3]/div[1]/div[1]/div/div[1]/ul/li[26]/div[1]').click()
            driver.find_element_by_xpath(
                '//*[@id="main"]/div/div[3]/div[1]/div[1]/div/div[1]/ul/li[26]/div[2]/div[2]/div').click()
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="main"]/div/div[3]/div[1]/div[1]/div/div[1]/div/div/div/span[1]'))).click()
            time.sleep(2)
            #ids = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[2]/div/div/div[3]/div[2]/div/span')))
            ids = driver.find_elements_by_xpath(
                '//*[@id="main"]/div/div[3]/div[2]/div/div[2]/div/div/div[3]/div[2]/div/span')
            print(ids)
            idx = 0
            while idx < len(ids):
                #print (ii.id)
                a = ids[idx]
                a.click()
                time.sleep(2)
                driver.execute_script("window.history.go(-1)")
                time.sleep(2)
                ids = driver.find_elements_by_xpath(
                    '//*[@id="main"]/div/div[3]/div[2]/div/div[2]/div/div/div[3]/div[2]/div/span')
                idx += 1
                # print (ii.get_attribute('id'))    # id name as string
        except TimeoutException:
            print("Loading took too much time!")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    # unittest.main()
    g = PythonOrgSearch()
    g.setUp()
    g.test_search_in_python_org()
    g.tearDown()
