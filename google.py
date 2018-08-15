from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
driver.get("http://www.google.com")
elem = driver.find_element_by_name("q")
elem.send_keys("selenium webdriver")
elem.submit()
time.sleep(5)
elem = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/div/h3/a')
elem.click()
