import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def print_welcome():
    print("Kezdodhet a teszteles")


# Irj egy olyan fuggvenyt, ami raklikkel a beviteli mezore, click_to_name_input()
def click_to_name_input():
    driver.find_element(By.ID, 'create-form:name-input').click()

# Irj egy olyan fuggvenyt, mely a parameterkent kapott nevet, beirja a beviteli mezobe
def type_to_name_input(name):
    driver.find_element(By.ID, 'create-form:name-input').send_keys(name)

# Irj egy olyan fuggvenyt, mely raklikkel a cimsorra click_to_header()
def click_to_header():
    driver.find_element(By.XPATH, '//h1').click()

# Irj egy fuggvenyt, ami a parameterkent megadott hibauzenetre var
def wait_for_error_message(message):
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.XPATH, "//span[@class = 'invalid-feedback']"),
                                                          message))

    error_message = driver.find_element(By.XPATH, "//span[@class = 'invalid-feedback']").text
    print(error_message)

# Olvassa be a monogramot, es azzal terjen vissza read_monogram()
def wait_for_monogram(expected_monogram):
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "create-form:monogram-text"),
                                                          expected_monogram))

# Irj fuggvenyt, ami raklikekl a create employee gombra
def click_to_create_employee_button():
    driver.find_element(By.ID, 'create-form:save-button').click()

# Irj fuggvenyt, ami kitolti a kartyaszamot
def type_to_card_input_with_random_number(name):
    driver.find_element(By.ID, 'create-form:card-number-input').send_keys(name + str(time.time()))


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.learnwebservices.com/empapp/create-employee.xhtml")

print_welcome()
click_to_name_input()
#click_to_header()
#wait_for_error_message("Az alkalmazott nevét meg kell adni!")

type_to_name_input("John Doe X")
wait_for_monogram("JDX")
click_to_create_employee_button()
type_to_card_input_with_random_number("123456")
click_to_create_employee_button()



