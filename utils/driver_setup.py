from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def setup_driver():
    """
    Configura e inicializa una instancia de Chrome WebDriver con opciones recomendadas.
    """
    chrome_options = Options()

    # Opciones de estabilidad y visualización
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Inicialización del driver de Chrome
    driver = webdriver.Chrome(options=chrome_options)

    return driver