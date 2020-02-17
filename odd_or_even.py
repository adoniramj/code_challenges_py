def odd_or_even(arr):
    return (lambda x : sum(arr) % 2 and 'odd' or 'even')(arr)
