def arrFill(arr: list):

    n = int(input("podaj ilość liczb w tabeli: "))

    while n>0:

        a = int(input("podaj liczbe: "))
        arr.append(a)
        n-=1
        
    return arr

arr = []

print(arrFill(arr))