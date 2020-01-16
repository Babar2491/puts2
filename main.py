from __future__ import division

from fractions import Fraction
from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


@app.route('/add')
def addition():
    value1 = request.args.get('A', type=int) or request.args.get('A', type=float) or request.args.get('A', type=Fraction) or 0.000
    value2 = request.args.get('B', type=int) or request.args.get('B', type=float) or request.args.get('B', type=Fraction) or 0.000

    has_float = isinstance(value1, (float, Fraction)) or isinstance(value2, (float, Fraction))

    result = value1 + value2

    if isinstance(result, Fraction):
        result = float(result)

    if has_float:
        return str(float(format(result, ".12g")))
    return str(format(result, '.12g'))


@app.route('/subtract')
def subtraction():
    value1 = request.args.get('A', type=int) or request.args.get('A', type=float) or request.args.get('A', type=Fraction) or 0.000
    value2 = request.args.get('B', type=int) or request.args.get('B', type=float) or request.args.get('B', type=Fraction) or 0.000

    has_float = isinstance(value1, (float, Fraction)) or isinstance(value2, (float, Fraction))

    result = value1 - value2

    if isinstance(result, Fraction):
        result = float(result)

    if has_float:
        return str(float(format(result, ".12g")))
    return str(format(result, '.12g'))


@app.route('/multiply')
def multiplication():
    value1 = request.args.get('A', type=int) or request.args.get('A', type=float) or request.args.get('A', type=Fraction) or 0.000
    value2 = request.args.get('B', type=int) or request.args.get('B', type=float) or request.args.get('B', type=Fraction) or 0.000

    has_float = isinstance(value1, (float, Fraction)) or isinstance(value2, (float, Fraction))

    result = value1 * value2

    if isinstance(result, Fraction):
        result = float(result)

    if has_float:
        return str(float(format(result, ".12g")))
    return str(format(result, '.12g'))


@app.route('/divide')
def division():
    value1 = request.args.get('A', type=int) or request.args.get('A', type=float) or request.args.get('A', type=Fraction) or 0.000
    value2 = request.args.get('B', type=int) or request.args.get('B', type=float) or request.args.get('B', type=Fraction) or 0.000

    has_float = isinstance(value1, (float, Fraction)) or isinstance(value2, (float, Fraction))

    result = value1 / value2

    if isinstance(result, Fraction):
        result = float(result)

    if has_float:
        return str(float(format(result, ".12g")))
    return str(format(result, '.12g'))

if __name__ == "__main__":
    app.run()
