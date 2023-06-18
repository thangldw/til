"""
The codes in this post, what I learnt from [`30 Helpful Python Snippets That You Can Learn in 30 Seconds or Less`](https://towardsdatascience.com/30-helpful-python-snippets-that-you-can-learn-in-30-seconds-or-less-69bb49204172)
"""#0. List function for variable.

s = 'Hello World'

dir(s)

# Check unique list - Checks whether a list has duplicate values by using the fact that set() contains only unique elements.

def is_unique_list(list):
    return len(list) == len(set(list))

a = [1,2,3,4,5]
b = [1,2,3,4,2]

is_unique_list(a), is_unique_list(b)

# Check Anagrams string - "abcd" and "dabc" are anagram of each other.

from collections import Counter

def is_anagram(first, second):
    return Counter(first) == Counter(second)

is_anagram('abcd3', '3acdb')

# Check Anagrams string with Time Complexity: O(n) and Space Complexity: O(1)
# The above implementation can be further optimized by using bit manipulation. 
# If we start at a value of 0 and XOR all the characters of both strings, 
# we should return an end value of 0 if they are anagrams because there would be an even occurrence of all characters in the anagram. 
# ord(): method returns an integer representing Unicode code point for the given Unicode character

def is_anagram(first, second):
    if len(first) != len(second):
        return False
    else:
        check = 0
        for i in range(len(first)):
            check ^= ord(first[i])^ord(second[i])
        return check == 0
    
is_anagram('abcd3', '3acdb')

# Memory - This snippet can be used to check the memory usage of an object.

import sys

variable = 30 

print(sys.getsizeof(variable))

# Byte size - This method returns the length of a string in bytes.

def byte_size(string):
    return(len(string.encode('utf-8')))

byte_size('Hello World')

# Print a string N times - This snippet can be used to print a string n times without having to use loops to do it.

n = 2
s ="Programming"

print(s * n)

# Chunk - This method chunks a list into smaller lists of a specified size.

def chunk(ls, size):
    return [ls[i:i+size] for i in range(0, len(ls), size)]

print(chunk([1, 2, 3, 4, 5, 6, 7], 3))
print(chunk('hello world', 3))

# Compact - This method removes falsy values (False, None, 0 and "") from a list by using filter().

def compact(ls):
    return list(filter(bool, ls))

compact([0, 1, False, 2, '', 3, 'a', 's', 34, True, ""])

# Transpose - This snippet can be used to transpose a 2D array.

array = [['a', 'b'], ['c', 'd'], ['e', 'f']]

transposed = zip(*array)

print(list(transposed))

# Comma-separated - This snippet can be used to turn a list of strings into a single string with each element from the list separated by commas.

hobbies = ["eating", "travel", "swimming"]

print("My hobbies are: " + ", ".join(hobbies)) # My hobbies are: basketball, football, swimming# Count characters in a string - This method counts the number of character found in a string with re library.

import re

def count_pattern_text(s, pattern_text):
    return len(re.findall(pattern_text, s, re.IGNORECASE))

# Count Vowels:

print(count_pattern_text('Hello world', '[aeiou]'))

# Count Consonants:

print(count_pattern_text('Hello world', '[^ aeiou]'))

# Decapitalize - This method can be used to turn the first letter of the given string into lowercase.

def decapitalize(s):
    return s[:1].lower() + s[1:]

decapitalize('Hello world')

# Flatten - The following methods flatten a potentially deep list using recursion.

flatten = lambda x: [z for y in x for z in (flatten(y) if hasattr(y, '__iter__') and not isinstance(y, str) else (y,))]

print(flatten([[[1,[2],3],[4,[5],6],[7,[8,[9]]]]]))
print(flatten([1, [2], [[3], 4], 5]))

# Difference - This method finds the difference between two iterables

def difference(a, b):
    diff = list(set(a).difference(set(b)))
    diff.extend(list(set(b).difference(set(a))))
    return diff

difference([1, 2, 3, 5, 'hello'], [1, 2, 4, 6, 5])

# Chained function call - call multiple functions inside a single line.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

add_lambda = lambda a, b : a + b
subtract_lambda = lambda a, b : a - b

a, b = 4, 5

print('subtract if {} > {} else add. Result: {}'.format(a, b, (subtract if a > b else add)(a, b)))
print('subtract if {} > {} else add. Result: {}'.format(a, b, (subtract_lambda if a > b else add_lambda)(a, b))) 

# Merge two dictionaries - The following method can be used to merge two dictionaries.

def merge_dictionaries(a, b):
    return {**a, **b}

a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}

merge_dictionaries(a, b)

# Convert two lists into a dictionary - The following method can be used to convert two lists into a dictionary.

def to_dictionary(keys, values):
    return dict(zip(keys, values))

keys = [2, 3, 4]
values = ['a', 'b', 'c']    

to_dictionary(keys, values)

# Use enumerate - This snippet shows that you can use enumerate to get both the values and the indexes of lists.

ls = ["a", "b", "c", "d"]

for index, element in enumerate(ls): 
    print("Value", element, "Index ", index)

# Try else - We can have an else clause as part of a try/except block, which is executed if no exception is thrown.
try:
    s = 'Today is Friday.'
except TypeError:
    print("An exception was raised")
else:
    print("Thank God, {}".format(s))

# Most frequent - This method returns the most frequent element that appears in a list.
def most_frequent_1(l):
    return max(set(l), key=l.count)

l = [1,2,45,55,5,4,4,4,4,4,4,5456,56,6,7,67]

most_frequent_1(l)

# Most frequent with frequent number - This method returns the most frequent element that appears in a list with Counter library

def most_frequent_2(l):
    from collections import Counter
    return Counter(l).most_common(1)[0]

l = [1,2,45,55,5,4,4,4,4,4,4,5456,56,6,7,67]

most_frequent_2(l)

# Test performance with randomize list
import random

l0 = [random.randrange(0,100) for i in range(1000)]
l1 = l0[:] * 100
 
# Palindrome - This method checks whether a given string is a palindrome.

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome('hello world'))
print(is_palindrome('geeks skeeg'))

# Calculator without if-else
import operator

action = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "**": pow
}

print(action['-'](50, 25))

#Detected time complexity:O(N**2)
def find_unique_element(A):
    remove_duplicated = sorted(set(A))

    for i in range(len(remove_duplicated)):
        if A.count(remove_duplicated[i]) == 1:
            return remove_duplicated[i]
        
find_unique_element([1,2,3,4,3,2,4])

# Cycle Array
def shift_right_array(A, K):
    result = []
    for i in range(len(A)):
        result.append(A[(i-K)%len(A)])
    return result
  
def shift_left_array(A, K):
    result = []
    for i in range(len(A)):
        result.append(A[(i+K)%len(A)])
    return result

print(shift_right_array([1,2,3,4,3,2,4], 2))
print(shift_left_array([1,2,3,4,3,2,4], 2))

# Swap key and value in dict

def swap_key_value_dict(old_dict):
    new_dict = {} 
    for key, value in old_dict.items():
        if value in new_dict:
            if not isinstance(new_dict[value], list):
                new_dict[value] = [new_dict[value]]
            new_dict[value].append(key)
        else: 
            new_dict[value]= key
    return new_dictd = {'a':'1','b':'2','c':'2'}
    
swap_key_value_dict(d)
