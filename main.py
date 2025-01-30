from flask import Flask, request
from extenso import extenso
app = Flask(__name__)

#  url para teste: http://127.0.0.1:5000/extenso?numero=23461

# Rota de exemplo
@app.route('/extenso', methods=['GET'])
def extenso_controller():
    dados = request.args.get('numero', type=int)
    # print(dados)
    resultado = extenso(dados)
    return resultado



if __name__ == '__main__':
    app.run(debug=True)
