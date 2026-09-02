#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#import counter from collections.
from collections import Counter
# define a function and taking two strings as input parameters.
def is_anagram(s, t):
# return true if the count of characters in both strings is the same
# otherwise return false.
    return Counter(s) == Counter(t)

#taking input from the user.
s = input("Enter the first string: ")
t = input("Enter the second string: ")

print(is_anagram(s, t))