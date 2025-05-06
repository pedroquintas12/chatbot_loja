from consultas import buscar_produto
import nltk
from nltk.tokenize import word_tokenize
import random
import json
import pickle
from utils import preprocessar
import re
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

with open('intents.json', encoding='utf-8') as file:
    data = json.load(file)

with open('chat_model.pkl', 'rb') as f:
    modelo_ia = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vetor_ia = pickle.load(f)

def responder(mensagem):
    tokens = word_tokenize(mensagem.lower())


    try:
        X = vetor_ia.transform([mensagem])
        tag_prevista = modelo_ia.predict(X)[0]

        if tag_prevista == "produto_info":
            nome_produto = extrair_nome_produto(mensagem)
            return recomendar_produto(nome_produto)
        
        if tag_prevista == "listar_produtos":
            return listar_produtos()
        elif tag_prevista == "recomendar_produto":
            nome_produto = extrair_nome_produto(mensagem)
            return recomendar_produto(nome_produto)

        for intent in data['intents']:
            if intent['tag'] == tag_prevista:
                return random.choice(intent['responses'])

    except Exception as e:
        print("Erro ao interpretar a mensagem:", e)

    return "Desculpe, não entendi. Pode repetir ou pedir para falar com um atendente?"

def listar_produtos():
    produtos = buscar_produto("")
    if produtos:
        resposta = "Temos os seguintes produtos:\n"
        for p in produtos:
            resposta += f"- <b>{p['id']}</b> {p['nome']} (R$ {p['preco']:.2f})<br>"
        resposta += "Para mais informações, digite o numero do produto."
        return resposta
    return "Nenhum produto cadastrado no momento."

def recomendar_produto(nome):
    if not nome:
        return "Por favor, diga o nome do produto que você quer saber mais."
    
    produtos = buscar_produto(nome)
    if produtos:
        p = produtos[0]
        return f"{p['nome']} - R$ {p['preco']:.2f}\nDescrição: {p['descricao']}"
    return "Não encontrei esse produto. Tente um nome diferente ou mais específico."


def extrair_nome_produto(mensagem):
    frases_remover = ["me fale sobre", "tem o", "me mostra o", "informações do", "detalhes do"]
    nome = mensagem.lower()
    for frase in frases_remover:
        nome = nome.replace(frase, "")
    
    # Remove tudo antes do primeiro número, incluindo espaços
    nome = re.sub(r'^.*?(\d+)', r'\1', nome)
    
    return nome.strip()

