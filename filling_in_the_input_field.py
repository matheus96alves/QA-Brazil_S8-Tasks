import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://cnt-5d64ec07-c9c9-4d43-b9cf-c000b9285273.containerhub.tripleten-services.com/?lng=pt")

time.sleep(2)

# Preencha os campos
driver.find_element(By.ID, "from").send_keys("East 2nd Street, 601")
driver.find_element(By.ID, "to").send_keys("1300 1st St")

time.sleep(2)

# CORREÇÃO: Adicione .click() aqui!
driver.find_element(By.XPATH, "//button[@class='button round']").click()

# Aguarde o campo de comentário aparecer
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, "comment")))

# Escreva o comentário
driver.find_element(By.ID, "comment").send_keys("Quanto custa seu serviço?")

time.sleep(2)

# Verifique o comentário
assert driver.find_element(By.ID, "comment").get_attribute("value") == "Quanto custa seu serviço?"

driver.quit()
