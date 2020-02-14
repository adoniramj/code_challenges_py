def odd_or_even(arr):
    total = 0
    for num in arr:
        total += num
    return (lambda x : x % 2 and 'odd' or 'even')(total)

