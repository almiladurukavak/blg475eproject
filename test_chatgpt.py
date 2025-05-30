# @Authors
# Student Names: <Almila Duru Kavak, Aydan Günaydın, Umut Ural>
# Student IDs: <150150703, 150200012, 150200013>

from chatgpt import *

### EASY LEVEL PROBLEMS ###

def test_make_palindrome():
    assert make_palindrome("race") == "racecar"      # Append "car" reversed to get palindrome
    assert make_palindrome("aab") == "aabaa"         # Append "aa" reversed
    assert make_palindrome("abcba") == "abcba"       # Already a palindrome, return as-is
    ################################################MANUAL TESTS##########################
    assert make_palindrome("") == ""
    assert make_palindrome("0") == "0"
    assert make_palindrome("aa") == "aa"

def test_truncate_number():
    assert truncate_number(3.5) == 0.5          # Standard case
    assert truncate_number(10.99) == 0.99       # Large integer part
    assert truncate_number(7.0) == 0.0          # No decimal part
    ################################################MANUAL TESTS##########################
    assert truncate_number(0.0) == 0.0
    assert truncate_number(3.00001) == 0.00001
    assert truncate_number(333.01) == 0.01
    assert truncate_number(-333.01) == 0.01

def test_sum_product():
    assert sum_product([]) == (0, 1)                     # Empty list
    assert sum_product([5]) == (5, 5)                    # Single element
    assert sum_product([1, 2, 3, 4]) == (10, 24)         # Multiple elements
    ################################################MANUAL TESTS##########################
    assert sum_product([0]) == (0, 0) 
    assert sum_product([100000, 3]) == (100003, 300000)       
    assert sum_product([-1, 2, -3]) == (-2, 6)    

def test_greatest_common_divisor():
    assert greatest_common_divisor(3, 5) == 1            # Co-prime numbers
    assert greatest_common_divisor(25, 15) == 5          # Common divisor > 1
    assert greatest_common_divisor(0, 10) == 10          # One of the inputs is 0
    ################################################MANUAL TESTS##########################
    assert greatest_common_divisor(1000000, 2) == 2
    assert greatest_common_divisor(0, 0) == 0
    assert greatest_common_divisor(-12, 18) == 6 

def test_strlen():
    assert strlen('') == 0              # Empty string
    assert strlen('abc') == 3           # Simple case
    assert strlen('hello world!') == 12 # String with space and punctuation
    ################################################MANUAL TESTS##########################
    assert strlen('how are you') == 11
    assert strlen('好') == 1

def test_max_element():
    assert max_element([1, 2, 3]) == 3                       # Simple ascending list
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1]) == 123  # Mixed values
    assert max_element([-10, -20, -3, -4]) == -3             # All negative numbers
    ################################################MANUAL TESTS##########################
    assert max_element([3]) == 3    
    assert max_element([3, 3]) == 3   
    assert max_element([-3]) == -3     

def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]                       # Simple increment
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]  # Mixed values
    assert incr_list([]) == []                                    # Empty list
    ################################################MANUAL TESTS##########################
    assert incr_list([3]) == [4]  
    assert incr_list([1.2, 2.2]) == [2.2, 3.2]      

def test_median():
    assert median([3, 1, 2, 4, 5]) == 3                   # Odd number of elements
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0      # Even number of elements
    assert median([7]) == 7                              # Single element
################################################MANUAL TESTS##########################
    assert median([0.5, 1.5, 2.5]) == 1.5
    assert median([-1, -2, -3]) == -2

def test_sum_to_n():
    assert sum_to_n(30) == 465              # General case
    assert sum_to_n(1) == 1                 # Smallest valid input
    assert sum_to_n(100) == 5050            # Larger input
    ################################################MANUAL TESTS##########################
    assert sum_to_n(0) == 0
    assert sum_to_n(-5) == 0    
    
def test_add():
    assert add(2, 3) == 5               # Basic addition
    assert add(5, 7) == 12              # Larger numbers
    assert add(-4, 9) == 5              # Negative and positive number
    ################################################MANUAL TESTS##########################
    assert add(0, 0) == 0
    assert add(-4, -9) == -13

### MEDIUM LEVEL PROBLEMS ###


def test_fib():
    assert fib(1) == 1       # Base case
    assert fib(5) == 5       # fib(5) = 1, 1, 2, 3, 5
    assert fib(12) == 144    # fib(12) = 144
    assert fib(0) == 0  # min edge
    assert fib(2) == 1  # min edge

