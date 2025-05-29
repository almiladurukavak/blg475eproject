# @Authors
# Student Names: <Almila Duru Kavak, Aydan Günaydın, Umut Ural>
# Student IDs: <150150703, 150200012 150200013>

### EASY LEVEL PROBLEMS ###
# make_palindrome (task_id: HumanEval/10)

#HUMANEVAL PROMPT RESULT
# def is_palindrome(string: str) -> bool:
#     """Test if given string is a palindrome"""
#     return string == string[::-1]

# def make_palindrome(string: str) -> str:
#     """Find the shortest palindrome that begins with a supplied string.
#     Algorithm idea is simple:
#     - Find the longest postfix of supplied string that is a palindrome.
#     - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
#     """
#     if not string:
#         return string

#     # Find the longest palindromic suffix
#     for i in range(len(string)):
#         if is_palindrome(string[i:]):
#             # The prefix that comes before the palindromic suffix
#             prefix = string[:i]
#             # Reverse the prefix and append it to the end of the string
#             return string + prefix[::-1]

#     return string

#updated prompt

# def is_palindrome(string: str) -> bool:
# """ Test if given string is a palindrome """
# return string == string[::-1]


# def make_palindrome(string: str) -> str:
# """ Find the shortest palindrome that begins with a supplied string.
# Algorithm idea is simple:
# - Find the longest postfix of supplied string that is a palindrome.
# - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
# >>> make_palindrome('')
# ''
# >>> make_palindrome('cat')
# 'catac'
# >>> make_palindrome('cata')
# 'catac'
# """

# if is_palindrome condition is true, directly return the string
#resulting function

def is_palindrome(string: str) -> bool:
    """Test if given string is a palindrome"""
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if is_palindrome(string):
        return string

    # Find the longest palindromic suffix
    n = len(string)
    for i in range(n):
        substring = string[i:]
        if is_palindrome(substring):
            # Append the reverse of the prefix before the palindromic suffix
            return string + string[:i][::-1]

    return string + string[:-1][::-1]


# truncate_number (task_id: HumanEval/2)
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Ensure the number is positive
    if number < 0:
        raise ValueError("The number must be positive")

    # Extract the decimal part
    decimal_part = number - int(number)
    return decimal_part

# sum_product (task_id: HumanEval/8)
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    if not numbers:
        return (0, 1)

    total_sum = sum(numbers)
    total_product = 1
    for number in numbers:
        total_product *= number

    return (total_sum, total_product)

# greatest_common_divisor (task_id: HumanEval/13)
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b != 0:
        a, b = b, a % b
    return a

# strlen (task_id: HumanEval/23)
def strlen(string: str) -> int:
    """
    Return the length of the given string.
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# max_element (task_id: HumanEval/35)
def max_element(l: list) -> int:
    """
    Return the maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not l:
        raise ValueError("The list is empty")

    return max(l)

# incr_list (task_id: HumanEval/42)
def incr_list(l: list) -> list:
    return [x + 1 for x in l]

# median (task_id: HumanEval/47)
def median(l: list) -> float:
    if not l:
        raise ValueError("The list is empty")

    sorted_list = sorted(l)
    n = len(sorted_list)
    mid = n // 2

    if n % 2 == 1:
        return float(sorted_list[mid])
    else:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2

# sum_to_n (task_id: HumanEval/60)
def sum_to_n(n: int) -> int:
    if n < 1:
        raise ValueError("n must be a positive integer")

    return n * (n + 1) // 2

# add (task_id: HumanEval/53)

def add(x: int, y: int) -> int:
    return x + y

### MEDIUM LEVEL PROBLEMS ###


#fib (task_id: HumanEval/55)
def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Test cases
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21


#common (task_id: HumanEval/58)

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    # Convert lists to sets to remove duplicates and find the intersection
    set1 = set(l1)
    set2 = set(l2)
    common_elements = set1.intersection(set2)

    # Convert the set back to a list and sort it
    sorted_common_elements = sorted(common_elements)

    return sorted_common_elements



#even_odd_palindrome (task_id: HumanEval/107)

