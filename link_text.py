import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r"C:\Users\navee\Downloads\chromedriver_win32\chromedriver.exe")
driver.get(r"https://www.flipkart.com/account/login?ret=%2Faccount%2Forders%3Flink%3Dhome_orders&fromMyOrdersPage=true")

driver.find_element(By.XPATH,"//*[@class='_2IX_2- VJZDxU']").send_keys(8919136400)
time.sleep(5)
driver.find_element(By.XPATH,"//*[@class='_2IX_2- _3mctLh VJZDxU']").send_keys("Chintha@23")
time.sleep(10)
driver.find_element(By.XPATH,"//*[@class='_2KpZ6l _2HKlqd _3AWRsL']").click()
time.sleep(15)
driver.find_element(By.LINK_TEXT,"Baby & Kids").click()
time.sleep(25)
driver.close()
