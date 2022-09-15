from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:\JoseDanilo\Python\chromedriver_win32\chromedriver.exe')
driver.get('file:///C:\JoseDanilo\Python\danilito3.html')
#establecer  posición de windows
check_button = driver.find_element(By.ID,'chrome');

if(check_button.get_attribute("type") == "checkbox"):
    print("Es un campo checkbox")
else:
    print("No es un campo checkbox")

print("Presionar vínculo llamado chrome")
