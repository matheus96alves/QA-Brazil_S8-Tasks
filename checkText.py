from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
# Substitua nosso link pelo link do seu próprio servidor aqui
driver.get("https://cnt-5d64ec07-c9c9-4d43-b9cf-c000b9285273.containerhub.tripleten-services.com/?lng=pt")

time.sleep(2)

# Obtém o texto do elemento
disclaimer = driver.find_element(By.CLASS_NAME, "logo-disclaimer").text

# Faça um assert para verificar se o texto da variável disclaimer é "PLATFORM"
assert disclaimer == "PLATFORM"
print(disclaimer)
driver.quit()