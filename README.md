# API - Conversor de Números para Extenso

Este projeto é uma API em Python que recebe um número como entrada e retorna sua representação por extenso.

## Funcionalidades

- Recebe um número via requisição HTTP.
- Retorna o número em formato por extenso.
- Contém um script para testar a API e registrar os resultados em um arquivo de texto.

## Tecnologias Utilizadas

- Python
- Flask

## Instalação e Execução

### 1. Clonar o repositório

```sh
git clone https://github.com/ViniciusTAC/api_numero_por_extenso
cd api_numero_por_extenso-main
```

### 2. Criar e ativar um ambiente virtual (opcional, mas recomendado)

```sh
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
```

### 3. Instalar as dependências

```sh
pip install -r requirements.txt
```

### 4. Executar a API

```sh
python main.py
```

## Como Usar

Fazer uma requisição GET para:

```
http://localhost:porta/extenso?numero=<numero>
```

Exemplo:

```
http://localhost:porta/extenso?numero=150
```

Resposta:

```json
{
  "resultado": "cento e vinte e três"
}
```

## Testando a API

O arquivo `testar_api.py` executa testes automáticos na API e salva os resultados em um arquivo `resultado.txt`.
Para rodar o teste:

```sh
python testar_api.py
```

## Deploy

O projeto contém um arquivo `vercel.json`, sugerindo que pode ser implantado no Vercel. Para isso, instale o CLI do Vercel e execute:

```sh
vercel
```

## Contribuição

Sinta-se à vontade para contribuir enviando pull requests ou sugerindo melhorias.

## Licença

Este projeto está sob a licença MIT.

