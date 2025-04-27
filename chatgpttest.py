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
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b
def test_fib():
    assert fib(1) == 1       # Base case
    assert fib(5) == 5       # fib(5) = 1, 1, 2, 3, 5
    assert fib(12) == 144    # fib(12) = 144

#common (task_id: HumanEval/58)
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    return sorted(set(l1) & set(l2))
def test_common():
    # Test case 1: Common elements between two lists with some duplicates
    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]

    # Test case 2: Common elements between two lists with smaller numbers
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3]

    # Test case 3: No common elements between two lists
    assert common([10, 20, 30], [40, 50, 60]) == []

#even_odd_palindrome (task_id: HumanEval/107)
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:
    >>> even_odd_palindrome(3)
    (1, 2)

    Example 2:
    >>> even_odd_palindrome(12)
    (4, 6)

    Note:
    1. 1 <= n <= 10^3
    2. Returned tuple has the number of even and odd integer palindromes respectively.
    """
    even_count = 0
    odd_count = 0

    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:  # check if it's a palindrome
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    return (even_count, odd_count)
def test_even_odd_palindrome():
    # Test case 1: Palindromes in the range 1 to 3 (inclusive)
    assert even_odd_palindrome(3) == (1, 2)  # Even palindrome: 2, Odd palindromes: 1, 3

    # Test case 2: Palindromes in the range 1 to 12 (inclusive)
    assert even_odd_palindrome(12) == (4, 6)  # Even palindromes: 2, 4, 6, 8, Odd palindromes: 1, 3, 5, 7, 9, 11

    # Test case 3: Palindromes in the range 1 to 20 (inclusive)
    assert even_odd_palindrome(20) == (6, 9)  # Even palindromes: 2, 4, 6, 8, 11, 22, Odd palindromes: 1, 3, 5, 7, 9, 11, 13, 15, 17

#sum_squares (task_id: HumanEval/142)
def sum_squares(lst):
    """
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries.

    Examples:
    >>> sum_squares([1, 2, 3])
    6
    >>> sum_squares([])
    0
    >>> sum_squares([-1, -5, 2, -1, -5])
    -126
    """
    total = 0
    for i, val in enumerate(lst):
        if i % 3 == 0:
            total += val ** 2
        elif i % 4 == 0:
            total += val ** 3
        else:
            total += val
    return total
def test_sum_squares():
    # Test case 1: List with 3 elements
    assert sum_squares([1, 2, 3]) == 6  # Squared first element (1^2), 2 stays, 3 stays

    # Test case 2: Empty list
    assert sum_squares([]) == 0  # No elements to sum

    # Test case 3: List with both positive and negative numbers
    assert sum_squares([-1, -5, 2, -1, -5]) == -126  # (-1^2) + (-5^3) + 2 + (-1^2) + (-5^3)

#specialFilter (task_id: HumanEval/146)
def specialFilter(nums):
    """
    Write a function that takes an array of numbers as input and returns
    the number of elements in the array that are greater than 10 and both
    first and last digits of a number are odd (1, 3, 5, 7, 9).

    For example:
    >>> specialFilter([15, -73, 14, -15])
    1
    >>> specialFilter([33, -2, -3, 45, 21, 109])
    2
    """
    def is_odd_digit(ch):
        return ch in '13579'

    count = 0
    for num in nums:
        if num > 10:
            str_num = str(num)
            if is_odd_digit(str_num[0]) and is_odd_digit(str_num[-1]):
                count += 1
    return count
def test_specialFilter():
    # Test case 1: List with both positive and negative numbers
    assert specialFilter([15, -73, 14, -15]) == 1  # Only 15 meets the criteria (first and last digits are odd)

    # Test case 2: List with a mix of numbers, some greater than 10
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2  # 33 and 109 meet the criteria

    # Test case 3: List with all numbers less than or equal to 10
    assert specialFilter([2, 5, 7, 10]) == 0  # No numbers greater than 10, so the result is 0

#is_bored (task_id: HumanEval/91)
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.

    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    import re
    sentences = re.split(r'[.?!]', S)
    count = 0
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence.startswith('I '):
            count += 1
        elif sentence == 'I':
            count += 1
    return count
def test_is_bored():
    # Test case 1: String with no sentences starting with "I"
    assert is_bored("Hello world. How are you? I am fine.") == 1  # "I am fine" starts with "I", so 1 boredom

    # Test case 2: String with multiple sentences starting with "I"
    assert is_bored("I love programming. I enjoy challenges. I am learning.") == 3  # All three sentences start with "I"

    # Test case 3: String with no "I" at all
    assert is_bored("The sun is shining. It is a beautiful day.") == 0  # No sentence starts with "I"

#encrypt (task_id: HumanEval/89)
def encrypt(s):
    """
    Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated.
    The alphabet should be rotated in a manner such that the letters
    shift down by two multiplied to two places.

    For example:
    >>> encrypt('hi')
    'lm'
    >>> encrypt('asdfghjkl')
    'ewhjklnop'
    >>> encrypt('gf')
    'kj'
    >>> encrypt('et')
    'ix'
    """
    result = ""
    shift = 2 * 2  # shift by 4 positions

    for char in s:
        if 'a' <= char <= 'z':
            new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            result += new_char
        else:
            result += char  # leave non-lowercase letters unchanged

    return result
def test_encrypt():
    # Test case 1: Simple string with lowercase letters
    assert encrypt('hi') == 'lm'  # 'h' -> 'l', 'i' -> 'm'

    # Test case 2: String with multiple characters
    assert encrypt('asdfghjkl') == 'ewhjklnop'  # Each letter shifted by 4 positions

    # Test case 3: String with mixed letters
    assert encrypt('gf') == 'kj'  # 'g' -> 'k', 'f' -> 'j'

#rounded_avg (task_id: HumanEval/103)
def rounded_avg(n, m):
    """
    You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m).
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.

    Example:
    >>> rounded_avg(1, 5)
    '0b11'
    >>> rounded_avg(7, 5)
    -1
    >>> rounded_avg(10, 20)
    '0b1111'
    >>> rounded_avg(20, 33)
    '0b11010'
    """
    if n > m:
        return -1

    total_numbers = m - n + 1
    total_sum = (n + m) * total_numbers // 2
    avg = round(total_sum / total_numbers)
    return bin(avg)
def test_rounded_avg():
    # Test case 1: Average of numbers from 1 to 5
    assert rounded_avg(1, 5) == '0b11'  # Average is (1+2+3+4+5)/5 = 3, which is '0b11' in binary

    # Test case 2: n is greater than m, should return -1
    assert rounded_avg(7, 5) == -1  # n > m, so should return -1

    # Test case 3: Average of numbers from 10 to 20
    assert rounded_avg(10, 20) == '0b1111'  # Average is (10+11+12+...+20)/11 = 15, which is '0b1111' in binary

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
def test_minSubArraySum():
    # Test case 1: Array with positive and negative numbers
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1  # The smallest sub-array sum is just [1]

    # Test case 2: Array with all negative numbers
    assert minSubArraySum([-1, -2, -3]) == -6  # The sum of the whole array is the minimum, which is -6

    # Test case 3: Array with mixed positive and negative numbers
    assert minSubArraySum([1, -2, 3, -4, 5]) == -4  # The smallest sub-array sum is [-4]

#intersection (task_id: HumanEval/127)
def intersection(interval1, interval2):
    """
    You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two
    intervals is a prime number.

    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".

    [input/output] samples:
    >>> intersection((1, 2), (2, 3))
    'NO'
    >>> intersection((-1, 1), (0, 4))
    'NO'
    >>> intersection((-3, -1), (-5, 5))
    'YES'
    """

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    start1, end1 = interval1
    start2, end2 = interval2

    start = max(start1, start2)
    end = min(end1, end2)

    if start > end:
        return "NO"

    # Since intervals are closed, length is (end - start + 1)
    length = end - start + 1

    return "YES" if is_prime(length) else "NO"
def test_intersection():
    # Test case 1: Intervals (1, 2) and (2, 3) intersect at point 2 with length 1, which is not prime
    assert intersection((1, 2), (2, 3)) == 'NO'  # Intersection length is 1, which is not prime

    # Test case 2: Intervals (-1, 1) and (0, 4) intersect at points 0 and 1 with length 2, which is prime
    assert intersection((-1, 1), (0, 4)) == 'NO'  # Intersection length is 2, which is prime

    # Test case 3: Intervals (-3, -1) and (-5, 5) intersect at points -3, -2, -1 with length 3, which is prime
    assert intersection((-3, -1), (-5, 5)) == 'YES'  # Intersection length is 3, which is prime
