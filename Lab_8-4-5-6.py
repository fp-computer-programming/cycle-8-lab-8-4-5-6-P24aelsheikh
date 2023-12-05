"""
Create a Python file named lab_8-4.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Write a function count_a(word) that takes in a string word and returns the number of a's in the word. 
The function should count both lowercase (a) and uppercase (A)
_____________________________________________________________________________________
"""
def count_a(word):
    # This is Counting both lowercase and uppercase 'a's
    return word.lower().count('a')

# These are Example usage:
word = "Abracadabra"
result = count_a(word)
print(f"The number of 'a's in '{word}' is: {result}")

"""
Create a Python file named lab_8-5.py

Write a function factorial(num) that takes in a number num 
and returns the product of all numbers from 1 up to and including num

_______________________________________________________________________________________
"""
def factorial(num):
    # this is a Base case: factorial of 0 or 1 is 1
    if num == 0 or num == 1:
        return 1
    # this is a Recursive case: num! = num * (num-1)!
    else:
        return num * factorial(num - 1)

# this is an Example usage:
num = 5
result = factorial(num)
print(f"The factorial of {num} is: {result}")

"""
Create a Python file named lab_8-6.py

Write a function is_palindrome(word) that takes in a string word 
and returns the true if the word is a palindrome, false otherwise. 

A palindrome is a word that is spelled the same forwards and backwards.
"""
def is_palindrome(word):
    # This will Convert the word to lowercase to make the comparison case-insensitive
    word = word.lower()
    # THis will Check if the reversed word is equal to the original word
    return word == word[::-1]

# this is an Example usage:
word1 = "radar"
result1 = is_palindrome(word1)
print(f"Is '{word1}' a palindrome? {result1}")

word2 = "hello"
result2 = is_palindrome(word2)
print(f"Is '{word2}' a palindrome? {result2}")
