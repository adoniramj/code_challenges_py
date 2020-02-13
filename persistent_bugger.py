"""
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit.
Steps.
1. Must be integer
2. Is n < 10 => return
3. split the digits
"""

def persistence(n):
    if isinstance(n, int):
        if n < 10:
            return 0
        num_str = str(n)
        count = 0
        while True:
            result = 1
            for item in num_str:
                result *= int(item) # result is an int
                print(result)
            if result >= 10:
                num_str = str(result)
                count += 1
                continue
            return count + 1  



print(persistence(999))