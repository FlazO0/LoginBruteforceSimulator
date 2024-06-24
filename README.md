# Sistema de Login Falso com Ataque de Força Bruta

Este é um projeto de demonstração que simula um sistema de login falso utilizando Flask, uma biblioteca web em Python, e um script de ataque de força bruta para tentar encontrar a senha de acesso.

## Funcionalidades

- Página de login com usuário e senha.
- Verificação de login falso com uma senha padrão.
- Mensagens de sucesso ou falha no login.
- Script de força bruta para encontrar a senha.

## Tecnologias Utilizadas

- **Flask:** Biblioteca web em Python para criação de aplicativos web.
- **Requests:** Biblioteca HTTP para Python, utilizada no script de força bruta.

## Configuração e Uso

1. Clone o repositório:
   ```bash
   git clone https://github.com/FlazO0/LoginBruteforceSimulator.git
   cd LoginBruteforceSimulator
   ```

2. Instale as dependências:
   Certifique-se de ter o Flask instalado. Você pode instalar as dependências utilizando o pip:
   ```bash
   pip install Flask requests
   ```

3. Execute o aplicativo Flask:
   Execute o seguinte comando para iniciar o aplicativo Flask:
   ```bash
   python FakeServer/app.py
   ```

4. Execute o script de força bruta:
   Abra um novo terminal e execute o seguinte comando para iniciar o script de força bruta:
   ```bash
   python BruteForceTool/app.py
   ```

5. Acesse o sistema:
   Abra um navegador web e acesse o seguinte endereço para acessar o sistema:
   ```
   http://localhost:5000/
   ```

6. Experimente diferentes senhas:
   Você pode editar o arquivo `wordlist.txt` para incluir diferentes senhas e testar o script de força bruta.

## Atenção

Este projeto é apenas uma simulação educacional e não deve ser utilizado para atividades maliciosas. Não tente acessar sistemas ou contas de outras pessoas sem permissão.
