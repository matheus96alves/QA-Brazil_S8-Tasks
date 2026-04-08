import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://cnt-47f7831d-675d-4bc8-a0d7-257851f70b7d.containerhub.tripleten-services.com/?lng=pt")

# Faça o aplicativo aguardar 2 segundos para permitir que a página carregue
time.sleep(2)

driver.find_element(By.XPATH, "//button[@aria-pressed='false']").click()

time.sleep(2)

driver.quit()