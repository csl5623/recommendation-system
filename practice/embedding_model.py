from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt_tab')

sentences = [
    "This is a sample sentence",
    "Word embeddings are useful",
    "We are learning how to build them"
]


tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]

model = Word2Vec(sentences=tokenized_sentences, vector_size=100, window=5, min_count=1, workers=4)

word_embedding = model.wv['sample']
print(word_embedding)
