# @Authors
# Student Names: <Almila Duru Kavak, Aydan Günaydın, Umut Ural>
# Student IDs: <150150703, 150200012, 150200013>

from geminitest import *

### EASY LEVEL PROBLEMS ###

def test_make_palindrome():
    assert make_palindrome("race") == "racecar"
    assert make_palindrome("google") == "googleelgoog"
    assert make_palindrome("aabaa") == "aabaa"
    print("All test cases passed!")

def test_truncate_number():
    assert truncate_number(3.14159) == 0.14159
    assert truncate_number(-2.71828) == -0.71828
    assert truncate_number(5.0) == 0.0
    print("All test cases passed!")

def test_sum_product():
    assert sum_product([1, 2, 3, 4]) == (10, 24)
    assert sum_product([-1, 0, 1]) == (0, 0)
    assert sum_product([5]) == (5, 5)
    print("All test cases passed!")

def test_greatest_common_divisor():
    assert greatest_common_divisor(12, 18) == 6
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(10, 7) == 1
    print("All test cases passed!")

def test_strlen():
    assert strlen("hello") == 5
    assert strlen("") == 0
    assert strlen("world!") == 6
    print("All test cases passed!")

def test_max_element():
    assert max_element([1, 2, 3, 4, 5]) == 5
    assert max_element([-1, -2, -3, -4, -5]) == -1
    assert max_element([5, 4, 3, 2, 1]) == 5
    print("All test cases passed!")

def test_incr_list():
    assert incr_list([1, 2, 3, 4, 5]) == [2, 3, 4, 5, 6]
    assert incr_list([-1, -2, -3, -4, -5]) == [0, -1, -2, -3, -4]
    assert incr_list([0, 0, 0, 0, 0]) == [1, 1, 1, 1, 1]
    print("All test cases passed!")

def test_median():
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([1, 2, 3, 4]) == 2.5
    assert median([5, 2, 1, 4, 3]) == 3
    print("All test cases passed!")

def test_sum_to_n():
    assert sum_to_n(5) == 15
    assert sum_to_n(10) == 55
    assert sum_to_n(0) == 0
    print("All test cases for sum_to_n passed!")

def test_add():
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(0, 0) == 0
    print("All test cases for add passed!")