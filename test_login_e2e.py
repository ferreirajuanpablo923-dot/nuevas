from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- CONFIGURACIÓN DEL NAVEGADOR ---
options = Options()
options.add_argument("--headless")  # No abre ventana del navegador
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    print("🔍 Abriendo la aplicación Flask...")
    driver.get("http://127.0.0.1:5000/login")  # ruta de tu formulario
    time.sleep(2)

    # --- INTERACCIÓN CON TU FORMULARIO ---
    email_input = driver.find_element(By.NAME, "email")
    password_input = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Entrar')]")

    # Ingresa datos de prueba
    email_input.send_keys("admin@example.com")   # cambia por un usuario válido de tu BD
    password_input.send_keys("12345")            # contraseña válida
    login_button.click()

    print("➡️  Enviando formulario...")
    time.sleep(3)

    # --- VALIDACIÓN ---
    html = driver.page_source
    if "Bienvenido" in html or "Inicio exitoso" in html or "Panel" in html:
        print("✅ Prueba E2E EXITOSA: el login funciona correctamente.")
    else:
        print("⚠️ El formulario se envió, pero no se encontró texto esperado.")
        print("🔍 Parte del HTML devuelto:")
        print(html[:500])  # muestra parte del HTML recibido
except Exception as e:
    print("❌ Error durante la prueba:", e)
finally:
    driver.quit()
    print("🧹 Navegador cerrado.")
