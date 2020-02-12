# Welcome. In this kata, you are asked to square every digit of a number.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer

"""
Thinking process
1. split the digits into a list
"""

def square_digits(num):
    num_str = str(num)
    num_arr = []
    dup_arr = []
    for i in range(len(num_str)):
        num_arr.append(num_str[i])
    for num in num_arr:
        dup_arr.append(str(int(num)**2))
    return int("".join(dup_arr))
 
"""
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)
"""
test_num = 9119

print(square_digits(test_num))