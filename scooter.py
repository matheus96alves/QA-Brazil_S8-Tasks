from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def test_personal_scooter():

    driver = webdriver.Chrome()


    driver.get('https://cnt-3c4ea560-57a7-4ec1-ac2a-b6bb85233cd5.containerhub.tripleten-services.com/?lng=pt')


    driver.find_element(By.ID, 'from').send_keys('East 2nd Street, 601')


    driver.find_element(By.ID, 'to').send_keys('1300 1st St')


    driver.find_element(By.XPATH, '//div[text()="Personal"]').click()
    time.sleep(2)


    driver.find_element(By.XPATH, '//img[@src="/static/media/scooter.cf9bb57e.svg"]').click()
    time.sleep(2)


    actual_value = driver.find_element(By.XPATH, '//div[contains(text(),"Scooter")]').text
    expected_value = "Scooter"
    assert expected_value in actual_value, f"Esperado {expected_value}, mas obtido {actual_value}"

    time.sleep(2)

    driver.quit()