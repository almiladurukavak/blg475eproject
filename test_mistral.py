# @Authors
# Student Names: <Almila Duru Kavak, Aydan Günaydın, Umut Ural>
# Student IDs: <150150703, 150200012, 150200013>

from chatgpt import *

### EASY LEVEL PROBLEMS ###
def test_make_palindrome():
    # Test Case 1: Empty String
    assert make_palindrome("") == "", "Test Case 1 Failed"

    # Test Case 2: Single Character String
    assert make_palindrome("a") == "a", "Test Case 2 Failed"

    # Test Case 3: Non-Palindromic String
    assert make_palindrome("race") == "racecar", "Test Case 3 Failed"

    print("All test cases passed!")

def test_truncate_number():
    # Test Case 1: Positive Floating Point Number
    assert truncate_number(3.5) == 0.5, "Test Case 1 Failed"

    # Test Case 2: Whole Number
    assert truncate_number(7.0) == 0.0, "Test Case 2 Failed"

    # Test Case 3: Floating Point Number with Small Decimal Part
    assert truncate_number(4.99) == 0.99, "Test Case 3 Failed"

    print("All test cases passed!")

def test_sum_product():
    # Test Case 1: Empty List
    assert sum_product([]) == (0, 1), "Test Case 1 Failed"

    # Test Case 2: List with Positive Integers
    assert sum_product([1, 2, 3, 4]) == (10, 24), "Test Case 2 Failed"

    # Test Case 3: List with Negative and Positive Integers
    assert sum_product([-1, 2, -3, 4]) == (2, 24), "Test Case 3 Failed"

    print("All test cases passed!")

def test_greatest_common_divisor():
    # Test Case 1: Coprime Numbers
    assert greatest_common_divisor(3, 5) == 1, "Test Case 1 Failed"

    # Test Case 2: Numbers with a Common Divisor
    assert greatest_common_divisor(25, 15) == 5, "Test Case 2 Failed"

    # Test Case 3: One Number is Zero
    assert greatest_common_divisor(0, 7) == 7, "Test Case 3 Failed"

    print("All test cases passed!")

def test_strlen():
    # Test Case 1: Empty String
    assert strlen('') == 0, "Test Case 1 Failed"

    # Test Case 2: Non-Empty String
    assert strlen('abc') == 3, "Test Case 2 Failed"

    # Test Case 3: String with Spaces and Special Characters
    assert strlen('Hello, World!') == 13, "Test Case 3 Failed"

    print("All test cases passed!")

def test_max_element():
    # Test Case 1: List with Positive Integers
    assert max_element([1, 2, 3]) == 3, "Test Case 1 Failed"

    # Test Case 2: List with Mixed Positive and Negative Integers
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123, "Test Case 2 Failed"

    # Test Case 3: List with Duplicate Maximum Values
    assert max_element([7, 7, 7, 1, 2]) == 7, "Test Case 3 Failed"

    print("All test cases passed!")

def test_incr_list():
    # Test Case 1: List with Positive Integers
    assert incr_list([1, 2, 3]) == [2, 3, 4], "Test Case 1 Failed"

    # Test Case 2: List with Mixed Positive and Negative Integers
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124], "Test Case 2 Failed"

    # Test Case 3: List with Negative Integers
    assert incr_list([-1, -2, -3]) == [0, -1, -2], "Test Case 3 Failed"

    print("All test cases passed!")

def test_median():
    # Test Case 1: Odd-length list
    assert median([3, 1, 2, 4, 5]) == 3, "Test Case 1 Failed"

    # Test Case 2: Even-length list
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0, "Test Case 2 Failed"

    # Test Case 3: List with negative and positive numbers
    assert median([-5, -1, 0, 2, 3]) == 0, "Test Case 3 Failed"

    print("All test cases passed!")

def test_sum_to_n():
    # Test Case 1
    assert sum_to_n(30) == 465, "Test Case 1 Failed"

    # Test Case 2
    assert sum_to_n(100) == 5050, "Test Case 2 Failed"

    # Test Case 3
    assert sum_to_n(5) == 15, "Test Case 3 Failed"

    print("All test cases passed!")

