"""
Remove all the vowels from the input string => return a string with no vowels

"""
import re
from string import maketrans

def disemvowel(string):
  newstring = ''
  for letter in string:
    if letter not in 'aeiouAEIOU':
      newstring += letter
  return newstring

def disemvowel2(string):
  return re.sub('[aeiou]', '', string, flags=re.IGNORECASE)

print(x)