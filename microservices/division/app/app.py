from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Divide(Resource):
    def get(self, num1, num2):
        try:
            result = float(num1) / float(num2)
        except:
            result="UNDEFINED"
        return {'result': result}

api.add_resource(Divide, '/<int:num1>/<int:num2>')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5054)
