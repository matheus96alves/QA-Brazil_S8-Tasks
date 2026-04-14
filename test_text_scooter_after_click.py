import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage

def test_personal_scooter_option():
    driver = webdriver.Chrome()
    driver.get('https://cnt-d85b24d3-d325-4df2-8b49-516b9f24849a.containerhub.tripleten-services.com/?lng=pt')
    time.sleep(2)

    urban_routes_page = UrbanRoutesPage(driver)

    urban_routes_page.enter_from_location('East 2nd Street, 601')
    urban_routes_page.enter_to_location('1300 1st St')

    urban_routes_page.click_personal_option()
    time.sleep(2)

    urban_routes_page.click_scooter_icon()
    time.sleep(2)

    actual_value = urban_routes_page.get_scooter_text()
    expected_value = "Scooter"
    assert expected_value in actual_value, f"Esperado '{expected_value}', mas obtido '{actual_value}'"
    driver.quit()

test_personal_scooter_option()