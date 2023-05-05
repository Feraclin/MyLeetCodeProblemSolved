from collections import Counter


def gistogramma() -> None:





    from string import whitespace
    with open('input.txt', 'r') as f:
        data = f.read()
    counter = Counter(data)
    for i in whitespace:
        if i in counter:
            counter.pop(i)
    max_len = counter.most_common(1)[0][1]
    from string import punctuation, ascii_uppercase, ascii_lowercase
    lst_gist = []
    for i in punctuation + ascii_uppercase + ascii_lowercase:
        if i in counter:
            lst_gist.append(list(i +  '#' * counter[i] + ' ' * (max_len - counter[i])))
    rotated_gist = list(zip(*lst_gist[::-1]))
    [print(''.join(i)[::-1]) for i in rotated_gist[::-1]]


gistogramma()