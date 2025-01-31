import requests
import pandas as pd

# Lista de números para testar
numeros_para_testar = [
    0, 1, 10, 11, 19, 20, 21, 30, 35, 40, 50, 60, 70, 80, 90, 99, 100, 101, 150, 199, 200, 250, 
    300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 999, 1000, 1001, 1100,
    1200, 1500, 1999, 2000, 2021, 2500, 2999, 3000, 3500, 3999, 4000, 4500, 4999, 5000, 5999, 
    6000, 6999, 7000, 7999, 8000, 8999, 9000, 9999, 10000, 11000, 12000, 15000, 19999, 20000, 
    25000, 30000, 35000, 39999, 40000, 45000, 49999, 50000, 55000, 59999, 60000, 65000, 69999,
    70000, 75000, 79999, 80000, 85000, 89999, 90000, 95000, 99999, 100000, 150000, 199999, 
    200000, 250000, 299999, 300000, 350000, 399999, 400000, 450000, 499999, 500000, 600000, 
    700000, 800000, 900000, 999999, 1000000, -1, -10, -99, -100, -101, -999, -1000, -1001, 
    -9999, -10000, -25000, -50000, -100000, -500000, -999999, -1000000
]

# URL base da API
url_base = "https://api-numero-por-extenso.vercel.app/extenso?numero="
# url_base = "http://127.0.0.1:5000/extenso?numero="

# Dicionário para armazenar os resultados
resultados = {}

# Testando cada número
for numero in numeros_para_testar:
    response = requests.get(url_base + str(numero))
    
    if response.status_code == 200:
        resultado_json = response.json()
        resultados[numero] = resultado_json.get("resultado", "Erro no formato da resposta")
    else:
        resultados[numero] = f"Erro HTTP {response.status_code}"

# Criando DataFrame com os resultados
df_resultados = pd.DataFrame(resultados.items(), columns=["Número", "Extenso"])

# Exibir os resultados
# print(df_resultados)

f = open("testar_api.txt", "a", encoding="utf-8")
for _, row in df_resultados.iterrows():
    numero = str(row.get("Número"))
    extenso = row.get("Extenso")
    texto = '{}{}'.format(numero.ljust(8), ': '+extenso)
    print(texto)
    f.write(texto+"\n")
f.close()
