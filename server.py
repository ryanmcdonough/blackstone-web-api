import os
import spacy
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

nlp = spacy.load("en_blackstone_proto")

app = Flask(__name__)
api = Api(app)

@app.route('/ner', methods=['POST'])
def ner():
    req_data = request.get_json()
    text = req_data['text']
                
    doc = nlp(text) 

    return doc.ents

@app.route("/test")
def test():
    req_data = request.get_json()
    text = req_data['text']
                
    doc = nlp(text) 

    return doc.ents


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
