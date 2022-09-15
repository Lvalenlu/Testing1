from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\JoseDanilo\Python\chromedriver_win32\chromedriver.exe')
driver.get('file:///C:\JoseDanilo\Python\danilito.html')
#obtener tamaño ventana
tam_window = driver.get_window_size()
print(tam_window);
