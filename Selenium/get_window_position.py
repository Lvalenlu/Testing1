from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\uestudiantes\Downloads\Selenium\Archivos\chromedriver_win32\chromedriver.exe');
driver.get('file:///C:\JoseDanilo\Python\danilito.html')
#obtener posicion de windows
posicion_window = driver.get_window_position();
print(posicion_window);
