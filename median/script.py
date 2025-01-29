def median(arr: list):
    n = int(len(arr))
    arr.sort()
    if n%2==0:
        n/=2
        return arr[int((n+(n+1))/2)-1]
    else:
        return arr[int((n+1)/2)]
    
arr = [23, 11, 123213, 1134, 21,3]
print(arr)
print("median:", median(arr))