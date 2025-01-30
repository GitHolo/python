def arrFill(arr: list):
    
    n = int(input("podaj ilość liczb w tabeli: "))

    while n>0:

        a = int(input("podaj liczbe: "))
        b = len(str(a))
        arr.append(float(a/10**b))
        n-=1

    
    return arr

def insertSort(arr: list):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr



def bucketSort(arr: list):
    
    n = len(arr)
    buckets = [[] for _ in range(n)]

    for num in arr:
        bi = int(n * num)
        buckets[bi].append(num)
    
    for bucket in buckets:
        insertSort(bucket)

    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1

arr = []
    
print(arrFill(arr))
bucketSort(arr)
print("posortowana tablica: "+str(arr))


