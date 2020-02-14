"""
It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. 
You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

1. Applies to string length > 2
2. Split the string into a list.
3. Remove characters.
4. Join string.
"""


def remove_char(s):
    if len(s) > 2:
        return s[1:(len(s)-1)]
    return ''

test_string = "ok"

print(remove_chars(test_string))