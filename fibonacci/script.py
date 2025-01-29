def fibonacci(max: int):

    result = [0]
    first = 0
    second = 1

    while max>0:

        first, second = second, first+second
        result.append(first)
        max-=1
        
    return result

max = int(input("podaj limit: "))
print(fibonacci(max))

