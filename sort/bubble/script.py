def bubble(arr: list):

    n = len(arr)
    
    for i in range(n):

        swapped = False

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        print(n-i-1)
        if (swapped == False):
            break

    return arr
arr = []

def arrFill(arr: list):

    n = int(input("podaj ilość liczb w tabeli: "))

    while n>0:

        a = int(input("podaj liczbe: "))
        arr.append(a)
        n-=1

    return arr


print(arrFill(arr))
print(bubble(arr))



