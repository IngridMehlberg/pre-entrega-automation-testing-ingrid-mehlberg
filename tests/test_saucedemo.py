from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver_setup import setup_driver

def test_login_exitoso():
    """
    Caso de prueba 1: Validar el inicio de sesión exitoso en SauceDemo.
    Asegura la navegación, el ingreso de credenciales válidas,
    la espera explícita del inventario y la aserción de URL y títulos.
    """
    driver = setup_driver()
    
    try:
        # 1. Navegar a la página de login
        driver.get("https://www.saucedemo.com/")

        # 2. Espera explícita para asegurar que el formulario cargue correctamente
        wait = WebDriverWait(driver, 10)
        username_input = wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )

        # 3. Ingresar credenciales válidas
        username_input.clear()
        username_input.send_keys("standard_user")

        password_input = driver.find_element(By.ID, "password")
        password_input.clear()
        password_input.send_keys("secret_sauce")

        # 4. Hacer clic en el botón de login
        driver.find_element(By.ID, "login-button").click()

        # 5. Espera explícita para la carga del catálogo/inventario
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
        )

        # 6. Validaciones (Aserciones)
        # a) Redirección a la URL de inventario
        assert "/inventory.html" in driver.current_url, (
            f"Se esperaba '/inventory.html' en la URL, pero es: {driver.current_url}"
        )

        # b) Título de la pestaña del navegador ("Swag Labs")
        assert driver.title == "Swag Labs", (
            f"Se esperaba 'Swag Labs' en el título de la pestaña, pero se obtuvo: {driver.title}"
        )

        # c) Título de la sección de productos ("Products")
        titulo_seccion = driver.find_element(By.CLASS_NAME, "title").text
        assert titulo_seccion == "Products", (
            f"Se esperaba 'Products' como título de sección, pero se obtuvo: {titulo_seccion}"
        )

    finally:
        # Cierre seguro de la sesión del navegador
        driver.quit()

def test_navegacion_y_catalogo():
    """
    Caso de prueba 2: Navegación y verificación del catálogo de productos.
    Valida el título de la sección, presencia de productos, lista nombre y precio
    del primer producto, y verifica la presencia de menú y filtros.
    """
    driver = setup_driver()

    try:
        # 1. Navegación e inicio de sesión
        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 10)

        user_input = wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        user_input.send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # 2. Esperar carga del catálogo
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
        )

        # 3. Validar título de sección ("Products")
        titulo = driver.find_element(
            By.CSS_SELECTOR, "div.header_secondary_container .title"
        ).text
        assert titulo == "Products", f"Se esperaba 'Products', pero se obtuvo: {titulo}"

        # 4. Validar presencia de productos visibles
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) > 0, "No se encontraron productos en el inventario."

        # 5. Listar en consola nombre y precio del primer producto
        primer_producto = productos[0]
        nombre = primer_producto.find_element(
            By.CLASS_NAME, "inventory_item_name"
        ).text
        precio = primer_producto.find_element(
            By.CLASS_NAME, "inventory_item_price"
        ).text
        print(f"\nPrimer producto: {nombre} | Precio: {precio}")

        # 6. Validar presencia de elementos de interfaz (menú y filtros)
        driver.find_element(By.ID, "react-burger-menu-btn")
        driver.find_element(By.CLASS_NAME, "product_sort_container")

    finally:
        driver.quit()

def test_carrito_de_compras():
    """
    Caso de prueba 3: Interacción con productos y carrito de compras.
    Añade el primer producto, valida el incremento del contador a 1
    mediante espera explícita, navega al carrito y comprueba que el
    ítem figure en la lista.
    """
    driver = setup_driver()

    try:
        # 1. Navegación e inicio de sesión independiente
        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 10)

        user_input = wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        user_input.send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # 2. Esperar carga del catálogo
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
        )

        # 3. Añadir el primer producto al carrito
        driver.find_element(
            By.XPATH, "//button[contains(@data-test, 'add-to-cart')]"
        ).click()

        # 4. Esperar explícitamente y verificar que el badge muestre '1'
        badge = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        assert badge.text == "1", (
            f"El contador del carrito debería mostrar 1, pero muestra: {badge.text}"
        )

        # 5. Navegar al carrito de compras
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # 6. Comprobar que el producto añadido figure en el carrito
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
        )
        assert "/cart.html" in driver.current_url, (
            f"Se esperaba '/cart.html' en la URL, pero es: {driver.current_url}"
        )

    finally:
        driver.quit()