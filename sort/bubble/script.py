def bubble(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break
    return arr

arr = []

n = int(input("podaj ile liczb w tabeli: "))
while n>0:
    a = int(input("podaj liczbe: "))
    arr.append(a)
    n-=1
print(arr)
print(bubble(arr))



