from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:\Users\uestudiantes\Downloads\Selenium>')
driver.get('https://www.eltiempo.com/')
print("Browser Window opened")

driver.quit()
print("Mover a la primera página")