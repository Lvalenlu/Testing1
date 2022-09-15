from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:\Users\uestudiantes\Downloads\Selenium\Archivos\chromedriver_win32\chromedriver.exe')
#Abrir Outlook
driver.get('https://www.uniempresarial.edu.co/')
#Ir al botón Iniciar Sesión
elemento_web = driver.find_elements(By.CSS_SELECTOR, 'a')
print(elemento_web)