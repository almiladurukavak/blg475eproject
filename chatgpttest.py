
# @Authors
# Student Names: <Almila Duru Kavak, Umut Ural>
# Student IDs: <150150703, 150200013>


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
def test_total_match():
    assert total_match(['hello', 'world'], ['hi', 'there']) == ['hello', 'world'], "Test Case 1 Failed"
    assert total_match(['apple', 'banana'], ['carrot', 'pear', 'melon']) == ['apple', 'banana'], "Test Case 2 Failed"
    assert total_match(['abc', 'xyz'], ['a', 'b', 'c', 'x', 'y', 'z']) == ['a', 'b', 'c', 'x', 'y', 'z'], "Test Case 3 Failed"

# will_it_fly (task_id: HumanEval/72)
def will_it_fly(q, w):
    # Check if the list q is a palindrome
    if q == q[::-1]:
        # Check if the sum of the elements is less than or equal to w
        if sum(q) <= w:
            return True
    return False
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

# reverse_delete (task_id: HumanEval/112)
def reverse_delete(s, c):
    # Step 1: Remove all characters from s that are in c
    result_string = ''.join([char for char in s if char not in c])

    # Step 2: Check if the result string is a palindrome
    is_palindrome = result_string == result_string[::-1]

    # Return the result tuple
    return (result_string, is_palindrome)
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

# right_angle_triangle (task_id: HumanEval/157)
def right_angle_triangle(a, b, c):
    # Find the largest of the three sides
    sides = sorted([a, b, c])

    # Check if the sum of the squares of the two smaller sides equals the square of the largest side
    return sides[0]**2 + sides[1]**2 == sides[2]**2
def test_right_angle_triangle():
    # Test case 1: Valid right angle triangle (3, 4, 5)
    assert right_angle_triangle(3, 4, 5) == True, "Test case 1 failed"

    # Test case 2: Valid right angle triangle (5, 12, 13)
    assert right_angle_triangle(5, 12, 13) == True, "Test case 2 failed"

    # Test case 3: Not a right angle triangle (1, 2, 3)
    assert right_angle_triangle(1, 2, 3) == False, "Test case 3 failed"

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