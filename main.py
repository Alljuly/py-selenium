from selenium.webdriver.support.ui import WebDriverWait
from automacao.actions import *
from automacao.actions.movement import *
from automacao.settings import URL_INCORPORATION, URL_TERM_RESPONSABILITY
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)

CORS(app)

from functools import wraps
from flask import jsonify

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
    print('indo ate', URL_INCORPORATION)
    wait = WebDriverWait(navigator, 30)
    wait.until(EC.url_matches(URL_INCORPORATION))
    res = query_list_items_service(navigator, plaquetas)    

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
    print('indo ate', URL_TERM_RESPONSABILITY)
    wait = WebDriverWait(navigator, 30)
    wait.until(EC.url_matches(URL_TERM_RESPONSABILITY))

    update_term(navigator, plaquetas, num_termo)



@app.route('/create_transference_and_update', methods=['POST'])
@handle_exceptions
def create_transference_and_update():
    data = request.get_json()
    print(f'data = request.get_json() {data}')
    destination = data.get('destination')
    plaquetas = data.get('plaquetas')


    with open('cookies.json', 'r', encoding='utf-8') as f:
        cookies = json.load(f)
    navigator = open_navigator_with_cookies(cookies)
    navigator.get(URL_TRANSFERENCE_MODULE)
    print('indo ate', URL_TRANSFERENCE_MODULE)
    wait = WebDriverWait(navigator, 30)
    wait.until(EC.url_matches(URL_TRANSFERENCE_MODULE))
    data_list = create_transference_by_group(navigator, destination, plaquetas)
    if data_list is not None:
        return jsonify({'message': 'Transferencias criadas'})  
    return jsonify(data_list)


@app.route("/login", methods=["POST"])
@handle_exceptions
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if not username or not password:
        return jsonify({"error": "Dados incompletos!"}), 400
    
    cookies = login_and_get_cookies(username, password)
    if cookies is not None:
        return jsonify({"message": "Credenciais inválidas!"}), 401
    save_cookies_to_file(cookies)
    return jsonify({"message": "Login realizado com sucesso!"})



def save_cookies_to_file(cookies, filename="cookies.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(cookies, f, indent=4, ensure_ascii=False)

# @app.get('/item/<patplaqueta>')
# def get_items():
#     #chamar a função aqui
#     pass

# def main():
#     cookies = login_and_get_cookies()

#     navigator = open_navigator_with_cookies(cookies)

#     wait = WebDriverWait(navigator, 30)


#     event = 0
#     match event:

#         case 1: 

#             wait.until(EC.url_matches(URL_INCORPORATION))
      
#             csv_res = query_random_list_items(navigator, CSV_PATH)
#             print(csv_res)
#         case 2:
#             navigator.get(URL_INCORPORATION)
#             wait.until(EC.url_matches(URL_INCORPORATION))
      
#             list_items_path = query_random_list_items(navigator, CSV_PATH) 
#             #list_items_path = "resultado_consulta_2025-04-07_13-19-59.csv"
#             #list_items_path = "resultado_consulta_2025-04-07_13-50-57.csv"
#             print(list_items_path)
#             destination = '1324'
#             if list_items_path:
#                 navigator.get(URL_TRANSFERENCE_MODULE)
#                 list_items = create_transference_by_group(navigator, destination, list_items_path)  
          
#                 navigator.get('https://arapiraca.abaco.com.br/ejade/servlet/wmtermoresponsabilidade')
          
#                 update_term(navigator, list_items, '29331')

#     input("enter para fechar \n")

# main()
