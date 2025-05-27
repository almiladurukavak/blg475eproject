
# @Authors
# Student Names: <Almila Duru Kavak, Aydan Günaydın, Umut Ural>
# Student IDs: <150150703, 150200012, 150200013>

from typing import List, Tuple
from collections import deque

### EASY LEVEL PROBLEMS ###

# make_palindrome (task_id: HumanEval/10)
def is_palindrome(string: str) -> bool:
  return string == string[::-1]

def make_palindrome(string: str) -> str:
  n = len(string)
  if n == 0:
      return ""
  for i in range(n - 1, -1, -1):
      if is_palindrome(string[i:]):
          prefix_to_reverse = string[:i]
          return string + prefix_to_reverse[::-1]
  return string + string[:-1][::-1]

# truncate_number (task_id: HumanEval/2)
def truncate_number(number: float) -> float:
    return number % 1.0

# sum_product (task_id: HumanEval/8)
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_value = 0
    prod_value = 1

    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value

# greatest_common_divisor (task_id: HumanEval/13)
def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# strlen (task_id: HumanEval/23)
def strlen(string: str) -> int:
    return len(string)

# max_element (task_id: HumanEval/35)
def max_element(l: list):
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m

# incr_list (task_id: HumanEval/42)
def incr_list(l: list):
    return [(e + 1) for e in l]

# median (task_id: HumanEval/47)
def median(l: list):
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0
    
# sum_to_n (task_id: HumanEval/60)
def sum_to_n(n: int):
    return sum(range(n + 1))

# add (task_id: HumanEval/53)
def add(x: int, y: int):
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
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

#common (task_id: HumanEval/58)
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    return sorted(set(l1) & set(l2))

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


### HARD LEVEL PROBLEMS ###


# total_match (task_id: HumanEval/74)
def total_match(lst1, lst2):
    # Calculate total characters in each list
    total1 = sum(len(word) for word in lst1)
    total2 = sum(len(word) for word in lst2)

    # Return the list with fewer total characters
    if total1 <= total2:
        return lst1
    else:
        return lst2

# will_it_fly (task_id: HumanEval/72)
def will_it_fly(q, w):
    # Check if the list q is a palindrome
    if q == q[::-1]:
        # Check if the sum of the elements is less than or equal to w
        if sum(q) <= w:
            return True
    return False

# circular_shift (task_id: HumanEval/65)
def circular_shift(x, shift):
    # Convert the integer to a string
    x_str = str(x)
    n = len(x_str)  # Number of digits in the number

    # If shift is greater than or equal to the number of digits, reverse the string
    if shift >= n:
        return x_str[::-1]

    # Perform the circular shift by slicing the string
    shifted_str = x_str[-shift:] + x_str[:-shift]

    return shifted_str

# reverse_delete (task_id: HumanEval/112)
def reverse_delete(s, c):
    # Step 1: Remove all characters from s that are in c
    result_string = ''.join([char for char in s if char not in c])

    # Step 2: Check if the result string is a palindrome
    is_palindrome = result_string == result_string[::-1]

    # Return the result tuple
    return (result_string, is_palindrome)

# minPath (task_id: HumanEval/129)
def minPath(grid, k):
    N = len(grid)

    # Directions for up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Function to check if a cell is within the grid boundaries
    def is_valid(x, y):
        return 0 <= x < N and 0 <= y < N

    # Function to perform BFS and return the lexicographically smallest path of length k
    def bfs(start_x, start_y):
        # Queue will store tuples of (x, y, path), where path is a list of visited cell values
        queue = deque([(start_x, start_y, [grid[start_x][start_y]])])
        min_path = None

        while queue:
            x, y, path = queue.popleft()

            # If the path length is k, check if it is the smallest path found so far
            if len(path) == k:
                if min_path is None or path < min_path:
                    min_path = path
                continue

            # Explore all neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny):
                    # Append the next cell to the path
                    queue.append((nx, ny, path + [grid[nx][ny]]))

        return min_path

    # Initialize the best path as None (to store lexicographically smallest path)
    best_path = None

    # Try starting from each cell in the grid
    for i in range(N):
        for j in range(N):
            current_path = bfs(i, j)
            if best_path is None or current_path < best_path:
                best_path = current_path

    return best_path

# move_one_ball (task_id: HumanEval/109)
def move_one_ball(arr):
    # Edge case: if the array is empty, return True
    if not arr:
        return True

    # Initialize count of decreases
    decrease_count = 0

    # Loop through the array to find the number of decreases
    n = len(arr)
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            decrease_count += 1

    # If there is more than one decrease, it's not possible to sort the array
    return decrease_count <= 1

# Strongest_Extension (task_id: HumanEval/153)
def Strongest_Extension(class_name, extensions):
    max_strength = float('-inf')  # Initialize to a very low value
    strongest_extension = ""

    # Loop through the extensions
    for extension in extensions:
        # Calculate the number of uppercase and lowercase letters
        CAP = sum(1 for char in extension if char.isupper())
        SM = sum(1 for char in extension if char.islower())

        # Calculate the strength of the extension
        strength = CAP - SM

        # Update the strongest extension if necessary
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    # Return the result in the required format
    return f"{class_name}.{strongest_extension}"

# right_angle_triangle (task_id: HumanEval/157)
def right_angle_triangle(a, b, c):
    # Find the largest of the three sides
    sides = sorted([a, b, c])

    # Check if the sum of the squares of the two smaller sides equals the square of the largest side
    return sides[0]**2 + sides[1]**2 == sides[2]**2

# do_algebra (task_id: HumanEval/160)
def do_algebra(operator, operand):
    # Ensure we have at least one operator and two operands
    if len(operator) == 0 or len(operand) < 2:
        raise ValueError("Invalid input: operator list must have at least one element and operand list at least two.")

    # Start by creating the expression string with the first operand
    expression = str(operand[0])

    # Iterate through operators and operands to build the expression
    for i in range(len(operator)):
        expression += f" {operator[i]} {operand[i + 1]}"

    # Evaluate the expression
    result = eval(expression)
    return result

# decode_cyclic (task_id: HumanEval/38)
def decode_cyclic(s: str):
    """
    Takes as input a string encoded with the encode_cyclic function.
    Returns the decoded string by reversing the cyclic shifts.
    """
    # Split string into groups of 3
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]

    # Reverse the cyclic shift for each group of length 3
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]

    # Join all the groups back into a single string
    return "".join(groups)