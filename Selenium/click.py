from selenium import webdriver
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path=r'C:\JoseDanilo\Python\chromedriver_win32\chromedriver.exe')
#Abrir Facebook
driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1663215125&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3deb3197cd-cf8d-5827-72b4-546f9bd7bdcf&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')
#Ir al botón Iniciar Sesión
elemento_web = driver.find_element(By.ID, "idSIButton9");
#Presionar click sobre el elemento
elemento_web.click();
print("Elemento presionado")