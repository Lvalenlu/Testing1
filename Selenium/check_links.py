from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:\JoseDanilo\Python\chromedriver_win32\chromedriver.exe')
#Abrir Outlook
driver.get('https://www.uniempresarial.edu.co/')
#Ir al botón Iniciar Sesión
elementos_web = driver.find_elements(By.CSS_SELECTOR, 'a')
print(elementos_web)