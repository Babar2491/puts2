import requests

url = 'http://127.0.0.1:5000' # The root url of the flask app


def test_index_page():
    r = requests.get(url + '/')  # Assumses that it has a path of "/"
    assert r.status_code == 200  # Assumes that it will return a 200 response


def test_addition():
    r = requests.get(url + '/add?A=10&B=20')
    assert r.status_code == 200
    assert r.text == "30.000 \n"


def test_subtraction():
    r = requests.get(url + '/subtract?A=10&B=20')
    assert r.status_code == 200
    assert r.text == "-10.000 \n"


def test_multiplication():
    r = requests.get(url + '/multiply?A=10&B=20')
    assert r.status_code == 200
    assert r.text == "200.000 \n"


def test_division():
    r = requests.get(url + '/divide?A=10&B=2')
    assert r.status_code == 200
    assert r.text == "5.000 \n"


def test_addition_decimal():
    r = requests.get(url + '/add?A=10.5&B=20.7')
    assert r.status_code == 200
    assert r.text == "31.200 \n"


def test_subtraction_decimal():
    r = requests.get(url + '/subtract?A=10&B=5.5')
    assert r.status_code == 200
    assert r.text == "4.500 \n"


def test_multiplication_decimal():
    r = requests.get(url + '/multiply?A=10.2&B=2')
    assert r.status_code == 200
    assert r.text == "20.400 \n"


def test_division_decimal():
    r = requests.get(url + '/divide?A=2&B=4')
    assert r.status_code == 200
    assert r.text == "0.500 \n"


def test_addition_rational():
    r = requests.get(url + '/add?A=1/2&B=1/2')
    assert r.status_code == 200
    assert r.text == "1.000 \n"


def test_subtraction_rational():
    r = requests.get(url + '/subtract?A=3/4&B=1/2')
    assert r.status_code == 200
    assert r.text == "0.250 \n"


def test_multiplication_rational():
    r = requests.get(url + '/multiply?A=1/2&B=1/2')
    assert r.status_code == 200
    assert r.text == "0.250 \n"


def test_division_rational():
    r = requests.get(url + '/divide?A=1/6&B=1/3')
    assert r.status_code == 200
    assert r.text == "0.500 \n"