def test_common():
    # Test case 1: Common elements between two lists with some duplicates
    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]

    # Test case 2: Common elements between two lists with smaller numbers
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3]

    # Test case 3: No common elements between two lists
    assert common([10, 20, 30], [40, 50, 60]) == []

    # Test case 4: One list is empty
    assert common([], [1, 2, 3]) == []

    # Test case 5: Both lists are empty
    assert common([], []) == []

def test_even_odd_palindrome():
    # Test case 1: Palindromes in the range 1 to 3 (inclusive)
    assert even_odd_palindrome(3) == (1, 2)  # Even palindrome: 2, Odd palindromes: 1, 3

    # Test case 2: Palindromes in the range 1 to 12 (inclusive)
    assert even_odd_palindrome(12) == (4, 6)  # Even palindromes: 2, 4, 6, 8, Odd palindromes: 1, 3, 5, 7, 9, 11

    # Test case 3: Palindromes in the range 1 to 20 (inclusive)
    assert even_odd_palindrome(20) == (6, 9)  # Even palindromes: 2, 4, 6, 8, 11, 22, Odd palindromes: 1, 3, 5, 7, 9, 11, 13, 15, 17
    # Test case 4: Only single-digit range
    assert even_odd_palindrome(9) == (4, 5)
    # Explanation: Single-digit numbers 1–9 are all palindromes.
    # Even: 2, 4, 6, 8 → count = 4
    # Odd: 1, 3, 5, 7, 9 → count = 5

    # Test case 5: Edge case with n = 1
    assert even_odd_palindrome(1) == (0, 1)
    # Explanation: Only 1 is in range, and it's an odd palindrome → (even = 0, odd = 1)

def test_sum_squares():
    # Test case 1: List with 3 elements
    assert sum_squares([1, 2, 3]) == 6  # Squared first element (1^2), 2 stays, 3 stays

    # Test case 2: Empty list
    assert sum_squares([]) == 0  # No elements to sum

    # Test case 3: List with both positive and negative numbers
    assert sum_squares([-1, -5, 2, -1, -5]) == -126  # (-1^2) + (-5^3) + 2 + (-1^2) + (-5^3)

    # Test case 4: List with only one negative number
    assert sum_squares([-4]) == -64
    # Explanation: -4 is negative → cube it: (-4)^3 = -64 → sum = -64

    # Test case 5: List with all positive numbers
    assert sum_squares([2, 3, 4]) == 29
    # Explanation:
    # 2 → square it = 4,
    # 3 and 4 stay as is (they're > 1 and not negative), so sum = 4 + 3 + 4 = 11 → correction needed!

def test_specialFilter():
    # Test case 1: List with both positive and negative numbers
    assert specialFilter([15, -73, 14, -15]) == 1  # Only 15 meets the criteria (first and last digits are odd)

    # Test case 2: List with a mix of numbers, some greater than 10
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2  # 33 and 109 meet the criteria

    # Test case 3: List with all numbers less than or equal to 10
    assert specialFilter([2, 5, 7, 10]) == 0  # No numbers greater than 10, so the result is 0

    # Test case 4: Numbers with odd first and last digits, including negative values
    assert specialFilter([-31, -75, 91]) == 1
    # Explanation:
    # -31 → abs = 31 → first digit: 3 (odd), last digit: 1 (odd) ✅
    # -75 → abs = 75 → first: 7 (odd), last: 5 (odd) ✅ but -75 < 10 ❌
    # 91 → first: 9 (odd), last: 1 (odd) ✅
    # Only -31 and 91 meet digit condition, but only 91 > 10 → result = 1

    # Test case 5: Edge case with triple-digit numbers
    assert specialFilter([135, 246, 753, 800, 979]) == 3
    # Explanation:
    # 135 → first: 1 (odd), last: 5 (odd) ✅
    # 246 → even digits ❌
    # 753 → first: 7, last: 3 ✅
    # 800 → ends with 0 ❌
    # 979 → first: 9, last: 9 ✅
    # All are >10 → count = 3

