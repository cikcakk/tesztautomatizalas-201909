from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def delete_by_name(name):
    xpath = "//tr[td[contains(text(), 'name')]]/td[last()]/form/input[2]".replace("name", name)
    delete_button = driver.find_element(By.XPATH, xpath)
    delete_button.click()


def find_id_by_name(name):
    xpath = "//tr[td[contains(text(), 'name')]]/td[1]/a".replace("name", name)
    id = driver.find_element(By.XPATH, xpath).text
    print(id)
    return id

def wait_for_message():
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "alert-info"), "Employee has deleted"))



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.learnwebservices.com/empapp")

delete_by_name("John Doe X")
wait_for_message()
find_id_by_name("John Doe X")