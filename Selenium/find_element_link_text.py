from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:\JoseDanilo\Python\chromedriver_win32\chromedriver.exe')
#Abrir Outlook
driver.get('https://www.uniempresarial.edu.co/')
elemento_web = driver.find_element(By.LINK_TEXT, 'QUIENES SOMOS')
print(elemento_web);
print("Elemento presionado")