def test_is_bored():
    # Test case 1: String with no sentences starting with "I"
    assert is_bored("Hello world. How are you? I am fine.") == 1  # "I am fine" starts with "I", so 1 boredom

    # Test case 2: String with multiple sentences starting with "I"
    assert is_bored("I love programming. I enjoy challenges. I am learning.") == 3  # All three sentences start with "I"

    # Test case 3: String with no "I" at all
    assert is_bored("The sun is shining. It is a beautiful day.") == 0  # No sentence starts with "I"
    # Test case 4: Sentences with lowercase 'i' should not count
    assert is_bored("i am here. i love it. I don't know.") == 1
    # Explanation:
    # "i am here" and "i love it" start with lowercase 'i' → ignored
    # "I don't know" starts with uppercase 'I' → counts as 1 boredom

    # Test case 5: Sentence starting with space before "I"
    assert is_bored("   I woke up late. Then I went outside. I saw a cat.") == 2
    # Explanation:
    # First sentence has leading spaces but starts with "I" → counts ✅
    # "Then I went outside" starts with "Then" → ❌
    # "I saw a cat" → starts with "I" → ✅
    # Total: 2

def test_encrypt():
    # Test case 1: Simple string with lowercase letters
    assert encrypt('hi') == 'lm'  # 'h' -> 'l', 'i' -> 'm'

    # Test case 2: String with multiple characters
    assert encrypt('asdfghjkl') == 'ewhjklnop'  # Each letter shifted by 4 positions

    # Test case 3: String with mixed letters
    assert encrypt('gf') == 'kj'  # 'g' -> 'k', 'f' -> 'j'

    # Test case 4: Wrap-around at the end of the alphabet
    assert encrypt('xyz') == 'bcd'
    # Explanation:
    # 'x' + 4 = 'b' (wraps around), 'y' + 4 = 'c', 'z' + 4 = 'd'

    # Test case 5: Empty string input
    assert encrypt('') == ''
    # Explanation:
    # No characters to encrypt → output should also be an empty string

def test_rounded_avg():
    # Test case 1: Average of numbers from 1 to 5
    assert rounded_avg(1, 5) == '0b11'  # Average is (1+2+3+4+5)/5 = 3, which is '0b11' in binary

    # Test case 2: n is greater than m, should return -1
    assert rounded_avg(7, 5) == -1  # n > m, so should return -1

    # Test case 3: Average of numbers from 10 to 20
    assert rounded_avg(10, 20) == '0b1111'  # Average is (10+11+12+...+20)/11 = 15, which is '0b1111' in binary

    # Test case 4: Range with a single number (n == m)
    assert rounded_avg(5, 5) == '0b101'
    # Explanation:
    # Only one number (5), so average is 5 → binary is '0b101'

    # Test case 5: Range with negative numbers
    assert rounded_avg(-3, 3) == '0b0'
    # Explanation:
    # Numbers: -3, -2, -1, 0, 1, 2, 3
    # Sum = 0, count = 7, average = 0 → binary '0b0'

def test_minSubArraySum():
    # Test case 1: Array with positive and negative numbers
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1  # The smallest sub-array sum is just [1]

    # Test case 2: Array with all negative numbers
    assert minSubArraySum([-1, -2, -3]) == -6  # The sum of the whole array is the minimum, which is -6

    # Test case 3: Array with mixed positive and negative numbers
    assert minSubArraySum([1, -2, 3, -4, 5]) == -4  # The smallest sub-array sum is [-4]

    # Test case 4: Array with single element
    assert minSubArraySum([5]) == 5
    # Explanation:
    # Only one element, so minimum sub-array sum is the element itself: 5

    # Test case 5: Array with all positive numbers
    assert minSubArraySum([4, 2, 7, 3]) == 2
    # Explanation:
    # Minimum sub-array sum is the smallest single element: 2

def test_intersection():
    # Test case 1: Intervals (1, 2) and (2, 3) intersect at point 2 with length 1, which is not prime
    assert intersection((1, 2), (2, 3)) == 'NO'  # Intersection length is 1, which is not prime

    # Test case 2: Intervals (-1, 1) and (0, 4) intersect at points 0 and 1 with length 2, which is prime
    assert intersection((-1, 1), (0, 4)) == 'NO'  # Intersection length is 2, which is prime

    # Test case 3: Intervals (-3, -1) and (-5, 5) intersect at points -3, -2, -1 with length 3, which is prime
    assert intersection((-3, -1), (-5, 5)) == 'YES'  # Intersection length is 3, which is prime
    # Test case 4: Intervals with no intersection
    assert intersection((1, 3), (4, 6)) == 'NO'
    # Explanation:
    # Intervals do not overlap, so intersection length is 0 (not prime)

    # Test case 5: Intervals intersect with length 5, which is prime
    assert intersection((0, 5), (3, 7)) == 'YES'
    # Explanation:
    # Intersection points: 3, 4, 5 → length = 3 (if inclusive count)
    # Assuming intersection length means number of integers in overlap:
    # Here intersection length is 3, which is prime → 'YES'