def test_add():
    # Test Case 1
    assert add(2, 3) == 5, "Test Case 1 Failed"

    # Test Case 2
    assert add(5, 7) == 12, "Test Case 2 Failed"

    # Additional Test Case 3: Negative Numbers
    assert add(-1, -2) == -3, "Test Case 3 Failed"

    print("All test cases passed!")
    
### MEDIUM LEVEL PROBLEMS ###

def test_fib():
    assert fib(1) == 1       # Base case
    assert fib(5) == 5       # fib(5) = 1, 1, 2, 3, 5
    assert fib(10) == 55     # fib(10) = 55
    assert fib(12) == 144    # fib(12) = 144
    assert fib(20) == 6765   # fib(20) = 6765
    assert fib(0) == 0       # Base case for n = 0

    print("All test cases passed!")



def test_common():
    # Test case 1: Common elements between two lists with some duplicates
    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]

    # Test case 2: Common elements between two lists with smaller numbers
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3]

    # Test case 3: No common elements between two lists
    assert common([10, 20, 30], [40, 50, 60]) == []

    # Test case 4: Common elements with one empty list
    assert common([1, 2, 3], []) == []

    # Test case 5: Common elements with both lists having the same elements
    assert common([1, 2, 3], [1, 2, 3]) == [1, 2, 3]

    # Test case 6: Common elements with one list being a subset of the other
    assert common([1, 2, 3], [2, 3, 4, 5]) == [2, 3]

    print("All test cases passed!")


def test_even_odd_palindrome():
    # Test case 1: Palindromes in the range 1 to 3 (inclusive)
    assert even_odd_palindrome(3) == (1, 2)  # Even palindrome: 2, Odd palindromes: 1, 3

    # Test case 2: Palindromes in the range 1 to 12 (inclusive)
    assert even_odd_palindrome(12) == (4, 6)  # Even palindromes: 2, 4, 6, 8, Odd palindromes: 1, 3, 5, 7, 9, 11

    # Test case 3: Palindromes in the range 1 to 20 (inclusive)
    assert even_odd_palindrome(20) == (4, 8)  # Even palindromes: 2, 4, 6, 8, Odd palindromes: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19

    # Test case 4: Palindromes in the range 1 to 100 (inclusive)
    assert even_odd_palindrome(100) == (10, 18)  # Even palindromes: 2, 4, 6, 8, 22, 44, 66, 88, Odd palindromes: 1, 3, 5, 7, 9, 11, 22, ...

    # Test case 5: Palindromes in the range 1 to 1 (inclusive)
    assert even_odd_palindrome(1) == (0, 1)  # Only one odd palindrome: 1

    # Test case 6: Palindromes in the range 1 to 10 (inclusive)
    assert even_odd_palindrome(10) == (4, 5)  # Even palindromes: 2, 4, 6, 8, Odd palindromes: 1, 3, 5, 7, 9

    print("All test cases passed!")

def test_sum_squares():
    # Test case 1: Basic example
    assert sum_squares([1, 2, 3]) == 6  # 1^2 + 2 + 3^2 = 1 + 2 + 9 = 12

    # Test case 2: Empty list
    assert sum_squares([]) == 0

    # Test case 3: Negative numbers
    assert sum_squares([-1, -5, 2, -1, -5]) == -126  # (-1)^2 + (-5) + 2^2 + (-1)^3 + (-5)^3 = 1 - 5 + 4 - 1 - 125 = -126

    # Test case 4: Mixed positive and negative numbers
    assert sum_squares([1, -2, 3, 4, -5, 6]) == 106  # 1^2 + (-2) + 3^2 + 4^3 + (-5) + 6^2 = 1 - 2 + 9 + 64 - 5 + 36 = 103

    # Test case 5: All indices are multiples of 3 or 4
    assert sum_squares([1, 2, 3, 4]) == 82  # 1^2 + 2^3 + 3^2 + 4^3 = 1 + 8 + 9 + 64 = 82

    # Test case 6: No indices are multiples of 3 or 4
    assert sum_squares([1, 2, 3, 4, 5]) == 15  # 1 + 2 + 3 + 4 + 5 = 15

    # Test case 7: Large numbers
    assert sum_squares([10, 20, 30, 40, 50]) == 1250  # 10^2 + 20 + 30^2 + 40^3 + 50 = 100 + 20 + 900 + 64000 + 50 = 65070

    # Test case 8: Single element list
    assert sum_squares([7]) == 49  # 7^2 = 49

    # Test case 9: List with zero
    assert sum_squares([0, 1, 2, 3, 4]) == 20  # 0^2 + 1 + 2 + 3^2 + 4^3 = 0 + 1 + 2 + 9 + 64 = 76

    print("All test cases passed!")


