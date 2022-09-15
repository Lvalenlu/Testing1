from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:\JoseDanilo\Python\chromedriver_win32\chromedriver.exe')
driver.get('file:///C:\JoseDanilo\Python\danilito4.html')
#encontrar campo de texto
campo_texto = driver.find_element(By.ID,'docente');
#Valor a ser insertado
campo_texto.send_keys("Luciana Sanz")
#insertar valor
campo_texto.submit()