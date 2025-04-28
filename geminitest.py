# @Authors
# Student Names: <Almila Duru Kavak, Umut Ural>
# Student IDs: <150150703, 150200013>


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



# total_match (task_id: HumanEval/74)
def total_match(lst1, lst2):
  """
  Accepts two lists of strings and returns the list with a smaller total number of characters.

  If the two lists have the same total number of characters, it returns the first list.

  Examples:
  total_match([], []) ➞ []
  total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
  total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
  total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
  total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
  """
  def calculate_total_chars(lst):
      return sum(len(string) for string in lst)

  total_chars1 = calculate_total_chars(lst1)
  total_chars2 = calculate_total_chars(lst2)

  if total_chars1 <= total_chars2:
      return lst1
  else:
      return lst2

def test_total_match():
  assert total_match([], []) == []
  assert total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
  assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
  assert total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
  assert total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']
  assert total_match(['apple', 'banana'], ['kiwi', 'orange']) == ['kiwi', 'orange']
  assert total_match(['one', 'two', 'three'], ['a', 'b', 'c', 'd', 'e']) == ['one', 'two', 'three']

# will_it_fly (task_id: HumanEval/72)
def will_it_fly(q, w):
  '''
  Write a function that returns True if the object q will fly, and False otherwise.
  The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

  Example:
  will_it_fly([1, 2], 5) ➞ False
  # 1+2 is less than the maximum possible weight, but it's unbalanced.

  will_it_fly([3, 2, 3], 1) ➞ False
  # it's balanced, but 3+2+3 is more than the maximum possible weight.

  will_it_fly([3, 2, 3], 9) ➞ True
  # 3+2+3 is less than the maximum possible weight, and it's balanced.

  will_it_fly([3], 5) ➞ True
  # 3 is less than the maximum possible weight, and it's balanced.
  '''
  if q == q[::-1] and sum(q) <= w:
      return True
  else:
      return False

def test_will_it_fly():
  assert will_it_fly([1, 2], 5) == False
  assert will_it_fly([3, 2, 3], 1) == False
  assert will_it_fly([3, 2, 3], 9) == True

# circular_shift (task_id: HumanEval/65)
def circular_shift(x, shift):
  """Circular shift the digits of the integer x, shift the digits right by shift
  and return the result as a string.
  If shift > number of digits, return digits reversed.
  >>> circular_shift(12, 1)
  "21"
  >>> circular_shift(12, 2)
  "12"
  """
  sx = str(x)
  n = len(sx)
  if n == 0:
      return ""
  effective_shift = shift % n
  if effective_shift == 0:
      return sx
  shifted = sx[-effective_shift:] + sx[:-effective_shift]
  return shifted

def test_circular_shift():
  assert circular_shift(12, 1) == "21"
  assert circular_shift(12345, 2) == "45123"
  assert circular_shift(123, 5) == "321"

# reverse_delete (task_id: HumanEval/112)
def reverse_delete(s, c):
  """Task
  We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
  then check if the result string is palindrome.
  A string is called palindrome if it reads the same backward as forward.
  You should return a tuple containing the result string and True/False for the check.
  Example
  For s = "abcde", c = "ae", the result should be ('bcd',False)
  For s = "abcdef", c = "b" the result should be ('acdef',False)
  For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
  """
  result_string = ""
  for char_s in s:
      if char_s not in c:
          result_string += char_s

  is_palindrome = result_string == result_string[::-1]
  return (result_string, is_palindrome)

def test_reverse_delete():
  assert reverse_delete("abcde", "ae") == ('bcd', False)
  assert reverse_delete("abcdef", "b") == ('acdef', False)
  assert reverse_delete("abcdedcba", "ab") == ('cdedc', True)
# minPath (task_id: HumanEval/129)
import heapq

