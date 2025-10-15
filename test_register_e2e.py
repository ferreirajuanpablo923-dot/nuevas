from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# --- CONFIGURACIÓN DEL NAVEGADOR ---
options = Options()
options.add_argument("--headless")  # No abre ventana del navegador
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    print("🧪 Iniciando prueba de registro...")
    driver.get("http://127.0.0.1:5000/register")
    time.sleep(2)

    # --- DATOS DE PRUEBA ÚNICOS ---
    random_id = random.randint(1000, 9999)
    nombre = f"usuario_test_{random_id}"
    email = f"test{random_id}@example.com"
    password = "12345abc!"

    # --- COMPLETA EL FORMULARIO ---
    driver.find_element(By.NAME, "nombre").send_keys(nombre)
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)

    # ✅ Nuevo selector compatible con tu botón
    register_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Registrarse')]")
    register_button.click()

    print("📨 Formulario enviado.")
    time.sleep(3)

    # --- VALIDACIÓN ---
    html = driver.page_source
    if "Registro exitoso" in html or "Inicia sesión" in html or "Login" in html:
        print("✅ Prueba E2E EXITOSA: el registro funciona correctamente.")
    else:
        print("⚠️ El formulario se envió, pero no se encontró texto esperado.")
        print("HTML devuelto:")
        print(html[:500])

except Exception as e:
    print("❌ Error durante la prueba:", e)
finally:
    driver.quit()
    print("🧹 Navegador cerrado.")
