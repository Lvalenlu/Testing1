from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path=r'C:\JoseDanilo\Python\chromedriver_win32\chromedriver.exe')
#Abrir Uniempresarial
driver.get('file:///C:\JoseDanilo\Python\danilito2.html')
email = driver.find_element(By.NAME,"email")
print("Email ", email)