class NerNlp(Resource):
        def post(self):
                
                req_data = request.get_json()
                text = req_data['text']
                
                doc = nlp(text) 

                return doc.ents

        def get(self):
                                
                return { 'Response': 'Success' }