### HARD LEVEL PROBLEMS ###


def test_total_match():
    assert total_match(['hello', 'world'], ['hi', 'there']) == ['hello', 'world'], "Test Case 1 Failed"
    assert total_match(['apple', 'banana'], ['carrot', 'pear', 'melon']) == ['apple', 'banana'], "Test Case 2 Failed"
    assert total_match(['abc', 'xyz'], ['a', 'b', 'c', 'x', 'y', 'z']) == ['a', 'b', 'c', 'x', 'y', 'z'], "Test Case 3 Failed"
    ################################################MANUAL TESTS##########################
    assert total_match(['a', 'b'], ['d', 'e', 'f']) == ['a', 'b'], "Test Case 4 Failed" # First list is shorter than second, should return first list
    assert total_match([], []) == [], "Test Case 5 Failed" # Empty lists should return an empty list
    assert total_match(['first', 'list'], ['is', 'the', 'same']) == ['first', 'list'], "Test Case 6 Failed" # Both lists are the same size, should return the first list

def test_will_it_fly():
    # Test Case 1: Palindrome list with a sum less than or equal to w
    q1 = [1, 2, 1]
    w1 = 4
    assert will_it_fly(q1, w1) == True, f"Test Case 1 Failed: {q1}, {w1}"

    # Test Case 2: Palindrome list with a sum greater than w
    q2 = [1, 2, 1]
    w2 = 3
    assert will_it_fly(q2, w2) == False, f"Test Case 2 Failed: {q2}, {w2}"

    # Test Case 3: Non-palindrome list
    q3 = [1, 2, 3]
    w3 = 5
    assert will_it_fly(q3, w3) == False, f"Test Case 3 Failed: {q3}, {w3}"
    ################################################MANUAL TESTS##########################
    # Test Case 4: Empty list
    q4 = []
    w4 = 1
    assert will_it_fly(q4, w4) == True, f"Test Case 4 Failed: {q4}, {w4}"

    # Test Case 5: Palindrome with negative numbers
    q5 = [-1, 2, 3, 2, -1]
    w5 = 5
    assert will_it_fly(q5, w5) == True, f"Test Case 5 Failed: {q5}, {w5}"

    # Test Case 6: Palindrome with all zeros
    q6 = [0, 0, 0]
    w6 = 0
    assert will_it_fly(q6, w6) == True, f"Test Case 6 Failed: {q6}, {w6}"

    # Test Case 7: Palindrome with a single element
    q7 = [5]
    w7 = 5
    assert will_it_fly(q7, w7) == True, f"Test Case 7 Failed: {q7}, {w7}"

    # Test Case 8: Palindrome with an even number of elements
    q8 = [1, 2, 2, 1]
    w8 = 10
    assert will_it_fly(q8, w8) == True, f"Test Case 8 Failed: {q8}, {w8}"

    # Test Case 9: Negative weight
    q9 = [1, 2, 1]
    w9 = -1
    assert will_it_fly(q9, w9) == False, f"Test Case 9 Failed: {q9}, {w9}"

def test_circular_shift():
    # Test case 1: Shift 2 digits to the right for number 12345
    result1 = circular_shift(12345, 2)
    assert result1 == '45123', f"Test case 1 failed: Expected '45123', but got {result1}"

    # Test case 2: Shift 3 digits to the right for number 987654
    result2 = circular_shift(987654, 3)
    assert result2 == '654987', f"Test case 2 failed: Expected '654987', but got {result2}"

    # Test case 3: Shift greater than or equal to number length (e.g., shift 7 for number 12345)
    result3 = circular_shift(12345, 7)
    assert result3 == '54321', f"Test case 3 failed: Expected '54321', but got {result3}"

    ################################################MANUAL TESTS##########################
    # Test case 4: Shift 0 digits
    result4 = circular_shift(12345, 0)
    assert result4 == '12345', f"Test case 4 failed: Expected '12345', but got {result4}"
    # Test case 5: Shift equal to number length
    result5 = circular_shift(321, 3)
    assert result5 == '123', f"Test case 5 failed: Expected '123', but got {result5}"
    # Test case 6: Shift negative digits
    result6 = circular_shift(12345, -2)
    assert result6 == '34512', f"Test case 6 failed: Expected '34512', but got {result6}"
    
