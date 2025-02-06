import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fizzbuzz import fizzbuzz

def test_fizz():
    assert fizzbuzz(4)[2] == "Fizz"
    assert fizzbuzz(7)[5] == "Fizz"
    assert fizzbuzz(10)[8] == "Fizz"

def test_buzz():
    assert fizzbuzz(6)[4] == "Buzz"
    assert fizzbuzz(11)[9] == "Buzz"
    assert fizzbuzz(21)[19] == "Buzz"

def test_fizzbuzz():
    assert fizzbuzz(16)[14] == "FizzBuzz"
    assert fizzbuzz(31)[29] == "FizzBuzz"
    assert fizzbuzz(46)[44] == "FizzBuzz"

def test_numbers():
    assert fizzbuzz(2)[0] == '1'
    assert fizzbuzz(3)[1] == '2'
    assert fizzbuzz(5)[3] == '4'
