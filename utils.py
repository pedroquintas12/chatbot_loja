import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('portuguese'))
pontuacao = set(string.punctuation)

def preprocessar(texto):
    tokens = word_tokenize(texto.lower())
    tokens = [t for t in tokens if t not in stop_words and t not in pontuacao]
    return tokens
