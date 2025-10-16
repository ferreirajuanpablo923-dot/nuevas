from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUESTS = Counter('validador_requests_total', 'Total de requests en validador', ['endpoint'])

@app.route('/')
def home():
    REQUESTS.labels(endpoint='/').inc()
    return "Hola desde validador"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
