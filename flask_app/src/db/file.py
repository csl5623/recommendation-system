news_api_key = '940fdaaa135b4c1387757b9c30c2519d'
open_api_key = "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"

# call news api 
import openai
import psycopg2
import requests
import re
import os
import yaml


openai.api_key = open_api_key


def connect():
    config = {}
    yml_path = os.path.join(os.path.dirname(__file__), '../../config/db.yml')
    with open(yml_path, 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return psycopg2.connect(dbname=config['database'],
                            user=config['user'],
                            password=config['password'],
                            host=config['host'],
                            port=config['port'])


def build_sql(path):
    full_path = os.path.join(os.path.dirname(__file__), f'../../{path}')
    conn = connect()
    cur = conn.cursor()
    with open(full_path, 'r') as file:
        cur.execute(file.read())
        conn.commit()
        conn.close()
    

def api_requests():
    url = f'https://newsapi.org/v2/everything?q=bitcoin&apiKey={news_api_key}'
    response = requests.get(url)
    data = []
    for r in response.json()["articles"]:
        cleaned_txt = re.sub(r'...\[s*\+\d+\s*chars\]$', '', r["content"])
        data.append((
            r["title"],
            cleaned_txt
        ))
    
    query = "insert into news_articles(title,content) VALUES (%s,%s)"
    conn1 = connect()
    cur = conn1.cursor()
    cur.executemany(query,data)
    conn1.commit()
    conn1.close()


#use openai api to get the embeddings for the texts
#An embedding is a vector (list) of floating point numbers. open ai text emebedding model transforms the text given into embeddings
#The distance between two vectors measures their relatedness. Small distances suggest high relatedness, and large distances suggest low relatedness.

def get_embedding(text):
    response = openai.embeddings.create(input=text, model="text-embedding-ada-002")
    return response['data'][0]['embedding']

def process_store_embeddings():
    conn1 = connect()
    cur = conn1.cursor()
    cur.execute("SELECT id,content from news_articles")
    news_articles = cur.fetchall()
    for id,content in news_articles:
        embedding = get_embedding(content)
        cur.execute('insert into news_embeddings values (%s,%s)',(id,embedding))
        conn1.commit()

    conn1.close() 
    return None
    

#performs a search similarity between the vectors, content given in the function and the embeddings already stored in the news_articles table
def recommendation_algorithm(content):
    emd = get_embedding(content)
    query = """   
    SELECT n.id,n.title,n.content from news_articles n
    JOIN news_embeddings e ON e.id and n.id
    WHERE embedding <-> %s
    ORDER BY embedding
    """
    conn1 = connect()
    cur = conn1.cursor()
    cur.execute(query,(emd))

    rec_list = cur.fetchall()
    conn1.close()
    return rec_list




