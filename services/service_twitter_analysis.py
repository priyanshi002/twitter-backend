from flask_restx import Resource
from models.twitter_analysis_model import api, Twitter_Payload
from bl.twitter_analysis import fetch_tweets_analysis

@api.route('/analyse')
class Follow(Resource):
    @api.expect(Twitter_Payload)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def post(self):
        response = fetch_tweets_analysis(api.payload['keyword'])
        return response