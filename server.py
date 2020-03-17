import os
import spacy
from flask import Flask, request
from flask_restful import Resource, Api

from resources.NerNlp import NerNlp

nlp = spacy.load("en_blackstone_proto")

app = Flask(__name__)
api = Api(app)


api.add_resource(NerNlp, '/ner')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
