# Podaj, ile liczb z pierwszego wiersza jest dzielnikiem jakiejkolwiek liczby spośród liczb z drugiego wiersza.
with open("liczby.txt", "r") as file:
    lines = file.readlines()
    first_row = lines[0].split()
    second_row = lines[1].split()

    count = 0
    for line in first_row:
        for num in second_row:
            if int(num) % int(line) == 0:
                count += 1
                break
    print(f"Ilość liczb dzielących się z {len(first_row)} liczb spośród {len(second_row)} liczb z drugiego wiersza: {count}")
    with open("wyniki4.txt", "w") as w:
        w.write(str(count))