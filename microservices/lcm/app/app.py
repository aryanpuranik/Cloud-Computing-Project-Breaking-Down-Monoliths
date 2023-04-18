from flask import Flask
from flask_restful import Resource, Api
import math

app = Flask(__name__)
api = Api(app)

class Lcm(Resource):
    def get(self, num1, num2):
        if num1 > num2:
            greater = num1
        else:
            greater = num2

        while(True):
            if((greater % num1 == 0) and (greater % num2 == 0)):
                lcm = greater
                break
            greater += 1

        return {'result':lcm}


api.add_resource(Lcm, '/<int:num1>/<int:num2>')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5056)
