# 🛍️ Chatbot Loja

Este projeto é um chatbot inteligente para auxiliar clientes de uma loja virtual, com interface web e backend em Python. Ele responde perguntas frequentes, sugere produtos e oferece um atendimento automatizado utilizando NLP (Processamento de Linguagem Natural) com modelos treinados.

## 📸 Visão Geral

O sistema possui:

- Interface Web com HTML/CSS/JS
- Backend Flask
- Base de conhecimento em JSON
- Treinamento de modelo com `scikit-learn`
- Conexão com banco de dados via SQLite
- Código modular (consultas, utilitários, conexões)

## 🚀 Funcionalidades

- Treinamento de modelo com intents (intents.json)
- Atendimento automático com respostas inteligentes
- Sugestão de produtos
- Consulta de dados no banco de dados
- Interface web para interação com o chatbot

## 🧠 Tecnologias Usadas

- Python 3.12
- Flask
- scikit-learn
- SQLite
- HTML, CSS, JavaScript

## 📁 Estrutura do Projeto

```
chatbot_loja-main/
├── app.py                     # Inicia o servidor Flask
├── chatbot.py                # Lógica principal do chatbot
├── treinar.py                # Treinamento do modelo
├── intents.json              # Base de conhecimento do chatbot
├── utils.py                  # Funções auxiliares
├── conexao.py                # Conexão com banco de dados
├── consultas.py              # Funções de consulta ao banco
├── chat_model.pkl            # Modelo treinado
├── vectorizer.pkl            # Vetorizador treinado
├── produtos_informatica.sql  # Script do banco de dados
├── requirements.txt          # Dependências do projeto
├── static/
│   ├── styles.css            # Estilo da interface
│   └── script.js             # Script do chatbot na web
├── templates/
│   └── index.html            # Página principal do chatbot
```

## ⚙️ Instalação e Execução

### 1. Clone o repositório

```bash
git clone https://github.com/pedroquintas12/chatbot_loja.git
cd chatbot_loja
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Treine o modelo (se necessário)

```bash
python treinar.py
```

### 5. Inicie a aplicação

```bash
python app.py
```

Acesse [http://localhost:5000](http://localhost:5000) no navegador para usar o chatbot.

## 💬 Exemplo de Uso

- “Quais são os produtos de informática?”
- “Quais são as formas de pagamento?”
- “Onde está meu pedido?”
- “Falar com um atendente”

## 📌 Requisitos

- Python 3.8+
- Navegador moderno
- Ambiente com acesso a terminal

## 📄 Licença

Este projeto está sob a licença MIT.
