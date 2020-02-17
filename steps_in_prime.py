def prime_num(num):
    if isinstance(num, int):
        for i in range(2, num):
            if num % i == 0:
                return -1
        return num


"""
1. Given a range test -> return a list with prime numbers
"""


def step(g, m, n):

    def prime_num(num):
        if isinstance(num, int):
            for i in range(2, num):
                if num % i == 0:
                    return -1
            return num

    prime_arr = []
    for i in range(m, n + 1):
        num = prime_num(i)
        if num != -1:
            prime_arr.append(i)

    for j in prime_arr:
        if(j+g) in prime_arr:
            return (j, j+g)

    return None


x = step(10, 300, 400)
y = 0
