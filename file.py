news_api_key = '940fdaaa135b4c1387757b9c30c2519d'
open_api_key = ' '

# call news api 

import openai
import psycopg2
import requests

url = f'https://newsapi.org/v2/everything?q=bitcoin&apiKey={news_api_key}'

response = requests.get(url)
print(response.text)