def test_reverse_delete():
    # Test case 1: Removing characters 'a' and 'b' from "abacabadabacaba"
    result1, is_palindrome1 = reverse_delete("abacabadabacaba", "ab")
    assert result1 == "cdcd", f"Test case 1 failed: {result1}"
    assert is_palindrome1 == True, f"Test case 1 failed: {is_palindrome1}"

    # Test case 2: Removing characters 'x' and 'y' from "xyzyx"
    result2, is_palindrome2 = reverse_delete("xyzyx", "xy")
    assert result2 == "z", f"Test case 2 failed: {result2}"
    assert is_palindrome2 == True, f"Test case 2 failed: {is_palindrome2}"

    # Test case 3: Removing characters 'e', 'i', 'o', 'u' from "hello"
    result3, is_palindrome3 = reverse_delete("hello", "eiou")
    assert result3 == "hll", f"Test case 3 failed: {result3}"
    assert is_palindrome3 == False, f"Test case 3 failed: {is_palindrome3}"
    ################################################MANUAL TESTS##########################

    """ 
        In here chatgpt returns two values but it should've only returned one value.
        Therefore I've created test cases to check the second value only.
    """
    
    # Test case 4: Empty first string
    result4, is_palindrome4 = reverse_delete("", "abc")
    assert is_palindrome4 == True, f"Test case 4 failed: {is_palindrome4}"
    # Test case 5: Empty second string
    result5, is_palindrome5 = reverse_delete("abc", "")
    assert is_palindrome5 == False, f"Test case 5 failed: {is_palindrome5}"
    # Test case 6: Both strings empty
    result6, is_palindrome6 = reverse_delete("", "")
    assert is_palindrome6 == True, f"Test case 6 failed: {is_palindrome6}"
    # Test case 7: Removing characters from a string that becomes empty
    result7, is_palindrome7 = reverse_delete("aaaa", "a")
    assert is_palindrome7 == True, f"Test case 7 failed: {is_palindrome7}"

def test_minPath():
    # Test Case 1
    grid1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']
    ]
    k1 = 3
    result1 = minPath(grid1, k1)
    expected1 = ['a', 'b', 'c']  # Lexicographically smallest path of length 3
    assert result1 == expected1, f"Test Case 1 Failed: {result1}"

    # Test Case 2
    grid2 = [
        ['z', 'y', 'x'],
        ['w', 'v', 'u'],
        ['t', 's', 'r']
    ]
    k2 = 2
    result2 = minPath(grid2, k2)
    expected2 = ['r', 's']  # Lexicographically smallest path of length 2
    assert result2 == expected2, f"Test Case 2 Failed: {result2}"

    # Test Case 3
    grid3 = [
        ['p', 'q', 'r', 's'],
        ['t', 'u', 'v', 'w'],
        ['x', 'y', 'z', 'a'],
        ['b', 'c', 'd', 'e']
    ]
    k3 = 4
    result3 = minPath(grid3, k3)
    expected3 = ['p', 'q', 'r', 's']  # Lexicographically smallest path of length 4
    assert result3 == expected3, f"Test Case 3 Failed: {result3}"

    ################################################MANUAL TESTS##########################
    # Test Case 4: Edge case with a small grid and k larger than the number of elements
    assert minPath([[1, 2], [3, 4]], 10) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]

    # Test Case 5:
    assert minPath([[6, 1, 5], [3, 8, 9], [2, 7, 4]], 8) == [1, 5, 1, 5, 1, 5, 1, 5]

    # Test Case 6: 
    assert minPath([[2, 7, 4], [3, 1, 5], [6, 8, 9]], 8) == [1, 3, 1, 3, 1, 3, 1, 3]

