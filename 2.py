import math
with open("skrot2.txt", "r") as lines:
    for line in lines:
        number = int(line)
        n = int(line)
        m = 0
        num = 1
        while n > 0:
            last = n % 10
            n = n // 10
            if last % 2 != 0:
                m = m + last * num
                num = num * 10
        if m != 0:
            if math.gcd(number, m) == 7:
                with open("wyniki3_3.txt", "a") as f:
                    f.write(str(number) + " skrot: " + str(m) + "\n")
            