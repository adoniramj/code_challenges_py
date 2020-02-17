# function to test if an integer is a prime number
# prime number is a whole number greater than one whose only factors are 1 and itself.


def prime_num(num):
    if isinstance(num, int):
        for i in range(2, num):
            if num % i == 0:
                return -1
        return num
