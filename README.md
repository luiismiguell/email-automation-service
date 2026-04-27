# Email Automation Service

Sistema backend para automação de envio de e-mails, com API construída em FastAPI e interface web opcional para interação.

## 📌 Contexto

Projeto desenvolvido com o objetivo de automatizar o envio de e-mails e servir como base para integração com sistemas e fluxos de comunicação.

## 🧱 Estrutura do projeto

* `backend/`

  * `main.py` → aplicação FastAPI com rotas da API
  * `services/` → lógica de envio de e-mails
  * `config/` → gerenciamento de variáveis de ambiente
  * `requirements.txt` → dependências do projeto
* `frontend/` → interface web simples para envio de e-mails
* `.env.example` → modelo de configuração
* `.gitignore` → arquivos ignorados pelo Git

## 🛠️ Tecnologias utilizadas

* Python
* FastAPI
* SMTP (envio de e-mails)
* HTML, CSS e JavaScript (frontend)

## ⚙️ Como usar

1. Copie `.env.example` para `.env`

2. Preencha as variáveis:

```env
EMAIL_USER=seu_email@example.com
EMAIL_PASS=sua_senha_ou_token_de_app
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

3. Instale as dependências:

```bash
cd backend
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate

pip install -r requirements.txt
```

4. Inicie o servidor:

```bash
uvicorn main:app --reload
```

5. Abra `frontend/index.html` no navegador e envie um e-mail.

## 🔗 API

* `GET /` → verifica se o serviço está rodando
* `POST /send-email` → envia um e-mail

### Exemplo de payload

```json
{
  "email": "destino@example.com",
  "subject": "Assunto",
  "message": "Corpo da mensagem"
}
```

## 🎯 Objetivo

Criar um serviço reutilizável para automação de envio de e-mails, com estrutura organizada e possibilidade de integração com diferentes sistemas.

## 🔐 Segurança

* Nunca versionar arquivos `.env`
* Utilizar variáveis de ambiente para credenciais sensíveis
* Recomenda-se uso de senha de aplicativo para serviços de e-mail
