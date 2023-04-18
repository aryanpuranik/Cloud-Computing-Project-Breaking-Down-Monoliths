from flask import Flask, render_template, request, flash, redirect, url_for
import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


def add(n1, n2):
    # return n1+n2
    response = requests.get(f'http://addition-service:5051/{n1}/{n2}')
    result = response.json()['result']
    return result

def minus(n1, n2):
    # return n1-n2
    response = requests.get(f'http://subtraction-service:5052/{n1}/{n2}')
    result = response.json()['result']
    return result

def multiply(n1, n2):
    # return n1*n2
    response = requests.get(f'http://multiplication-service:5053/{n1}/{n2}')
    result = response.json()['result']
    return result

def divide(n1, n2):
    # return n1/n2
    response = requests.get(f'http://division-service:5054/{n1}/{n2}')
    result = response.json()['result']
    return result

def gcd(n1,n2):
    response = requests.get(f'http://gcd-service:5055/{n1}/{n2}')
    result = response.json()['result']
    return result

def lcm(n1,n2):
    response = requests.get(f'http://lcm-service:5056/{n1}/{n2}')
    result = response.json()['result']
    return result

def modulus(n1,n2):
    response = requests.get(f'http://modulus-service:5057/{n1}/{n2}')
    result = response.json()['result']
    return result

def exponent(n1,n2):
    response = requests.get(f'http://exponent-service:5058/{n1}/{n2}')
    result = response.json()['result']
    return result

def equal_to(n1,n2):
    response = requests.get(f'http://equal-service:5059/{n1}/{n2}')
    result = response.json()['result']
    return result

@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = request.form.get('first')
    number_2 = request.form.get('second')
    operation = request.form.get('operation')
    result = 0
    try:
        number_1=int(number_1)
        number_2=int(number_2)
        if operation == 'add':
            result = add(number_1, number_2)
        elif operation == 'minus':
            result =  minus(number_1, number_2)
        elif operation == 'multiply':
            result = multiply(number_1, number_2)
        elif operation == 'divide':
            # if(number_2!=0):
            result = divide(number_1, number_2)
            # else:
                # result="undef"
                # flash("Second Number can't be 0 for Division.......")
        elif operation == 'gcd':
            result =  gcd(number_1, number_2)
        elif operation == 'lcm':
            result = lcm(number_1, number_2)
        elif operation == 'modulus':
            result = modulus(number_1, number_2)
        elif operation == 'exponent':
            result =  exponent(number_1, number_2)
        elif operation == 'equal_to':
            result =  equal_to(number_1, number_2)
        flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    except(TypeError,ValueError,ZeroDivisionError):
        flash("Please enter valid numbers.")



    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )

