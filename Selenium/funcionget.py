from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\uestudiantes\Downloads\Selenium\Archivos\chromedriver_win32\chromedriver.exe')     
driver.get('https://www.uniempresarial.edu.co')
print("Browser Window opened")
