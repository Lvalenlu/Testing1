from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\uestudiantes\Downloads\Selenium\Archivos\chromedriver_win32\chromedriver.exe')
driver.get('file:///C:\JoseDanilo\Python\danilito.html')
#establecer  posición de windows
driver.fullscreen_window();
print("Establecer FullScreen")
 