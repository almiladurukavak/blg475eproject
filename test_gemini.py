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


##Almila Duru Kavak

##MODERATE LEVEL PROBLEMS

def test_fib():
    assert fib(3) == 2
    assert fib(5) == 5
    assert fib(7) == 13
    print("All test cases for fib passed!")

def test_common():
    assert common([1, 2, 3], [3, 2, 1]) == [1, 2, 3]
    assert common([1, 2, 3, 4], [5, 6, 7, 8]) == []
    assert common(['a', 'b', 'c'], ['b', 'c', 'd']) == ['b', 'c']
    print("All test cases for common passed!")


def test_even_odd_palindrome():
    assert even_odd_palindrome(5) == (2, 3)
    assert even_odd_palindrome(15) == (4, 7)
    assert even_odd_palindrome(20) == (6, 9)
    print("All test cases for even_odd_palindrome passed!")


def test_sum_squares():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([]) == 0
    assert sum_squares([-1, -5, 2, -1, -5]) == -126
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 50
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 130
    print("All test cases for sum_squares passed!")


def test_specialFilter():
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert specialFilter([11, 22, 33, 44, 55]) == 1
    assert specialFilter([13, 24, 35, 46, 57]) == 3
    assert specialFilter([111, 222, 333, 444, 555]) == 1
    print("All test cases for specialFilter passed!")

def test_is_bored():
    assert is_bored("Hello world") == 0
    assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert is_bored("I am bored!") == 1
    assert is_bored("Are you bored? I am.") == 1
    assert is_bored("I think so. Really?") == 1
    assert is_bored("I am. I am too!") == 2
    assert is_bored("I begin. What about you?") == 1
    assert is_bored("End of story.") == 0
    assert is_bored("I?") == 1
    assert is_bored("I!") == 1
    assert is_bored(" I am first.") == 0 # Başında boşluk var
    assert is_bored("I am. Then I go!") == 2
    print("All test cases for is_bored passed!")


def test_encrypt():
    assert encrypt('hi') == 'lm'
    assert encrypt('asdfghjkl') == 'ewhjklnop'
    assert encrypt('gf') == 'kj'
    assert encrypt('et') == 'ix'
    assert encrypt('abc') == 'efg'
    assert encrypt('xyz') == 'bcd'
    assert encrypt('aBcDeFg') == 'eFgHiJk'
    assert encrypt('123abcXYZ') == '123efgBCD'
    print("All test cases for encrypt passed!")



def test_rounded_avg():
    assert rounded_avg(1, 5) == "0b11"
    assert rounded_avg(7, 5) == -1
    assert rounded_avg(10, 20) == "0b1111"
    assert rounded_avg(20, 33) == "0b11010"
    assert rounded_avg(1, 1) == "0b1"
    assert rounded_avg(2, 4) == "0b10"
    assert rounded_avg(3, 6) == "0b100"
    assert rounded_avg(1, 2) == "0b10"
    assert rounded_avg(2, 3) == "0b10"
    print("All test cases for rounded_avg passed!")

def test_minSubArraySum():
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert minSubArraySum([-1, -2, -3]) == -6
    assert minSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == -5
    assert minSubArraySum([1, -1, -2, 1]) == -2
    assert minSubArraySum([-5]) == -5
    assert minSubArraySum([5]) == 5
    assert minSubArraySum([0, -1, 2]) == -1
    print("All test cases for minSubArraySum passed!")


def test_intersection_function():
    assert intersection((1, 2), (2, 3)) == "NO"
    assert intersection((-1, 1), (0, 4)) == "NO"
    assert intersection((-3, -1), (-5, 5)) == "YES"
    assert intersection((1, 5), (2, 3)) == "YES"
    assert intersection((1, 5), (5, 8)) == "NO"
    assert intersection((1, 10), (1, 10)) == "YES"
    assert intersection((0, 0), (0, 0)) == "NO"
    assert intersection((0, 1), (2, 3)) == "NO"
    assert intersection((0, 3), (1, 5)) == "YES"
    assert intersection((-5, -2), (-4, -1)) == "YES"
    print("All test cases for intersection passed!")

### HARD LEVEL PROBLEMS ###

def test_total_match():
  assert total_match([], []) == []
  assert total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
  assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
  assert total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
  assert total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']
  assert total_match(['apple', 'banana'], ['kiwi', 'orange']) == ['kiwi', 'orange']
  assert total_match(['one', 'two', 'three'], ['a', 'b', 'c', 'd', 'e']) == ['one', 'two', 'three']

def test_will_it_fly():
  assert will_it_fly([1, 2], 5) == False
  assert will_it_fly([3, 2, 3], 1) == False
  assert will_it_fly([3, 2, 3], 9) == True

def test_circular_shift():
  assert circular_shift(12, 1) == "21"
  assert circular_shift(12345, 2) == "45123"
  assert circular_shift(123, 5) == "321"

def test_reverse_delete():
  assert reverse_delete("abcde", "ae") == ('bcd', False)
  assert reverse_delete("abcdef", "b") == ('acdef', False)
  assert reverse_delete("abcdedcba", "ab") == ('cdedc', True)

def test_minPath():
  # Test case 1: Simple 2x2 grid, k=2
  grid1 = [[1, 2], [3, 4]]
  k1 = 2
  expected1 = [1, 2]
  assert minPath(grid1, k1) == expected1

  # Test case 2: Larger grid with a longer path, k=3
  grid2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  k2 = 3
  result2 = minPath(grid2, k2)
  assert len(result2) == k2
  assert result2[0] in [1, 2, 4] # Starting from any cell in the first step is valid for a path of length 3

  # Test case 3: Grid with all same values, k=4
  grid3 = [[5, 5], [5, 5]]
  k3 = 4
  expected3 = [5, 5, 5, 5]
  assert minPath(grid3, k3) == expected3

def test_move_one_ball():
  assert move_one_ball([1, 2, 3, 4, 5]) == True
  assert move_one_ball([3, 4, 5, 1, 2]) == True
  assert move_one_ball([1, 3, 2]) == False

def test_strongest_extension():
  assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
  assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
  assert Strongest_Extension('Data', ['Process', 'AnalyzeData', 'Report']) == 'Data.AnalyzeData'

def test_right_angle_triangle():
  assert right_angle_triangle(3, 4, 5) == True
  assert right_angle_triangle(1, 2, 3) == False
  assert right_angle_triangle(5, 12, 13) == True

def test_do_algebra():
  operator1 = ['+', '*', '-']
  operand1 = [2, 3, 4, 5]
  assert do_algebra(operator1, operand1) == 9

  operator2 = ['**', '//', '+']
  operand2 = [2, 3, 10, 4]
  assert do_algebra(operator2, operand2) == 10

  operator3 = ['-', '+', '*']
  operand3 = [10, 5, 2, 3]
  assert do_algebra(operator3, operand3) == 21

def test_decode_cyclic():
  assert decode_cyclic("cba") == "abc"
  assert decode_cyclic("defghi") == "abcdefghi"
  assert decode_cyclic("jklmno") == "jklmno"