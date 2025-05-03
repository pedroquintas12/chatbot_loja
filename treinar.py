import json
import random
import nltk
import pickle
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords
from utils import preprocessar

nltk.download('punkt')
nltk.download('stopwords')

# Stopwords e pontuação
stop_words = set(stopwords.words('portuguese'))
pontuacao = set(string.punctuation)

# Carrega intents
with open('intents.json', encoding='utf-8') as f:
    data = json.load(f)

# Coleta e pré-processa os dados
texts = []
labels = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        texts.append(pattern)
        labels.append(intent['tag'])

# Embaralha os dados (evita viés na ordem)
combined = list(zip(texts, labels))
random.shuffle(combined)
texts, labels = zip(*combined)

# Vetorização com TF-IDF
vectorizer = TfidfVectorizer(tokenizer=preprocessar)
X = vectorizer.fit_transform(texts)

# Modelo
model = MultinomialNB()
model.fit(X, labels)

# Salva modelo e vetor
with open('chat_model.pkl', 'wb') as f:
    pickle.dump(model, f, protocol=pickle.HIGHEST_PROTOCOL)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f, protocol=pickle.HIGHEST_PROTOCOL)

print("✅ Modelo treinado com sucesso e otimizado!")
