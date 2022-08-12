import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s=Service('C:/Users/arzha/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://qa.neapro.site/login")
driver.set_window_size(1024, 600)
driver.minimize_window()

driver.find_element(By.XPATH, "//*[@id='__layout']/div/section/div[2]/div/div/div/form/div[1]/div[1]/div/input").send_keys("arzhancevataya@mail.ru")
driver.find_element(By.XPATH, "//*[@id='__layout']/div/section/div[2]/div/div/div/form/div[1]/div[2]/div/input").send_keys("VizgunovaTPO818")
driver.find_element(By.XPATH, "//*[@id='__layout']/div/section/div[2]/div/div/div/form/div[2]/button").click()
time.sleep(10)

driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[3]/div/div/div[2]/div[2]/div[1]").click()

driver.find_element(By.ID, "surname").clear()
driver.find_element(By.ID, "surname").send_keys("Фамилия")
driver.find_element(By.ID, "name").clear()
driver.find_element(By.ID, "name").send_keys("Имя")
driver.find_element(By.ID, "patronymic").clear()
driver.find_element(By.ID, "patronymic").send_keys("Отчество")




