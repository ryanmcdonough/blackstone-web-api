import os
import spacy
from flask import Flask, request
from flask_restful import Resource, Api
from blackstone.legislation_linker import extract_legislation_relations

nlp = spacy.load("en_blackstone_proto")

app = Flask(__name__)
api = Api(app)


class SpacyCoreNlp(Resource):
        def legislation(self):
                query = request.data.decode(request.charset)
                doc = nlp(text) 
                relations = extract_legislation_relations(doc)

                return relations

        def ner(self):
                query = request.data.decode(request.charset)
                doc = nlp(text) 

                return doc.ents


api.add_resource(SpacyCoreNlp, '/core-nlp')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
