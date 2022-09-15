from selenium import webdriver
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path=r'C:\JoseDanilo\Python\chromedriver_win32\chromedriver.exe')
#Abrir Facebook
driver.get('https://www.facebook.com/')
print("Pagina será refrescada")
#Ir al botón Iniciar Sesión
elemento_web = driver.find_element(By.NAME, "login")
#Presionar click sobre el elemento
elemento_web.click();
print("Elemento presionado")