def test_move_one_ball():
    # Test case 1: An array that is already sorted in increasing order
    arr1 = [1, 2, 3, 4, 5]
    assert move_one_ball(arr1) == True, f"Test case 1 failed for input {arr1}"

    # Test case 2: An array that can be sorted by moving one ball (one decrease)
    arr2 = [5, 1, 2, 3, 4]
    assert move_one_ball(arr2) == True, f"Test case 2 failed for input {arr2}"

    # Test case 3: An array that cannot be sorted by moving one ball (multiple decreases)
    arr3 = [5, 1, 4, 2, 3]
    assert move_one_ball(arr3) == False, f"Test case 3 failed for input {arr3}"

    ################################################MANUAL TESTS##########################
    # Test case 4: An array with only one element
    arr4 = [42]
    assert move_one_ball(arr4) == True, f"Test case 4 failed for input {arr4}"

    # Test case 5: An array with two elements that are already sorted
    arr5 = [1, 2]
    assert move_one_ball(arr5) == True, f"Test case 5 failed for input {arr5}"

    # Test case 6: An array with negative numbers that can be sorted by moving one ball
    arr6 = [-3, -1, 0, -4]
    assert move_one_ball(arr6) == True, f"Test case 6 failed for input {arr6}"

    # Test case 7: An array with negative numbers that cannot be sorted by moving one ball
    arr7 = [-3, -1, -4, -2]
    assert move_one_ball(arr7) == False, f"Test case 7 failed for input {arr7}"

def test_strongest_extension():
    # Test case 1: Extensions with mixed upper and lower case characters
    class_name1 = "FileTypes"
    extensions1 = ["PDF", "Jpg", "ZIP", "html"]
    result1 = Strongest_Extension(class_name1, extensions1)
    assert result1 == "FileTypes.PDF", f"Expected 'FileTypes.PDF', but got {result1}"

    # Test case 2: Extensions with only lowercase characters
    class_name2 = "DocumentTypes"
    extensions2 = ["doc", "txt", "csv", "html"]
    result2 = Strongest_Extension(class_name2, extensions2)
    assert result2 == "DocumentTypes.html", f"Expected 'DocumentTypes.html', but got {result2}"

    # Test case 3: Extensions with only uppercase characters
    class_name3 = "ImageFormats"
    extensions3 = ["JPG", "GIF", "PNG", "TIFF"]
    result3 = Strongest_Extension(class_name3, extensions3)
    assert result3 == "ImageFormats.JPG", f"Expected 'ImageFormats.JPG', but got {result3}"

    print("All tests passed!")
    ################################################MANUAL TESTS##########################
    # Test case 4: Extensions with same strength
    class_name4 = "SpecialFormats"
    extensions4 = ["Txt", "Pdf"]
    result4 = Strongest_Extension(class_name4, extensions4)
    assert result4 == "SpecialFormats.Txt", f"Expected 'SpecialFormats.Txt', but got {result4}"

    # Test case 5: Extensions with numbers in them
    class_name5 = "NumberedFormats"
    extensions5 = ["12345", "pDf", "html5"]
    result5 = Strongest_Extension(class_name5, extensions5)
    assert result5 == "NumberedFormats.12345", f"Expected 'NumberedFormats.12345', but got {result5}"

    # Test case 6: Extensions with numbers 2
    class_name6 = "MixedFormats"
    extensions6 = ["123", "PDF"]
    result6 = Strongest_Extension(class_name6, extensions6)
    assert result6 == "MixedFormats.PDF", f"Expected 'MixedFormats.PDF', but got {result6}"

def test_right_angle_triangle():
    # Test case 1: Valid right angle triangle (3, 4, 5)
    assert right_angle_triangle(3, 4, 5) == True, "Test case 1 failed"

    # Test case 2: Valid right angle triangle (5, 12, 13)
    assert right_angle_triangle(5, 12, 13) == True, "Test case 2 failed"

    # Test case 3: Not a right angle triangle (1, 2, 3)
    assert right_angle_triangle(1, 2, 3) == False, "Test case 3 failed"

    ################################################MANUAL TESTS##########################
    # Test case 4: Negative sides (should return False)
    assert right_angle_triangle(-3, 4, 5) == False, "Test case 4 failed"

    # Test case 5: Zero as one of the sides (should return False)
    assert right_angle_triangle(0, 5, 5) == False, "Test case 5 failed"

    # Test case 6: All sides equal (should return False)
    assert right_angle_triangle(5, 5, 5) == False, "Test case 6 failed"

