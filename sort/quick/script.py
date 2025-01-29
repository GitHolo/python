def arrFill(arr: list):

    n = int(input("podaj ilość liczb w tabeli: "))

    while n>0:

        a = int(input("podaj liczbe: "))
        arr.append(a)
        n-=1
        
    return arr



def quickSort(arr: list, low=0, high=None):
    
    if high is None:
        
        high = len(arr)-1
    
    if low < high:

        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot, high)
    
    return arr

def partition(arr: list, low, high):

    pivot = arr[high]
    i = low - 1

    for j in range(low,high):

        if arr[j] <= pivot:

            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

arr = []

print(arrFill(arr))
print(quickSort(arr))
