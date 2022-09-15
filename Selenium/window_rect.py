from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\JoseDanilo\Python\chromedriver_win32\chromedriver.exe')
driver.get('file:///C:\JoseDanilo\Python\danilito.html')
#establecer  posición de windows
driver.set_window_rect(x=30,y=30, width=450, height=500)
print("Establecer tamaño navegador con coordenadas")