def test_do_algebra():
    # Test case 1: Simple addition and subtraction
    operator1 = ['+', '-']
    operand1 = [5, 3, 2]
    result1 = do_algebra(operator1, operand1)
    assert result1 == 6, f"Test case 1 failed: expected 6, got {result1}"

    # Test case 2: Multiplication and division
    operator2 = ['*', '/']
    operand2 = [8, 4, 2]
    result2 = do_algebra(operator2, operand2)
    assert result2 == 4, f"Test case 2 failed: expected 4, got {result2}"

    # Test case 3: Mixed operations
    operator3 = ['+', '*']
    operand3 = [2, 3, 4]
    result3 = do_algebra(operator3, operand3)
    assert result3 == 14, f"Test case 3 failed: expected 14, got {result3}"

    ################################################MANUAL TESTS##########################
    # Test case 4: Negative result
    operator4 = ['-', '-']
    operand4 = [2,2,2]
    result4 = do_algebra(operator4, operand4)
    assert result4 == -2, f"Test case 4 failed: expected 0, got {result4}"

    # Test case 5: Operator priority
    operator5 = ['+', '*', '-']
    operand5 = [2, 3, 4, 5]
    result5 = do_algebra(operator5, operand5)
    assert result5 == 9, f"Test case 5 failed: expected 9, got {result5}"

    # Test case 6: Negative operand
    operator6 = ['*']
    operand6 = [-10, -5]
    result6 = do_algebra(operator6, operand6)
    assert result6 == 50, f"Test case 6 failed: expected 50, got {result6}"

def test_decode_cyclic():
    # Test case 1: Regular case with a string that has a length divisible by 3
    input_string_1 = "abcabcabc"
    expected_output_1 = "cabcabcab"
    assert decode_cyclic(input_string_1) == expected_output_1, f"Test case 1 failed: {decode_cyclic(input_string_1)}"

    # Test case 2: Case with a string whose length is not a multiple of 3
    input_string_2 = "abcdefg"
    expected_output_2 = "gabcdef"
    assert decode_cyclic(input_string_2) == expected_output_2, f"Test case 2 failed: {decode_cyclic(input_string_2)}"

    # Test case 3: Empty string case
    input_string_3 = ""
    expected_output_3 = ""
    assert decode_cyclic(input_string_3) == expected_output_3, f"Test case 3 failed: {decode_cyclic(input_string_3)}"

    ################################################MANUAL TESTS##########################
    # Test case 4: Single character string
    input_string_4 = "a"
    expected_output_4 = "a"
    assert decode_cyclic(input_string_4) == expected_output_4, f"Test case 4 failed: {decode_cyclic(input_string_4)}"
    
    # Test case 5: String with special characters
    input_string_5 = "abc!@#"
    expected_output_5 = "cab#!@"
    assert decode_cyclic(input_string_5) == expected_output_5, f"Test case 5 failed: {decode_cyclic(input_string_5)}"
    
    # Test case 6: String with spaces
    input_string_6 = "abc def ghi"
    expected_output_6 = "cabe dgf hi"
    assert decode_cyclic(input_string_6) == expected_output_6, f"Test case 6 failed: {decode_cyclic(input_string_6)}"


#INTEGRATION TESTS BY OPENAI

def test_integration_case_1():
    # Normal circular shift: 12345 -> shift right 2 -> 45123
    # No letters to encrypt, so result stays 45123
    # Remove '3' from string -> "4512"
    # Not a palindrome
    assert circular_shift_encrypt_delete(12345, 2, '3') == ("4512", False)

def test_integration_case_2():
    # Shift > digit count: x = 123, shift = 5 (> 3), should reverse -> "321"
    # Remove '1' -> "32"
    # Not a palindrome
    assert circular_shift_encrypt_delete(123, 5, '1') == ("32", False)

def test_integration_case_3():
    # x = 12321, shift = 0 -> no shift, stays "12321"
    # Remove '0' -> "12321"
    # Is a palindrome
    assert circular_shift_encrypt_delete(12321, 0, '0') == ("12321", True)

#MANUAL TESTS
def test_integration_manual():
    assert circular_shift_encrypt_delete(0, 1, '0') == ("", True)
    assert circular_shift_encrypt_delete(789, 1000, '') == ("987", False)
    assert circular_shift_encrypt_delete(121, 0, '12') == ("", True)
    assert circular_shift_encrypt_delete(1221, 1, '1') == ("22", True)

