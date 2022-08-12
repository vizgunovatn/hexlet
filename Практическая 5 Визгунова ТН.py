import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

s=Service('C:/Users/arzha/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://qa.neapro.site/login")
driver.set_window_size(1920, 1080)

driver.find_element(By.XPATH, "//*[@id='__layout']/div/section/div[2]/div/div/div/form/div[1]/div[1]/div/input").send_keys("arzhancevataya@mail.ru")
driver.find_element(By.XPATH, "//*[@id='__layout']/div/section/div[2]/div/div/div/form/div[1]/div[2]/div/input").send_keys("VizgunovaTPO818")
driver.find_element(By.XPATH, "//*[@id='__layout']/div/section/div[2]/div/div/div/form/div[2]/button").click()
time.sleep(5)

driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[3]/div/div/div[2]/div[2]/div[1]").click()

driver.find_element(By.ID, "surname").send_keys("Фамилия")
driver.find_element(By.ID, "name").send_keys("Имя")
driver.find_element(By.ID, "patronymic").send_keys("Отчество")

driver.find_element(By.NAME, "date").send_keys("12.08.1991")

driver.find_element(By.ID, "passportSeries").click()

driver.find_element(By.ID, "passportSeries").send_keys(Keys.LEFT)
driver.find_element(By.ID, "passportSeries").send_keys(Keys.LEFT)
driver.find_element(By.ID, "passportSeries").send_keys(Keys.LEFT)
driver.find_element(By.ID, "passportSeries").send_keys(Keys.LEFT)
driver.find_element(By.ID, "passportSeries").send_keys(Keys.LEFT)
driver.find_element(By.ID, "passportSeries").send_keys("1111")
time.sleep(1)

driver.find_element(By.ID, "passportNumber").send_keys(Keys.LEFT)
driver.find_element(By.ID, "passportNumber").send_keys(Keys.LEFT)
driver.find_element(By.ID, "passportNumber").send_keys(Keys.LEFT)
driver.find_element(By.ID, "passportNumber").send_keys(Keys.LEFT)
driver.find_element(By.ID, "passportNumber").send_keys(Keys.LEFT)
driver.find_element(By.ID, "passportNumber").send_keys(Keys.LEFT)
driver.find_element(By.ID, "passportNumber").send_keys(Keys.LEFT)
driver.find_element(By.ID, "passportNumber").send_keys("111111")
time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='dateOfIssue']/div/input").send_keys("12.08.2004")

driver.find_element(By.ID, "code").send_keys(Keys.LEFT)
driver.find_element(By.ID, "code").send_keys(Keys.LEFT)
driver.find_element(By.ID, "code").send_keys(Keys.LEFT)
driver.find_element(By.ID, "code").send_keys(Keys.LEFT)
driver.find_element(By.ID, "code").send_keys(Keys.LEFT)
driver.find_element(By.ID, "code").send_keys(Keys.LEFT)
driver.find_element(By.ID, "code").send_keys(Keys.LEFT)
driver.find_element(By.ID, "code").send_keys("111111")
time.sleep(1)

driver.find_element(By.ID, "cardId").send_keys(Keys.LEFT)
driver.find_element(By.ID, "cardId").send_keys(Keys.LEFT)
driver.find_element(By.ID, "cardId").send_keys(Keys.LEFT)
driver.find_element(By.ID, "cardId").send_keys(Keys.LEFT)
driver.find_element(By.ID, "cardId").send_keys(Keys.LEFT)
driver.find_element(By.ID, "cardId").send_keys(Keys.LEFT)
driver.find_element(By.ID, "cardId").send_keys(Keys.LEFT)
driver.find_element(By.ID, "cardId").send_keys(Keys.LEFT)
driver.find_element(By.ID, "cardId").send_keys(Keys.LEFT)
driver.find_element(By.ID, "cardId").send_keys(Keys.LEFT)
driver.find_element(By.ID, "cardId").send_keys(Keys.LEFT)
driver.find_element(By.ID, "cardId").send_keys(Keys.LEFT)
driver.find_element(By.ID, "cardId").send_keys(Keys.LEFT)
driver.find_element(By.ID, "cardId").send_keys(Keys.LEFT)
driver.find_element(By.ID, "cardId").send_keys("11111111111")
time.sleep(1)

driver.find_element(By.ID, "issued").send_keys("Кем выдан")

driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys("г Москва")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.ARROW_DOWN)
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.ENTER)
time.sleep(1)

driver.find_element(By.ID, "phone").send_keys(Keys.LEFT)
driver.find_element(By.ID, "phone").send_keys(Keys.LEFT)
driver.find_element(By.ID, "phone").send_keys(Keys.LEFT)
driver.find_element(By.ID, "phone").send_keys(Keys.LEFT)
driver.find_element(By.ID, "phone").send_keys(Keys.LEFT)
driver.find_element(By.ID, "phone").send_keys(Keys.LEFT)
driver.find_element(By.ID, "phone").send_keys(Keys.LEFT)
driver.find_element(By.ID, "phone").send_keys(Keys.LEFT)
driver.find_element(By.ID, "phone").send_keys(Keys.LEFT)
driver.find_element(By.ID, "phone").send_keys(Keys.LEFT)
driver.find_element(By.ID, "phone").send_keys(Keys.LEFT)
driver.find_element(By.ID, "phone").send_keys(Keys.LEFT)
driver.find_element(By.ID, "phone").send_keys(Keys.LEFT)
driver.find_element(By.ID, "phone").send_keys("1111111111")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".upload-widget > input").send_keys("C://Users//arzha//Desktop//kotik.jpg")





