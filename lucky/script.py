
def lucky(limit):
    
    arr = list(range(1, limit+1))
    n = 1

    while n < len(arr):

        step = arr[n]
        arr = [num for i, num in enumerate(arr) if (i + 1) % step != 0]
        n+=1

    return arr

print(lucky(20))
