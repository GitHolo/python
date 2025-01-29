def insertSort(arr: list):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

def arrFill(arr: list):

    n = int(input("podaj ilość liczb w tabeli: "))

    while n>0:

        a = int(input("podaj liczbe: "))
        arr.append(a)
        n-=1
        
    return arr

arr = []

print(arrFill(arr))

print(insertSort(arr))