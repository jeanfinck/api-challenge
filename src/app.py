from flask import Flask
from flask_restful import Api
from resources.user import User
from resources.forecast import Forecast


app = Flask(__name__)
api = Api(app)
api.add_resource(User, '/users/<user_id>')
api.add_resource(Forecast, '/users/<user_id>/forecast/<forecast_id>')


if __name__ == '__main__':
    app.run(debug=True)