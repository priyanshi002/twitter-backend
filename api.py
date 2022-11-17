from flask import Flask
from flask_restx import Api
from flask_cors import CORS

##############Import service###############
from services.service_twitter_analysis import api as TwitterNLP


flask_app = Flask(__name__)
CORS(flask_app)

# ==================================== JWT START =====================================
AUTH = {
    'apikey' :{
        'type' : 'apiKey',
        'in' : 'header',
        'name' : 'Authorization'
    }
}
API = Api(flask_app, authorizations= AUTH)
# ================================= JWT END ==========================================

############Append Namespace##############
API.add_namespace(TwitterNLP)

if __name__ == '__main__':
    flask_app.run(port=8080,debug=True)