from flask_restful import Resource, reqparse, request 
from db.file import *
import json

class Init(Resource):
    def post(self):
        build_sql('src/db/schema.sql')
       

class FetchArticles(Resource):
        def post(self):
            api_requests()
            return {"message": "Success"}


class StoreEmbeddings(Resource):
     def post(self):
        process_store_embeddings()


class SimilarArticles(Resource):
    def get(self):
        p1 = request.args.get('queryString')
        similar_articles = recommendation_algorithm(p1)
        return json.dumps(similar_articles)

    
