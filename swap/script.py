def swap(a,b):
    a,b = b,a
    a="a is "+str(a)
    b="b is "+str(b)
    return a,b

a=input('a: ')
b=input('b: ')

print(swap(a,b))