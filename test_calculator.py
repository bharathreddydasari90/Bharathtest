import calculator_app

def test_add():
    assert calculator_app.add(2, 3) == 5

def test_subtract():
    assert calculator_app.subtract(5, 3) == 2

def test_multiply():
    assert calculator_app.multiply(4, 3) == 12

def test_divide():
    assert calculator_app.divide(10, 2) == 5
