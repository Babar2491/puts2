from fractions import Fraction
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


@app.route('/add')
def addition():
    value1 = request.args.get('A', type=float) or request.args.get('A', type=Fraction) or 0.000
    value2 = request.args.get('B', type=float) or request.args.get('B', type=Fraction) or 0.000
    result = value1+value2
    return '%0.3f \n' % result


@app.route('/subtract')
def subtraction():
    value1 = request.args.get('A', type=float) or request.args.get('A', type=Fraction) or 0.000
    value2 = request.args.get('B', type=float) or request.args.get('B', type=Fraction) or 0.000
    result = value1-value2
    return '%0.3f \n' % result


@app.route('/multiply')
def multiplication():
    value1 = request.args.get('A', type=float) or request.args.get('A', type=Fraction) or 0.000
    value2 = request.args.get('B', type=float) or request.args.get('B', type=Fraction) or 0.000
    result = value1*value2
    return '%0.3f \n' % result


@app.route('/divide')
def division():
    value1 = request.args.get('A', type=float) or request.args.get('A', type=Fraction) or 0.000
    value2 = request.args.get('B', type=float) or request.args.get('B', type=Fraction) or 0.000
    result = value1/value2
    return '%0.3f \n' % result

if __name__ == "__main__":
    app.run()
