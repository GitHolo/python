with open("skrot.txt") as f:
    for line in f:
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
        if m == 0:
            print("Skrót liczby nie istnieje.")
            with open("wyniki3_2.txt", "a") as file: 
                file.write(str(number) + "\n")
        else:
            print("Skrótem liczby jest ", m)
