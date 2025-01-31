from flask import Flask, jsonify, request
from extenso import extenso
app = Flask(__name__)

#  url para teste: http://127.0.0.1:5000/extenso?numero=23461

# Rota básica para testar
@app.route('/')
def home():
    return jsonify({"mensagem": "API funcionando na Vercel!"})

# Rota de exemplo
@app.route('/extenso', methods=['GET'])
def extenso_controller():
    dados = request.args.get('numero', type=int)
    # print(dados)
    if dados == None:
        resultado = jsonify({"erro": f"Número igual a {dados}, não é possível processar número"}), 400
    else:
        resultado = extenso(dados)
    return resultado



if __name__ == '__main__':
    app.run(debug=True)