def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:
    Input: 3
    Output: (1, 2)
    Explanation:
    Integer palindromes are 1, 2, 3. One of them is even, and two of them are odd.

    Example 2:
    Input: 12
    Output: (4, 6)
    Explanation:
    Integer palindromes are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. Four of them are even, and 6 of them are odd.

    Note:
    1. 1 <= n <= 10^3
    2. Returned tuple has the number of even and odd integer palindromes respectively.
    """
    even_count = 0
    odd_count = 0

    for num in range(1, n + 1):
        num_str = str(num)
        if num_str == num_str[::-1]:  # Check if the number is a palindrome
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    return (even_count, odd_count)



#sum_squares (task_id: HumanEval/142)

def sum_squares(lst):
    """
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries.

    Examples:
    For lst = [1, 2, 3] the output should be 6
    For lst = [] the output should be 0
    For lst = [-1, -5, 2, -1, -5] the output should be -126
    """
    modified_list = []

    for index, value in enumerate(lst):
        if index % 3 == 0:
            modified_list.append(value ** 2)
        elif index % 4 == 0:
            modified_list.append(value ** 3)
        else:
            modified_list.append(value)

    return sum(modified_list)



#specialFilter (task_id: HumanEval/146)

def specialFilter(nums):
    """
    Write a function that takes an array of numbers as input and returns
    the number of elements in the array that are greater than 10 and both
    first and last digits of a number are odd (1, 3, 5, 7, 9).

    For example:
    specialFilter([15, -73, 14, -15]) => 1
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    def is_odd_digit(digit):
        return digit in {'1', '3', '5', '7', '9'}

    count = 0
    for num in nums:
        if num > 10:
            num_str = str(num)
            if is_odd_digit(num_str[0]) and is_odd_digit(num_str[-1]):
                count += 1

    return count



#is_bored (task_id: HumanEval/91)

import re

def is_bored(S):
    """
    Count the number of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.

    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    # Split the string into sentences using regex
    sentences = re.split(r'[.?!]', S)

    # Initialize the boredom count
    boredom_count = 0

    # Iterate through each sentence
    for sentence in sentences:
        # Trim whitespace and check if the sentence starts with "I"
        trimmed_sentence = sentence.strip()
        if trimmed_sentence.split()[0] == "I":
            boredom_count += 1

    return boredom_count



#encrypt (task_id: HumanEval/89)

def encrypt(s):
    """
    Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated.
    The alphabet should be rotated in a manner such that the letters
    shift down by eight places.

    For example:
    encrypt('hi') returns 'pm'
    encrypt('asdfghjkl') returns 'iwoznpbts'
    encrypt('gf') returns 'on'
    encrypt('et') returns 'ma'
    """
    def shift_char(c, shift):
        if 'a' <= c <= 'z':
            return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            return chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        else:
            return c

    shift = 8
    return ''.join(shift_char(c, shift) for c in s)


#rounded_avg (task_id: HumanEval/103)

def rounded_avg(n, m):
    """
    Compute the average of the integers from n through m (including n and m),
    round the answer to the nearest integer, and convert that to binary.
    If n is greater than m, return -1.

    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    if n > m:
        return -1

    # Calculate the sum of the range
    num_terms = m - n + 1
    total_sum = (num_terms * (n + m)) // 2

    # Calculate the average
    average = total_sum / num_terms

    # Round the average to the nearest integer
    rounded_average = round(average)

    # Convert to binary
    binary_representation = bin(rounded_average)

    return binary_representation

#minSubArraySum (task_id: HumanEval/114)


def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.

    Example:
    >>> minSubArraySum([2, 3, 4, 1, 2, 4])
    1
    >>> minSubArraySum([-1, -2, -3])
    -6
    """
    min_ending_here = min_so_far = nums[0]
    for num in nums[1:]:
        min_ending_here = min(num, min_ending_here + num)
        min_so_far = min(min_so_far, min_ending_here)
    return min_so_far




#intersection (task_id: HumanEval/127)

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def intersection(interval1, interval2):
    """Determine if the length of the intersection of two intervals is a prime number."""
    start1, end1 = interval1
    start2, end2 = interval2

    # Calculate the intersection
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)

    # Check if the intervals intersect
    if intersection_start > intersection_end:
        return "NO"

    # Calculate the length of the intersection
    length = intersection_end - intersection_start + 1

    # Check if the length is a prime number
    if is_prime(length):
        return "YES"
    else:
        return "NO"



### HARD LEVEL PROBLEMS ###

# total_match (task_id: HumanEval/74)
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

    print("All test cases passed!")

# will_it_fly (task_id: HumanEval/72)
def will_it_fly(q, w):
    # Check if the list is balanced (palindromic)
    if q != q[::-1]:
        return False

    # Check if the sum of the elements is less than or equal to the maximum weight
    if sum(q) > w:
        return False

    # If both conditions are met, the object will fly
    return True
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

# circular_shift (task_id: HumanEval/65)
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """
    # Convert the integer to a string to manipulate its digits
    x_str = str(x)
    num_digits = len(x_str)

    # If shift is greater than the number of digits, return the digits reversed
    if shift > num_digits:
        return x_str[::-1]

    # Perform the circular shift
    shift = shift % num_digits  # In case shift is greater than the number of digits
    shifted_str = x_str[-shift:] + x_str[:-shift]

    return shifted_str
def test_circular_shift():
    # Test case 1: Shift the digits of 12345 by 2 positions to the right
    assert circular_shift(12345, 2) == '45123', f"Test case 1 failed: {circular_shift(12345, 2)}"

    # Test case 2: Shift the digits of 6789 by 5 positions to the right (should reverse the digits)
    assert circular_shift(6789, 5) == '9876', f"Test case 2 failed: {circular_shift(6789, 5)}"

    # Test case 3: Shift the digits of 123456789 by 3 positions to the right
    assert circular_shift(123456789, 3) == '789123456', f"Test case 3 failed: {circular_shift(123456789, 3)}"

    print("All test cases passed!")

