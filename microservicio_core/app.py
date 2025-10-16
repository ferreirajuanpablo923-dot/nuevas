from flask import Flask, request, jsonify, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# --- MÉTRICAS ---
REQUESTS = Counter(
    'microservicio_core_requests_total',
    'Número total de solicitudes procesadas en el core'
)

# --- ENDPOINT PRINCIPAL ---
@app.route('/procesar', methods=['POST'])
def procesar():
    REQUESTS.inc()  # incrementa contador de métricas
    data = request.get_json()
    password = data.get("password", "")

    longitud = len(password)
    return jsonify({
        "procesado": True,
        "longitud": longitud
    })

# --- ENDPOINT DE SALUD ---
@app.route('/')
def home():
    return "Microservicio Core operativo"

# --- ENDPOINT DE MÉTRICAS PARA PROMETHEUS ---
@app.route('/metrics')
def metrics():
    # 🔥 Este es el endpoint que Prometheus busca
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
