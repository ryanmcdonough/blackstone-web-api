import os
import spacy
from flask import Flask, request
from flask_restful import Resource, Api

nlp = spacy.load("en_blackstone_proto")

app = Flask(__name__)
api = Api(app)


class NerNlp(Resource):
        def post(self):
                
                req_data = request.get_json()
                text = req_data['text']
                
                doc = nlp(text) 

                return doc.ents


api.add_resource(NerNlp, '/ner')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