def test_specialFilter():
    # Test case 1: Basic example
    assert specialFilter([15, -73, 14, -15]) == 1  # Only 15 meets the criteria

    # Test case 2: Multiple valid numbers
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2  # 33 and 109 meet the criteria

    # Test case 3: No valid numbers
    assert specialFilter([10, 20, 30, 40]) == 0  # No numbers meet the criteria

    # Test case 4: All valid numbers
    assert specialFilter([11, 35, 57, 79, 91]) == 5  # All numbers meet the criteria

    # Test case 5: Mixed valid and invalid numbers
    assert specialFilter([13, 25, 37, 49, 50, 61]) == 3  # 13, 37, and 61 meet the criteria

    # Test case 6: Negative numbers and zero
    assert specialFilter([-15, -25, 0, 15, 25]) == 1  # Only 15 meets the criteria

    # Test case 7: Large numbers
    assert specialFilter([12345, 67891, 24680, 13579]) == 2  # 12345 and 13579 meet the criteria

    print("All test cases passed!")



def test_is_bored():
    # Test case 1: No sentences starting with "I"
    assert is_bored("Hello world") == 0

    # Test case 2: One sentence starting with "I"
    assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1

    # Test case 3: Multiple sentences starting with "I"
    assert is_bored("I am happy. You are great! I am bored?") == 2

    # Test case 4: No sentences
    assert is_bored("") == 0

    # Test case 5: Sentences with different delimiters
    assert is_bored("I am here! Are you there? I hope so.") == 2

    # Test case 6: Sentences with leading and trailing whitespace
    assert is_bored("  I am tired. You are not. I need rest! ") == 2

    # Test case 7: Sentences with only "I"
    assert is_bored("I. I! I?") == 3

    # Test case 8: Mixed sentences
    assert is_bored("This is a test. I am testing. Are you ready? I hope so!") == 2
    print("All test cases passed!")



def test_encrypt():
    # Test case 1: Basic example with lowercase letters
    assert encrypt('hi') == 'pm'

    # Test case 2: Longer string with lowercase letters
    assert encrypt('asdfghjkl') == 'iwoznpbts'

    # Test case 3: Short string with lowercase letters
    assert encrypt('gf') == 'on'

    # Test case 4: Short string with lowercase letters
    assert encrypt('et') == 'ma'

    # Test case 5: String with uppercase letters
    assert encrypt('HI') == 'PM'

    # Test case 6: String with mixed case letters
    assert encrypt('Hello World') == 'Pmttw Ewztl'

    # Test case 7: String with special characters and numbers
    assert encrypt('Hello, World! 123') == 'Pmttw, Ewztl! 123'

    # Test case 8: Empty string
    assert encrypt('') == ''

    # Test case 9: String with spaces
    assert encrypt('a b c') == 'i j k'

    # Test case 10: String with all letters in the alphabet
    assert encrypt('abcdefghijklmnopqrstuvwxyz') == 'ijklmnopqrstuvwxyzabcdefgh'

    print("All test cases passed!")



