from  selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\uestudiantes\Downloads\Selenium>')
#Abrir Uniempresarial
driver.get('file:///C:\JoseDanilo\Python\danilito.html')
#Abrir Google
driver.get('https://www.google.com')
driver.back();#Devolver pagina local o Uniempresarial
print("Mover a la primera página")
#Ir a la pagina actual
driver.forward()
print("Mover a la segunda página")