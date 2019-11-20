from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/empapp/employees.xhtml")

# xpath = "//tr[td[a[text() = 'id']]]/td[last()]/form/input[2]".replace("id", "c121985d-728c-4c76-bd53-dd2457fa6c54")
id = "dfe6ecf0-de7e-4657-b105-996eab3df302"
xpath = "//tr[td[a[text() = '" + id + "']]]/td[last()]/form/input[2]"
print(xpath)
delete_button = driver.find_element(By.XPATH, xpath)
print(delete_button)
delete_button.click()
