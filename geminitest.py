# @Authors
# Student Names: <Almila Duru Kavak>
# Student IDs: <150150703>


# fib (task_id: HumanEval/55)

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
    raise ValueError("Input must be a positive integer")
elif n == 1:
    return 1
elif n == 2:
    return 1
else:
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

# test cases

>> > fib(5)
5
>> > fib(3)
2
>> > fib(15)
610


# common (task_id: HumanEval/58)

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """


set1 = set(l1)
set2 = set(l2)
common_elements = sorted(list(set1.intersection(set2)))
return common_elements

# test cases

>> > common([1, 2, 3], [4, 5, 6])
[]
>> > common(['apple', 'banana', 'cherry'], ['banana', 'date', 'apple'])
['apple', 'banana']
>> > common([10, 20, 30, 10], [30, 40, 20, 20])
[20, 30]


# even_odd_palindrome (task_id: HumanEval/107)

def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

    Input: 3
    Output: (1, 2)
    Explanation:
    Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

    Input: 12
    Output: (4, 6)
    Explanation:
    Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
    1. 1 <= n <= 10^3
    2. returned tuple has the number of even and odd integer palindromes respectively.
    """


even_palindromes = 0
odd_palindromes = 0
for i in range(1, n + 1):
    s = str(i)
    if s == s[::-1]:
        if i % 2 == 0:
            even_palindromes += 1
        else:
            odd_palindromes += 1
return (even_palindromes, odd_palindromes)
# test cases

>> > even_odd_palindrome(1)
(0, 1)
>> > even_odd_palindrome(22)
(9, 10)
>> > even_odd_palindrome(100)
(9, 9)


# sum_squares (task_id: HumanEval/142)

def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries.

    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = [] the output should be 0
    For lst = [-1,-5,2,-1,-5] the output should be -126
    """


total_sum = 0
for index, value in enumerate(lst):
    if index % 3 == 0:
        total_sum += value ** 2
    elif index % 4 == 0:
        total_sum += value ** 3
    else:
        total_sum += value
return total_sum
# test cases

>> > sum_squares([1, 2, 3, 4, 5, 6])
50
>> > sum_squares([10, -20, 30, -40, 50])
-79010
>> > sum_squares([2, 4, 6, 8, 10, 12, 14, 16])
4 + 6 + 512 + 10 + 12 + 196 + 16 = 756


# specialFilter (task_id: HumanEval/146)

def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns
    the number of elements in the array that are greater than 10 and both
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """


count = 0
for num in nums:
    if abs(num) > 10:
        s_num = str(abs(num))
        if len(s_num) > 0 and int(s_num[0]) % 2 != 0 and int(s_num[-1]) % 2 != 0:
            count += 1
return count

# test cases

>> > specialFilter([11, 22, 33, 44, 55])
3
>> > specialFilter([135, 246, 357, 468, 579])
3
>> > specialFilter([1, 11, 101, 222, 313, 404, 515])
3


# is_bored (task_id: HumanEval/91)
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


count = 0
sentences = S.split('.')
for sentence in sentences:
    if sentence.strip().startswith("I"):
        if sentence.strip()[-1] in ['.', '?', '!']:
            count += 1
        elif not sentence.strip():
            continue
        else:
            # Check if the 'I' sentence is the last part before '?' or '!'
            parts = sentence.split('?')
            for part in parts:
                if part.strip().startswith("I") and not part.strip().endswith('!'):
                    count += 1
            parts = sentence.split('!')
            for part in parts:
                if part.strip().startswith("I"):
                    count += 1
return count

# test cases

>> > is_bored("I am bored.")
1
>> > is_bored("Are you happy? I am!")
1
>> > is_bored("This is a sentence. Is this another? I think so.")
1


# encrypt (task_id: HumanEval/89)

def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated.
    The alphabet should be rotated in a manner such that the letters
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """


result = ''
for char in s:
    if 'a' <= char <= 'z':
        shifted_char = chr(((ord(char) - ord('a') + 4) % 26) + ord('a'))
    elif 'A' <= char <= 'Z':
        shifted_char = chr(((ord(char) - ord('A') + 4) % 26) + ord('A'))
    else:
        shifted_char = char
    result += shifted_char
return result

# test cases

>> > encrypt('xyz')
'bcd'
>> > encrypt('HELLO')
'LIPPS'
>> > encrypt('hello world')
'lipps asvph'


# rounded_avg (task_id: HumanEval/103)


def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m).
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """


if n > m:
    return -1
total = sum(range(n, m + 1))
count = m - n + 1
average = round(total / count)
return bin(average)

# test cases

>> > rounded_avg(1, 1)
'0b1'
>> > rounded_avg(2, 4)
'0b11'
>> > rounded_avg(15, 16)
'0b1111'


# minSubArraySum (task_id: HumanEval/114)

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """


if not nums:
    raise ValueError("Input array cannot be empty")

min_so_far = float('inf')
current_min = 0

for num in nums:
    current_min = min(num, current_min + num)
    min_so_far = min(min_so_far, current_min)

return min_so_far

# test cases

>> > minSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
-5
>> > minSubArraySum([1])
1
>> > minSubArraySum([-5])
-5


# intersection (task_id: HumanEval/127)

def intersection(interval1, interval2):
    """You are given two intervals,
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
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    """


start1, end1 = interval1
start2, end2 = interval2

intersection_start = max(start1, start2)
intersection_end = min(end1, end2)

if intersection_start > intersection_end:
    return "NO"

intersection_length = intersection_end - intersection_start + 1

if intersection_length <= 1:
    return "NO"

if intersection_length == 2:
    return "YES"

if intersection_length % 2 == 0:
    return "NO"

for i in range(3, int(intersection_length ** 0.5) + 1, 2):
    if intersection_length % i == 0:
        return "NO"

return "YES"

# test cases

>> > intersection((0, 5), (2, 3))
'YES'
>> > intersection((10, 20), (15, 25))
'YES'
>> > intersection((-10, 0), (0, 10))
'NO'