def test_rounded_avg():
    # Test case 1: Basic example with n < m
    assert rounded_avg(1, 5) == "0b11"

    # Test case 2: n is greater than m
    assert rounded_avg(7, 5) == -1

    # Test case 3: Larger range
    assert rounded_avg(10, 20) == "0b1111"

    # Test case 4: Another larger range
    assert rounded_avg(20, 33) == "0b11010"

    # Test case 5: Single number range
    assert rounded_avg(5, 5) == "0b101"

    # Test case 6: Negative numbers
    assert rounded_avg(-5, 5) == "0b0"

    # Test case 7: Negative range with n < m
    assert rounded_avg(-10, -5) == "0b1111111111111111111111111111011"

    # Test case 8: Mixed positive and negative range
    assert rounded_avg(-3, 3) == "0b0"

    # Test case 9: Large numbers
    assert rounded_avg(100, 110) == "0b1101011"

    # Test case 10: Zero range
    assert rounded_avg(0, 0) == "0b0"

    print("All test cases passed!")



def test_minSubArraySum():
    # Test case 1: Basic example with positive numbers
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1

    # Test case 2: Array with all negative numbers
    assert minSubArraySum([-1, -2, -3]) == -6

    # Test case 3: Array with mixed positive and negative numbers
    assert minSubArraySum([1, -2, 3, 10, -1, -5]) == -7

    # Test case 4: Single element array
    assert minSubArraySum([5]) == 5

    # Test case 5: Array with zero
    assert minSubArraySum([0, -1, 2, -3, 4]) == -3

    # Test case 6: Array with all positive numbers
    assert minSubArraySum([1, 2, 3, 4, 5]) == 1

    # Test case 7: Array with large negative numbers
    assert minSubArraySum([-100, -200, -300]) == -600

    # Test case 8: Array with alternating positive and negative numbers
    assert minSubArraySum([1, -1, 1, -1, 1]) == -1

    # Test case 9: Array with a single negative number
    assert minSubArraySum([-5]) == -5

    # Test case 10: Array with a mix of small and large numbers
    assert minSubArraySum([10, -15, 20, -5, 30]) == -15

    print("All test cases passed!")

def test_intersection():
    # Test case 1: Intervals intersect with a prime length
    assert intersection((1, 5), (3, 7)) == "YES"  # Intersection is (3, 5), length is 3 (prime)

    # Test case 2: Intervals intersect with a non-prime length
    assert intersection((1, 6), (4, 8)) == "NO"  # Intersection is (4, 6), length is 3 (prime)

    # Test case 3: Intervals do not intersect
    assert intersection((1, 2), (3, 4)) == "NO"  # No intersection

    # Test case 4: Intervals are identical with a prime length
    assert intersection((1, 3), (1, 3)) == "YES"  # Intersection is (1, 3), length is 3 (prime)

    # Test case 5: Intervals are identical with a non-prime length
    assert intersection((1, 4), (1, 4)) == "NO"  # Intersection is (1, 4), length is 4 (non-prime)

    # Test case 6: One interval is completely within the other with a prime length
    assert intersection((2, 6), (3, 5)) == "YES"  # Intersection is (3, 5), length is 3 (prime)

    # Test case 7: One interval is completely within the other with a non-prime length
    assert intersection((2, 7), (3, 6)) == "NO"  # Intersection is (3, 6), length is 4 (non-prime)

    # Test case 8: Intervals touch at one point
    assert intersection((1, 2), (2, 3)) == "NO"  # Intersection is (2, 2), length is 1 (non-prime)

    # Test case 9: Intervals with negative numbers intersect with a prime length
    assert intersection((-5, -1), (-3, 0)) == "YES"  # Intersection is (-3, -1), length is 3 (prime)

    # Test case 10: Intervals with negative numbers do not intersect
    assert intersection((-5, -3), (-2, 0)) == "NO"  # No intersection

    print("All test cases passed!")



### HARD LEVEL PROBLEMS ###



def total_match(lst1, lst2):
    # Calculate the total number of characters in lst1
    total_chars_lst1 = sum(len(s) for s in lst1)

    # Calculate the total number of characters in lst2
    total_chars_lst2 = sum(len(s) for s in lst2)

    # Compare the totals and return the appropriate list
    if total_chars_lst1 <= total_chars_lst2:
        return lst1
    else:
        return lst2

    print("All test cases passed!")

