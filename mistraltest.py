# @Authors
# Student Names: <Almila Duru Kavak>
# Student IDs: <150150703>

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

# Test cases
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # Output: [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # Output: [2, 3]

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

# Test cases
print(even_odd_palindrome(3))   # Output: (1, 2)
print(even_odd_palindrome(12))  # Output: (4, 6)

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

# Test cases
print(sum_squares([1, 2, 3]))  # Output: 6
print(sum_squares([]))  # Output: 0
print(sum_squares([-1, -5, 2, -1, -5]))  # Output: -126


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

# Test cases
print(specialFilter([15, -73, 14, -15]))  # Output: 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # Output: 2


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

# Test cases
print(is_bored("Hello world"))  # Output: 0
print(is_bored("The sky is blue. The sun is shining. I love this weather"))  # Output: 1
print(is_bored("I am bored. Are you? I think so!"))  # Output: 2
print(is_bored("This is a test. I hope it works. I think it will!"))  # Output: 2



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

# Test cases
print(encrypt('hi'))          # Output: 'pm'
print(encrypt('asdfghjkl'))   # Output: 'iwoznpbts'
print(encrypt('gf'))          # Output: 'on'
print(encrypt('et'))          # Output: 'ma'


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

# Test cases
print(rounded_avg(1, 5))   # Output: "0b11"
print(rounded_avg(7, 5))   # Output: -1
print(rounded_avg(10, 20)) # Output: "0b1111"
print(rounded_avg(20, 33)) # Output: "0b11010"

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

# Test cases
print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # Output: 1
print(minSubArraySum([-1, -2, -3]))  # Output: -6



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

# Test cases
print(intersection((1, 2), (2, 3)))  # Output: "NO"
print(intersection((-1, 1), (0, 4)))  # Output: "NO"
print(intersection((-3, -1), (-5, 5)))  # Output: "YES"

