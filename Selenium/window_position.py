from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\JoseDanilo\Python\chromedriver_win32\chromedriver.exe')
driver.get('file:///C:\JoseDanilo\Python\danilito.html')
#establecer  posición de windows
driver.set_window_position(x=240,y=400);
print("Establecer posición browser")
