"""
2022 (c) Havaii
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def test_smoke():
    """
    SMK-1. Smoke test
    """

    	# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения

    # устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service(ChromeDriverManager().install())

    # запускаем браузер с указанными выше настройками
    browser = webdriver.Chrome(service=service, options=chrome_options)
    # browser = webdriver.Chrome()

    browser.get("https://test.qa.studio/")

    # driver.quit()

    assert True, ""



