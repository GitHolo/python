with open("liczby_przyklad.txt", "r") as file:
    li = []
    lines = file.readlines()
    first_row = lines[0]
    for line in first_row.split():
        li.append(int(line))
    li.sort(reverse=True)
    print(li[100])