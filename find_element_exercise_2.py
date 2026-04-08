import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Abra uma nova instância do Chrome WebDriver
driver = webdriver.Chrome()

# Abra a URL especificada no navegador
driver.get("https://cnt-9bb93889-4343-4b05-b88d-e19340b1ade5.containerhub.tripleten-services.com/?lng=pt")

# Pause a execução por 2 segundos para permitir que a página carregue por completo
time.sleep(2)

# Encontre todos os elementos na página usando um seletor de XPath
elements = driver.find_elements(By.XPATH, "//div[@class='dst-picker-marker']")

# Verifique se o número de elementos encontrados é maior que 1 usando len()
assert len(elements) > 1

# Feche o navegador e encerre a sessão do WebDriver
driver.quit()

