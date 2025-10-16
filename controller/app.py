from flask import Flask, request, jsonify, Response
import requests
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# 🔹 Métricas Prometheus
REQUEST_COUNT = Counter(
    'controller_requests_total',
    'Número total de solicitudes recibidas por el controller',
    ['method', 'endpoint']
)
REQUEST_LATENCY = Histogram(
    'controller_request_latency_seconds',
    'Latencia de las solicitudes del controller',
    ['endpoint']
)

@app.route('/')
def home():
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    return "Soy el Controller — coordinando servicios 🚀"

# 🔹 Endpoint principal: coordina validator → core
@app.route('/validar', methods=['POST'])
def validar():
    REQUEST_COUNT.labels(method='POST', endpoint='/validar').inc()

    data = request.get_json()
    password = data.get("password")

    with REQUEST_LATENCY.labels(endpoint='/validar').time():
        try:
            # Llamar al microservicio validator
            validator_resp = requests.post("http://validator:5000/validate", json={"password": password}, timeout=5)
            validator_data = validator_resp.json()

            # Si es válida, llamar al core
            if validator_data.get("valido"):
                core_resp = requests.post("http://microservicio-core:5000/procesar", json={"password": password}, timeout=5)
                core_data = core_resp.json()
            else:
                core_data = {"procesado": False, "motivo": "Contraseña inválida"}

            return jsonify({
                "validator": validator_data,
                "core": core_data
            })

        except Exception as e:
            return jsonify({"error": str(e)}), 500

# 🔹 Endpoint de métricas Prometheus
@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

# 🔹 Punto de entrada
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
