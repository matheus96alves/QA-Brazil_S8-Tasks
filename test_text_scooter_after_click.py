import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage

def test_personal_scooter_option():

    driver = webdriver.Chrome()
    driver.get('https://cnt-fb26ecd4-5d4d-4416-89f2-36a452b2d760.containerhub.tripleten-services.com/?lng=pt')
    time.sleep(5)
    # Crie uma instância da classe de página
    urban_routes_page = UrbanRoutesPage(driver)

    # Etapa 3: use métodos POM para executar ações na página
    # Insira os locais "De" e "Para".
    urban_routes_page.enter_from_location('East 2nd Street, 601')
    urban_routes_page.enter_to_location('1300 1st St')

    # Selecione a opção "Personal".
    urban_routes_page.click_personal_option()
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Clique no ícone "Scooter".
    urban_routes_page.click_scooter_icon()
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 4: Verifique se o texto Scooter é exibido corretamente
    actual_value = urban_routes_page.get_scooter_text()
    expected_value = "Scooter"
    assert expected_value in actual_value, f"Esperado '{expected_value}', mas obtido '{actual_value}'"
    driver.quit()

if __name__ == "__main__":
    test_personal_scooter_option()