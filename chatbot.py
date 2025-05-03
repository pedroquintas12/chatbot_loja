from consultas import buscar_produto
import nltk
from nltk.tokenize import word_tokenize
import random
import json
import pickle
from utils import preprocessar


nltk.download('punkt')

# Carrega intents
with open('intents.json', encoding='utf-8') as file:
    data = json.load(file)

# Carrega modelo IA e vetor
with open('chat_model.pkl', 'rb') as f:
    modelo_ia = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vetor_ia = pickle.load(f)

def responder(mensagem):
    tokens = word_tokenize(mensagem.lower())

    # Regras fixas (mantidas)
    if any(p in mensagem.lower() for p in ["me fale sobre", "me mostra o", "detalhes do", "informações do", "tem o"]):
        nome_produto = extrair_nome_produto(mensagem)
        return recomendar_produto(nome_produto)

    # Detecção de intenção com IA
    try:
        X = vetor_ia.transform([mensagem])
        tag_prevista = modelo_ia.predict(X)[0]

        # Ações com base na intenção
        if tag_prevista == "listar_produtos":
            return listar_produtos()
        elif tag_prevista == "recomendar_produto":
            nome_produto = extrair_nome_produto(mensagem)
            return recomendar_produto(nome_produto)

        # Outras respostas do intents.json
        for intent in data['intents']:
            if intent['tag'] == tag_prevista:
                return random.choice(intent['responses'])

    except:
        pass

    return "Desculpe, não entendi. Pode repetir ou pedir para falar com um atendente?"


def listar_produtos():
    produtos = buscar_produto("")
    if produtos:
        resposta = "Temos os seguintes produtos:\n"
        for p in produtos:
            resposta += f"- {p['nome']} (R$ {p['preco']:.2f})\n"
        resposta += "Para mais informações, digite 'detalhes do' + o nome do produto."
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
    return nome.strip()