def test_total_match():
    # Test case 1: lst1 has fewer total characters than lst2
    lst1 = ["apple", "banana"]
    lst2 = ["cherry", "date", "elderberry"]
    assert total_match(lst1, lst2) == lst1, "Test case 1 failed"

    # Test case 2: lst2 has fewer total characters than lst1
    lst1 = ["grapefruit", "honeydew"]
    lst2 = ["kiwi", "lemon"]
    assert total_match(lst1, lst2) == lst2, "Test case 2 failed"

    # Test case 3: lst1 and lst2 have the same total number of characters
    lst1 = ["mango", "nectarine"]
    lst2 = ["orange", "pear"]
    assert total_match(lst1, lst2) == lst1, "Test case 3 failed"

    # Test case 4: Both lists are empty
    lst1 = []
    lst2 = []
    assert total_match(lst1, lst2) == lst1, "Test case 4 failed"

    # Test case 5: lst1 is empty
    lst1 = []
    lst2 = ["apple", "banana"]
    assert total_match(lst1, lst2) == lst1, "Test case 5 failed"

    # Test case 6: lst2 is empty
    lst1 = ["apple", "banana"]
    lst2 = []
    assert total_match(lst1, lst2) == lst1, "Test case 6 failed"

    # Test case 7: lst1 has one element with fewer characters than lst2
    lst1 = ["apple"]
    lst2 = ["banana", "cherry"]
    assert total_match(lst1, lst2) == lst1, "Test case 7 failed"

    # Test case 8: lst2 has one element with fewer characters than lst1
    lst1 = ["banana", "cherry"]
    lst2 = ["apple"]
    assert total_match(lst1, lst2) == lst2, "Test case 8 failed"

    print("All test cases passed!")


def test_will_it_fly():
    # Test case 1: Balanced list with sum less than or equal to the maximum weight
    q1 = [1, 2, 3, 2, 1]
    w1 = 10
    assert will_it_fly(q1, w1) == True, "Test case 1 failed"

    # Test case 2: Unbalanced list
    q2 = [1, 2, 3, 4, 5]
    w2 = 15
    assert will_it_fly(q2, w2) == False, "Test case 2 failed"

    # Test case 3: Balanced list with sum greater than the maximum weight
    q3 = [2, 3, 4, 3, 2]
    w3 = 10
    assert will_it_fly(q3, w3) == False, "Test case 3 failed"




def test_circular_shift():
    # Test case 1: Shift the digits of 12345 by 2 positions to the right
    assert circular_shift(12345, 2) == '45123', f"Test case 1 failed: {circular_shift(12345, 2)}"

    # Test case 2: Shift the digits of 6789 by 5 positions to the right (should reverse the digits)
    assert circular_shift(6789, 5) == '9876', f"Test case 2 failed: {circular_shift(6789, 5)}"

    # Test case 3: Shift the digits of 123456789 by 3 positions to the right
    assert circular_shift(123456789, 3) == '789123456', f"Test case 3 failed: {circular_shift(123456789, 3)}"

    print("All test cases passed!")

def test_reverse_delete():
    # Test case 1: String becomes a palindrome after removing specified characters
    s1 = "racecar"
    c1 = "ae"
    assert reverse_delete(s1, c1) == ("rcr", False)

    # Test case 2: String does not become a palindrome after removing specified characters
    s2 = "hello"
    c2 = "aeiou"
    assert reverse_delete(s2, c2) == ("hll", False)

    # Test case 3: Edge case with an empty string
    s3 = ""
    c3 = "aeiou"
    assert reverse_delete(s3, c3) == ("", True)

    print("All test cases passed!")



