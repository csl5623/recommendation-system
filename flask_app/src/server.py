from flask import Flask
from flask_restful import Resource, Api


from api.management import *

app = Flask(__name__)
api = Api(app)

api.add_resource(Init, '/manage/init')
api.add_resource(FetchArticles,'/manage/fetchData')
api.add_resource(StoreEmbeddings,'/manage/storeEmbeddings')
api.add_resource(SimilarArticles,'/manage/similar-articles')


if __name__ == '__main__':
    build_sql('src/db/schema.sql')
    app.run(debug=True)