from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

# Abra a página inicial do Urban Routes
driver.get('https://cnt-54f9e497-481f-431a-955b-46875f1b19b8.containerhub.tripleten-services.com/?lng=pt')

# Verifique se a URL contém tripleten-services.com
assert 'tripleten-services.com' in driver.current_url

# Feche o navegador
driver.quit()