# reverse_delete (task_id: HumanEval/112)
def reverse_delete(s, c):
    # Step 1: Remove all characters from s that are in c
    result = ''.join([char for char in s if char not in c])

    # Step 2: Check if the result string is a palindrome
    is_palindrome = (result == result[::-1])

    # Step 3: Return the result string and the palindrome check
    return (result, is_palindrome)
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

# minPath (task_id: HumanEval/129)
from collections import deque
def minPath(grid, k):
    N = len(grid)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    def is_valid(x, y):
        return 0 <= x < N and 0 <= y < N

    min_path = None

    for i in range(N):
        for j in range(N):
            queue = deque([(i, j, [grid[i][j]])])

            while queue:
                x, y, path = queue.popleft()

                if len(path) == k:
                    if min_path is None or tuple(path) < tuple(min_path):
                        min_path = path
                    continue

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if is_valid(nx, ny):
                        queue.append((nx, ny, path + [grid[nx][ny]]))

    return min_path
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

# move_one_ball (task_id: HumanEval/109)
def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True

    n = len(arr)

    # Check if the array is already sorted
    if arr == sorted(arr):
        return True

    # Find the point where the array can be split
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            # Rotate the array at this point
            rotated_arr = arr[i:] + arr[:i]
            # Check if the rotated array is sorted
            if rotated_arr == sorted(rotated_arr):
                return True
            else:
                return False

    # If no such point is found, return False
    return False
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

# Strongest_Extension (task_id: HumanEval/153)
def Strongest_Extension(class_name, extensions):
    def calculate_strength(extension):
        CAP = sum(1 for char in extension if char.isupper())
        SM = sum(1 for char in extension if char.islower())
        return CAP - SM

    strongest_extension = extensions[0]
    max_strength = calculate_strength(strongest_extension)

    for extension in extensions[1:]:
        strength = calculate_strength(extension)
        if strength > max_strength:
            strongest_extension = extension
            max_strength = strength

    return f"{class_name}.{strongest_extension}"
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

""" 

This is the old version of the right_angle_triangle function.

,# right_angle_triangle (task_id: HumanEval/157)
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    # Sort the sides so that the largest side is always compared as the hypotenuse
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2 """

""" 
    This is the new version of the right_angle_triangle function with the prompt:

    def right_angle_triangle(a, b, c):
        '''
        Given the lengths of the three sides of a triangle. Return True if the three
        sides form a right-angled triangle also make sure that the values don't break the triangle inequality, return False otherwise.
        A right-angled triangle is a triangle in which one angle is right angle or
        90 degree.
        Example:
        right_angle_triangle(3, 4, 5) == True
        right_angle_triangle(1, 2, 3) == False
        '''

 """
def right_angle_triangle(a, b, c):
    # Check the triangle inequality theorem
    sides = sorted([a, b, c])
    if sides[0] + sides[1] <= sides[2]:
        return False

    # Check the Pythagorean theorem
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False


"""  

This is the old version of the do_algebra function.

do_algebra (task_id: HumanEval/160)
def do_algebra(operator, operand):
    # Initialize the result with the first operand
    result = operand[0]

    # Iterate through the operators and operands
    for i in range(len(operator)):
        op = operator[i]
        num = operand[i + 1]

        # Perform the operation based on the operator
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '//':
            result //= num
        elif op == '**':
            result **= num

    return result """

""" 
    This is the new version of the do_algebra function with the prompt:
    def do_algebra(operator, operand):
        
        Given two lists operator, and operand. The first list has basic algebra operations, and
        the second list is a list of integers. Use the two given lists to build the algebric
        expression and return the evaluation of this expression.

        The basic algebra operations:
        Addition ( + )
        Subtraction ( - )
        Multiplication ( * )
        Floor division ( // )
        Exponentiation ( ** )

        Example:
        operator['+', '*', '-']
        array = [2, 3, 4, 5]
        result = 2 + 3 * 4 - 5
        => result = 9

        Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.


        Please also think about the order of operations. 

 """
def do_algebra(operators, operands):
    # Check if the lengths of the lists are compatible
    if len(operators) != len(operands) - 1:
        raise ValueError("The length of the operator list must be one less than the length of the operand list.")

    # Start with the first operand
    expression = str(operands[0])

    # Iterate through the operators and operands to build the expression
    for operator, operand in zip(operators, operands[1:]):
        expression += f" {operator} {operand}"

    # Evaluate the expression
    result = eval(expression)
    return result

# decode_cyclic (task_id: HumanEval/38)
def decode_cyclic(s: str) -> str:
    """
    Takes as input a string encoded with the encode_cyclic function and returns the decoded string.
    """
    # Split string into groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group back to their original positions. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)
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