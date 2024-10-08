with open("liczby.txt", "r") as file:
    li = []
    lines = file.readlines()
    first_row = lines[0]
    for line in first_row.split():
        li.append(int(line.strip()))
    li.sort(reverse=True)
    print(li)