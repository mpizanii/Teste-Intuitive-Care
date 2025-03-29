# Teste de API

Este projeto consiste em uma interface web desenvolvida com Vue.js que interage com um servidor Python para realizar buscas textuais em uma lista de operadoras carregada a partir de um arquivo CSV.

## Tecnologias Utilizadas

- **Frontend:** Vue.js
- **Backend:** Python (Django)
- **Ferramenta de Teste de API:** Postman

## 🚀 Configuração e Execução

### 1️⃣ Configurar e rodar o Backend (Python/Django)

1. Instale as dependências:

   ```sh
   pip install -r requirements.txt
   ```

2. Execute o servidor:

   ```sh
   python manage.py runserver
   ```

### 2️⃣ Configurar e rodar o Frontend (Vue.js)

1. Acesse a pasta do frontend:

   ```sh
   cd frontend
   ```

2. Instale as dependências:

   ```sh
   npm install
   ```

3. Inicie o servidor Vue:

   ```sh
   npm run serve
   ```

## 📡 API - Endpoints

### 🔎 Busca de Operadoras

**Rota:** `GET /buscar/?q=<termo>`

**Parâmetros:**
- `q`: Termo de busca (exemplo: "Odontologica")

**Exemplo de Requisição:**
```sh
curl -X GET "http://localhost:5000/buscar/?q=Odontologica"
```

**Resposta:**
```json
[
  {
    "registro_ans": "415952",
    "nome_fantasia": "CDA ASSISTENCIA ODONTOLOGICA LTDA-EPP",
    "razao_social": "CDA - ASSISTÊNCIA ODONTOLÓGICA LTDA - EPP",
    "cidade": "Campinas",
    "UF": "SP"
  }
]
```