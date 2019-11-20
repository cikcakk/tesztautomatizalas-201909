from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/empapp/create-employee.xhtml")

driver.find_element(By.ID, 'create-form:name-input').click()
driver.find_element(By.XPATH, '//h1').click()

error_message = driver.find_element(By.XPATH, "//span[@class = 'invalid-feedback']").text
print(error_message)