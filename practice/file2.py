news_api_key = '940fdaaa135b4c1387757b9c30c2519d'
open_api_key = "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"

# call news api 
from json_example import json_example
import openai
import psycopg2
import requests
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk
import re

nltk.download('punkt_tab')
openai.api_key = open_api_key

conn1 = psycopg2.connect(
    host="localhost",
    port="5433",
    database="pgvector_project",
    user="postgres",
    password="carla16"
)
cur = conn1.cursor()
def api_requests():
    # url = f'https://newsapi.org/v2/everything?q=bitcoin&apiKey={news_api_key}'
    # response = requests.get(url)

    data = []
    for r in json_example["articles"]:
        # content = re.sub("[0-9]"," ", r["content"])
        content = re.sub(r'\s*\[\+\d+\]$', '', r["content"])
        data.append((
           r["title"],
           content
         ))
    print(data)
    
    # query = "insert into news_articles(title,content) VALUES (%s,%s)"
    # cur.executemany(query,data)
    conn1.commit()


#use openai api to get the embeddings for the texts
#An embedding is a vector (list) of floating point numbers. open ai text emebedding model transforms the text given into embeddings
#The distance between two vectors measures their relatedness. Small distances suggest high relatedness, and large distances suggest low relatedness.

def get_embedding(news_articles,text):
    tokenized_sentences = []
    for id,content in news_articles:
        tokenized_sentence =  word_tokenize(content.lower())
        tokenized_sentences.append(tokenized_sentence)
    print(tokenized_sentences)


    model = Word2Vec(sentences=tokenized_sentences, vector_size=100, window=5, min_count=1, workers=4)

    word_embedding = model.wv[text]
    return word_embedding


def process_store_embeddings():
    cur.execute("SELECT id,content from news_articles")
    news_articles = cur.fetchall()
    for id,content in news_articles:
        embedding = get_embedding(news_articles,content)
        cur.execute('insert into news_embeddings values (%s,%s)',(id,embedding))
        conn1.commit()


def recommendation_algorithm(content):
    emd = get_embedding(content)
    #performs a search similarity between the vectors, content given in the function and the embeddings already stored in the news_articles table
    query = """   
    SELECT n.title,n.content from news_articles n
    JOIN news_embeddings e ON e.id and n.id
    WHERE embedding <-> %s
    ORDER BY embedding
    """
    cur.execute(query,(emd))
    return cur.fetchall()


def main():
    api_requests()
   


main()