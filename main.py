with open('input.txt', 'r', encoding='utf-8') as file:
    string: str = file.readline()
with open('output.txt', 'w', encoding='utf-8') as out:
    file.write(str(sum([int(i) for i in string.strip().split()])))
