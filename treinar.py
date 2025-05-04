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


stop_words = set(stopwords.words('portuguese'))
pontuacao = set(string.punctuation)


with open('intents.json', encoding='utf-8') as f:
    data = json.load(f)


texts = []
labels = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        texts.append(pattern)
        labels.append(intent['tag'])


combined = list(zip(texts, labels))
random.shuffle(combined)
texts, labels = zip(*combined)


vectorizer = TfidfVectorizer(tokenizer=preprocessar)
X = vectorizer.fit_transform(texts)


model = MultinomialNB()
model.fit(X, labels)


with open('chat_model.pkl', 'wb') as f:
    pickle.dump(model, f, protocol=pickle.HIGHEST_PROTOCOL)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f, protocol=pickle.HIGHEST_PROTOCOL)

print("Modelo treinado com sucesso e otimizado!")
