from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path=r'C:\JoseDanilo\Python\chromedriver_win32\chromedriver.exe')
driver.get('file:///C:\JoseDanilo\Python\danilito5.html')
#encontrar campo de texto
listaSeleccionada = Select(driver.find_element(By.ID,'fruits'))
listaSeleccionada.select_by_index('4')
listaSeleccionada.select_by_value('cranberry')
#Valor a ser seleccionado
print(listaSeleccionada.select_by_index('4'));
print(listaSeleccionada.all_selected_options)