from collections import deque
def test_minPath():
    # Test case 1: Simple 2x2 grid with k=2
    grid1 = [
        [1, 2],
        [3, 4]
    ]
    k1 = 2
    expected1 = [1, 2]
    assert minPath(grid1, k1) == expected1, f"Test case 1 failed: expected {expected1}, got {minPath(grid1, k1)}"

    # Test case 2: 3x3 grid with k=3
    grid2 = [
        [5, 6, 7],
        [8, 1, 2],
        [3, 4, 9]
    ]
    k2 = 3
    expected2 = [1, 2, 9]
    assert minPath(grid2, k2) == expected2, f"Test case 2 failed: expected {expected2}, got {minPath(grid2, k2)}"

    # Test case 3: 4x4 grid with k=4
    grid3 = [
        [10, 11, 12, 13],
        [14, 15, 16, 17],
        [18, 19, 20, 21],
        [22, 23, 24, 25]
    ]
    k3 = 4
    expected3 = [10, 11, 12, 13]
    assert minPath(grid3, k3) == expected3, f"Test case 3 failed: expected {expected3}, got {minPath(grid3, k3)}"

    print("All test cases passed!")



def test_move_one_ball():
    # Test case 1: Array is already sorted
    arr1 = [1, 2, 3, 4, 5]
    assert move_one_ball(arr1) == True, "Test case 1 failed"

    # Test case 2: Array can be sorted by moving one element
    arr2 = [3, 4, 5, 1, 2]
    assert move_one_ball(arr2) == True, "Test case 2 failed"

    # Test case 3: Array cannot be sorted by moving one element
    arr3 = [3, 2, 1, 5, 4]
    assert move_one_ball(arr3) == False, "Test case 3 failed"

    print("All test cases passed!")

def test_Strongest_Extension():
    # Test case 1: Basic test with mixed case extensions
    class_name = "ExampleClass"
    extensions = ["ExtensionONE", "extensionTWO", "EXTENSIONthree", "extFOUR"]
    assert Strongest_Extension(class_name, extensions) == "ExampleClass.EXTENSIONthree"

    # Test case 2: All extensions have the same strength
    class_name = "TestClass"
    extensions = ["AbC", "XyZ", "Def"]
    assert Strongest_Extension(class_name, extensions) == "TestClass.AbC"

    # Test case 3: Extensions with varying strengths
    class_name = "SampleClass"
    extensions = ["aBcDeF", "GhIjKl", "mNoPqRs", "TuvWxYz"]
    assert Strongest_Extension(class_name, extensions) == "SampleClass.TuvWxYz"

    print("All test cases passed!")



def test_right_angle_triangle():
    # Test case 1: Known right-angled triangle
    assert right_angle_triangle(3, 4, 5) == True, "Test case 1 failed"

    # Test case 2: Non-right-angled triangle
    assert right_angle_triangle(1, 2, 3) == False, "Test case 2 failed"

    # Test case 3: Another right-angled triangle
    assert right_angle_triangle(5, 12, 13) == True, "Test case 3 failed"

    print("All test cases passed!")





def test_do_algebra():
    # Test case 1: Basic arithmetic operations
    operator1 = ['+', '-', '*']
    operand1 = [2, 3, 4, 5]
    assert do_algebra(operator1, operand1) == 2, "Test case 1 failed"

    # Test case 2: Exponentiation and integer division
    operator2 = ['**', '//']
    operand2 = [2, 3, 4]
    assert do_algebra(operator2, operand2) == 16, "Test case 2 failed"

    # Test case 3: Mixed operations
    operator3 = ['+', '*', '-']
    operand3 = [1, 2, 3, 4]
    assert do_algebra(operator3, operand3) == -1, "Test case 3 failed"

    print("All test cases passed!")



def test_decode_cyclic():
    # Test case 1: String length is a multiple of 3
    encoded_str1 = "bcaefd"
    expected_decoded_str1 = "abcdef"
    assert decode_cyclic(encoded_str1) == expected_decoded_str1, f"Test case 1 failed: {decode_cyclic(encoded_str1)}"

    # Test case 2: String length is not a multiple of 3
    encoded_str2 = "cabdef"
    expected_decoded_str2 = "abcdef"
    assert decode_cyclic(encoded_str2) == expected_decoded_str2, f"Test case 2 failed: {decode_cyclic(encoded_str2)}"

    # Test case 3: Empty string
    encoded_str3 = ""
    expected_decoded_str3 = ""
    assert decode_cyclic(encoded_str3) == expected_decoded_str3, f"Test case 3 failed: {decode_cyclic(encoded_str3)}"

    print("All test cases passed!")








