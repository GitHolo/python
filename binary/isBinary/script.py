def isBinary(n: int):
    for i in str(n):
        if str(i) not in ['0', '1']:
            return False
    return True
        
print(isBinary(101))