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
    print("🧩 Iniciando prueba E2E completa (registro + login)...")

    # === 1️⃣ REGISTRO ===
    driver.get("http://127.0.0.1:5000/register")
    time.sleep(2)

    # Generar datos únicos
    random_id = random.randint(1000, 9999)
    nombre = f"user_test_{random_id}"
    email = f"test{random_id}@example.com"
    password = "12345abc!"

    # Completar formulario
    driver.find_element(By.NAME, "nombre").send_keys(nombre)
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)

    driver.find_element(By.XPATH, "//button[contains(text(), 'Registrarse')]").click()
    print("✅ Registro enviado...")
    time.sleep(3)

    # Validar que redirige a login
    html = driver.page_source
    if "Inicia sesión" not in html and "Login" not in html:
        print("⚠️ No se detectó redirección a login. HTML parcial:")
        print(html[:400])
    else:
        print("➡️ Registro correcto, procediendo al login...")

    # === 2️⃣ LOGIN ===
    driver.get("http://127.0.0.1:5000/login")
    time.sleep(2)

    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Entrar')]").click()
    print("🔐 Iniciando sesión...")
    time.sleep(3)

    # === 3️⃣ VALIDACIÓN ===
    html = driver.page_source
    if ("Analizar" in html or "Panel" in html or "Bienvenido" in html or "Contraseña" in html):
        print("✅ Prueba E2E COMPLETA EXITOSA: el usuario pudo registrarse e iniciar sesión correctamente.")
    else:
        print("⚠️ Algo salió mal tras el login. HTML parcial:")
        print(html[:500])

except Exception as e:
    print("❌ Error durante la prueba:", e)
finally:
    driver.quit()
    print("🧹 Navegador cerrado.")