def minPath(grid, k):
  n = len(grid)
  min_paths = {}  # (row, col, length) -> min_path_list

  for r in range(n):
      for c in range(n):
          min_paths[(r, c, 1)] = [grid[r][c]]

  pq = []
  for r in range(n):
      for c in range(n):
          heapq.heappush(pq, (grid[r][c], r, c, 1, [grid[r][c]]))

  while pq:
      current_val, r, c, length, path = heapq.heappop(pq)

      if length == k:
          return path

      for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
          nr, nc = r + dr, c + dc
          if 0 <= nr < n and 0 <= nc < n:
              new_length = length + 1
              new_path = path + [grid[nr][nc]]
              if (nr, nc, new_length) not in min_paths or new_path < min_paths[(nr, nc, new_length)]:
                  min_paths[(nr, nc, new_length)] = new_path
                  heapq.heappush(pq, (grid[nr][nc], nr, nc, new_length, new_path))

  return []

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
# move_one_ball (task_id: HumanEval/109)
def move_one_ball(arr):
  """
  Determines if a non-decreasingly sorted array can be obtained by right shifts.

  Args:
      arr: A list of unique integers.

  Returns:
      True if a sorted array can be obtained, False otherwise.
  """
  n = len(arr)
  if n == 0:
      return True

  sorted_arr = sorted(arr)

  for i in range(n):
      shifted_arr = arr[-i:] + arr[:-i]
      if shifted_arr == sorted_arr:
          return True

  return False

def test_move_one_ball():
  assert move_one_ball([1, 2, 3, 4, 5]) == True
  assert move_one_ball([3, 4, 5, 1, 2]) == True
  assert move_one_ball([1, 3, 2]) == False
# Strongest_Extension (task_id: HumanEval/153)
def Strongest_Extension(class_name, extensions):
  """You will be given the name of a class (a string) and a list of extensions.
  The extensions are to be used to load additional classes to the class. The
  strength of the extension is as follows: Let CAP be the number of the uppercase
  letters in the extension's name, and let SM be the number of lowercase letters
  in the extension's name, the strength is given by the fraction CAP - SM.
  You should find the strongest extension and return a string in this
  format: ClassName.StrongestExtensionName.
  If there are two or more extensions with the same strength, you should
  choose the one that comes first in the list.
  For example, if you are given "Slices" as the class and a list of the
  extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
  return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension
  (its strength is -1).
  Example:
  for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
  """
  strongest_extension = ""
  max_strength = float('-inf')

  for extension in extensions:
      uppercase_count = 0
      lowercase_count = 0
      for char in extension:
          if 'A' <= char <= 'Z':
              uppercase_count += 1
          elif 'a' <= char <= 'z':
              lowercase_count += 1

      strength = uppercase_count - lowercase_count

      if strength > max_strength:
          max_strength = strength
          strongest_extension = extension

  return f"{class_name}.{strongest_extension}"

def test_strongest_extension():
  assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
  assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
  assert Strongest_Extension('Data', ['Process', 'AnalyzeData', 'Report']) == 'Data.AnalyzeData'
# right_angle_triangle (task_id: HumanEval/157)
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
  sides = sorted([a, b, c])
  return sides[0]**2 + sides[1]**2 == sides[2]**2

def test_right_angle_triangle():
  assert right_angle_triangle(3, 4, 5) == True
  assert right_angle_triangle(1, 2, 3) == False
  assert right_angle_triangle(5, 12, 13) == True
# do_algebra (task_id: HumanEval/160)
def do_algebra(operator, operand):
  """
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
  operator = ['+', '*', '-']
  operand = [2, 3, 4, 5]
  result = 2 + 3 * 4 - 5
  => result = 9

  Note:
  The length of operator list is equal to the length of operand list minus one.
  Operand is a list of of non-negative integers.
  Operator list has at least one operator, and operand list has at least two operands.

  """
  expression = str(operand[0])
  for i in range(len(operator)):
      expression += operator[i] + str(operand[i+1])
  return eval(expression)

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
# decode_cyclic (task_id: HumanEval/38)
def decode_cyclic(s: str):
  """
  takes as input string encoded with encode_cyclic function. Returns decoded string.
  """
  # split string to groups. Each of length 3.
  groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
  # uncycle elements in each group. Unless group has fewer elements than 3.
  groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
  return "".join(groups)

def test_decode_cyclic():
  assert decode_cyclic("cba") == "abc"
  assert decode_cyclic("defghi") == "abcdefghi"
  assert decode_cyclic("jklmno") == "jklmno"