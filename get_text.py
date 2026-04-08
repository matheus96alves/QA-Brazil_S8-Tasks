import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://cnt-67970319-c8fd-46e5-a1f4-bc14ca49fb4c.containerhub.tripleten-services.com/?lng=pt")

# Pause a execução por 2 segundos para permitir que a página carregue por completo
time.sleep(2)

# Encontre o campo DE e o preencha
driver.find_element(By.ID, "from").send_keys("East 2nd Street, 601")

# Encontre o campo PARA e o preencha
driver.find_element(By.ID, "to").send_keys("1300 1st St")

time.sleep(2)

# Obtenha o texto do modo "Fastest"
mode = driver.find_element(By.XPATH, "//div[@class='mode active']").text

time.sleep(2)

# Faça um assert para verificar se o texto da variável mode é "Fastest"
print(f"Texto capturado: '{mode}'")
assert mode == "Flash"

driver.quit()
