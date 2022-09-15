from  selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\JoseDanilo\Python\chromedriver_win32\chromedriver.exe')
#Abrir Uniempresarial
driver.get('file:///C:\JoseDanilo\Python\danilito.html')
print("Pagina será refrescada")
#Pagina refrescada
driver.refresh();
print("Pagina es refrescada")