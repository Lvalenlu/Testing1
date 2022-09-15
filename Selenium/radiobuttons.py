from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path=r'C:\JoseDanilo\Python\chromedriver_win32\chromedriver.exe')
driver.get('file:///C:\JoseDanilo\Python\danilito6.html')
caja = driver.find_element(By.NAME,'browser3').click();
