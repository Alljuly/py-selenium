from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from backend.scripts import (
    login_and_get_cookies,
    open_navigator_with_cookies,
    query_list_items_service,
    update_term,
    create_transference_by_group
)
from backend.settings import (
    URL_INCORPORATION,
    URL_TERM_RESPONSABILITY,
    URL_TRANSFERENCE_MODULE
)
from flask import Flask, request, jsonify
from functools import wraps
from flask_cors import CORS
import json

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": ['http://localhost:5173', 'https://ejade-automacao.vercel.app']}})

@app.after_request
def apply_cors_headers(response):
    origin = request.headers.get("Origin")
    if origin in ['http://localhost:5173', 'https://ejade-automacao.vercel.app']:
        response.headers["Access-Control-Allow-Origin"] = origin
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
    return response

def handle_exceptions(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print(f"Erro em {f.__name__}: {str(e)}")
            return jsonify({
                "error": "Erro interno no servidor",
                "details": str(e)
            }), 500
    return decorated_function

@app.route("/", methods=["GET"])
@handle_exceptions
def home():
    return jsonify({"message": "API está funcionando!"})

@app.route('/get_items', methods=['POST'])
@handle_exceptions
def get_items():
    data = request.get_json()
    plaquetas = data.get('plaquetas')

    with open('cookies.json', 'r', encoding='utf-8') as f:
        cookies = json.load(f)

    navigator = open_navigator_with_cookies(cookies)
    navigator.get(URL_INCORPORATION)
    wait = WebDriverWait(navigator, 30)
    wait.until(EC.url_matches(URL_INCORPORATION))
    res = query_list_items_service(navigator, plaquetas)

    navigator.quit()
    return jsonify(res), 200

@app.route('/include_terms_items', methods=['POST'])
@handle_exceptions
def include_terms_items():
    data = request.get_json()
    plaquetas = data.get('plaquetas')
    num_termo = data.get('num_termo')

    with open('cookies.json', 'r', encoding='utf-8') as f:
        cookies = json.load(f)

    navigator = open_navigator_with_cookies(cookies)
    navigator.get(URL_TERM_RESPONSABILITY)
    wait = WebDriverWait(navigator, 30)
    wait.until(EC.url_matches(URL_TERM_RESPONSABILITY))

    update_term(navigator, plaquetas, num_termo)
    navigator.quit()
    return jsonify({"message": "Termo incluído com sucesso"}), 200

@app.route('/create_transference_and_update', methods=['POST'])
@handle_exceptions
def create_transference_and_update():
    data = request.get_json()

    destination = data.get('destination')
    plaquetas = data.get('plaquetas')

    with open('cookies.json', 'r', encoding='utf-8') as f:
        cookies = json.load(f)

    navigator = open_navigator_with_cookies(cookies)
    navigator.get(URL_TRANSFERENCE_MODULE)
    wait = WebDriverWait(navigator, 30)
    wait.until(EC.url_matches(URL_TRANSFERENCE_MODULE))

    data_list = create_transference_by_group(navigator, destination, plaquetas)
    if data_list is not None:
        return jsonify({'message': 'Transferências criadas com sucesso'})
    navigator.quit()

    return jsonify(data_list)

@app.route("/login", methods=["POST"])
@handle_exceptions
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Dados incompletos!"}), 400

    cookies = login_and_get_cookies(username, password)
    if cookies is None:
        return jsonify({"message": "Credenciais inválidas!"}), 401

    save_cookies_to_file(cookies)
    return jsonify({"message": "Login realizado com sucesso!"})

def save_cookies_to_file(cookies, filename="cookies.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(cookies, f, indent=4, ensure_ascii=False)
