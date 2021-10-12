import pytest

@pytest.fixture()
def setup():
    print("once before every method")

@pytest.yield_fixture()
def setup2():
    print("once before every method")
    yield
    print("once after every method")

def testMethod1(setup):
    print("test method 1")

def testMethod2(setup):
    print("test method 2")

def testMethod3(setup2):
    print("test method 3")

def testMethod4(setup2):
    print("test method 4")