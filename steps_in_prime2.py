def step(g,m,n):
    arr_primes = []
    for j in range(m, n + 1):
        item = j
        for k in range(2,j):
            if j % k == 0:
                prime = False
                break   
        if prime:
            arr_primes.append(j)
        prime = True

    for j in arr_primes:
        if(j+g) in arr_primes:
            return (j, j+g)
            
    return None


print(step(2,100,110))
print(step(8,300,400))
print(step(10,300,400))