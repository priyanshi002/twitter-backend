from flask_restx import Namespace, fields

api = Namespace('TwitterNLP', description='Twitter NLP')

Twitter_Payload = api.model(
    'Twitter_Payload', {
        'keyword' : fields.String(attribute='keyword')
    }
)