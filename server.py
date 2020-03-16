import os
import spacy
from flask import Flask, request
from flask_restful import Resource, Api

nlp = spacy.load("en_blackstone_proto")

app = Flask(__name__)
api = Api(app)


class SpacyCoreNlp(Resource):
        def ner(self):
                query = request.data.decode(request.charset)
                doc = nlp(text) 

                return doc.ents


api.add_resource(SpacyCoreNlp, '/core-nlp')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
