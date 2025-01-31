from flask import jsonify


def extenso(numero):
    centena = [
        "cento",
        "duzentos",
        "trezentos",
        "quatrocentos",
        "quinhentos",
        "seiscentos",
        "setecentos",
        "oitocentos",
        "novecentos",
    ]

    dezena = [
        "dez",
        "onze",
        "doze",
        "treze",
        "quatorze",
        "quinze",
        "dezesseis",
        "dezessete",
        "dezoito",
        "dezenove",
        "vinte",
        "trinta",
        "quarenta",
        "cinquenta",
        "sessenta",
        "setenta",
        "oitenta",
        "noventa",
    ]

    unidades = [
        "zero",
        "um",
        "dois",
        "três",
        "quatro",
        "cinco",
        "seis",
        "sete",
        "oito",
        "nove",
    ]
    try:
        retorno = ""

        def menor10(x):
            # print("ta chamando menor10")
            return unidades[x]

        def menor100(x):
            if x < 10:
                return menor10(x)
            # print("ta chamando menor100")
            if x < 20:
                return dezena[x - 10]

            y = int((x - 20) / 10)
            if x % 10 == 0:
                return dezena[10 + y]
            else:
                w = int(str(x - 20)[-1])
                return dezena[10 + y] + " e " + unidades[w]

        def menor1000(x):
            if x < 100:
                return menor100(x)
            # print("ta chamando menor1000")
            if x == 100:
                return "cem"

            y = int((x - 100) / 100)
            if x % 100 == 0:
                return centena[y]
            else:
                w = int(str(int((x - 100) / 100))[-1])
                teste = f"{x / 100:.2f}"
                z = int(teste[2 : len(teste)])
                print(w, z)
                return centena[w] + " e " + menor100(z)

        def maior1000(x):
            y = int(x / 1000)
            teste = f"{x / 1000:.3f}"
            # teste = float(teste)
            w = str(x / 1000).index(".")
            z = int(teste[w + 1 : len(teste)])
            retorno = (
                str("" if menor1000(y) == "um" else menor1000(y) + " ")
                + "mil"
                + str("" if z == 0 else " e " + menor1000(z))
            )

            return retorno

        retorno = ""
        if numero < 0:
            if numero <= -1000000:
                retorno = "Ainda não implementado para menores que menos 999.999"
                
                return jsonify({"resultado": f"{str(retorno)}"}), 200
            else:
                retorno = "menos "
                numero = numero * (-1)

        if numero >= 1000000:
            retorno = "Ainda não implementado para maiores que 999.999"
        else:
            if numero < 1000:
                retorno += menor1000(numero)
            if numero >= 1000:
                retorno += maior1000(numero)

        return jsonify({"resultado": f"{str(retorno)}"}), 200

    except Exception as e:
        retorno = jsonify({"erro": f"Ocorreu um erro: {str(e)}"}), 400
        return retorno
