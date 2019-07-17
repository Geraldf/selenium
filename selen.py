import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time



class PythonOrgSearch():

    def setUp(self):
        self.driver = webdriver.Firefox()
        self. delay = 10 # seconds

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://mykarlstorz-smartit.onbmc.com/smartit/app/#/ticket-console")
        try:
            myElem = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/h3')))
            ## clear the filter
            ClearFilter = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div[1]/div/div[3]/button[1]')))
            ClearFilter.click()
           
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div[1]/div/div[1]/button/span'))).click()
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div[1]/div/div[1]/ul/li[2]/div[2]/div[1]/div'))).click()
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div[1]/div/div[1]/ul/li[16]/div[1]'))).click()
            Filter = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div[1]/div/div[1]/ul/li[16]/div[2]/div/div/input')))
            Filter.click()
            Filter.send_keys("Virtual Server")
            Filter.send_keys(Keys.ENTER)
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div[1]/div/div[1]/div/div/div/span[1]'))).click()
            time.sleep(10)
            #ids = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[2]/div/div/div[3]/div[2]/div/span')))
            ids = driver.find_elements_by_xpath( '//*[@id="main"]/div/div[3]/div[2]/div/div[2]/div/div/div[3]/div[2]/div/span')
            print (ids)
            for ii in ids:
                print (ii.id)

                ii.click()
                driver.execute_script("window.history.go(-1)")
                # print (ii.get_attribute('id'))    # id name as string
        except TimeoutException:
            print ("Loading took too much time!")
        


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    # unittest.main()
    g = PythonOrgSearch()
    g.setUp()
    g.test_search_in_python_org()
    g.tearDown()