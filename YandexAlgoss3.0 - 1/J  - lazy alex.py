def letter_counter(letter: str) -> None:
    c = dict()
    length = len(letter)

    a = 0
    # print(letter[:length//2])
    # print(letter[length//2:][::-1])
    for k, i in enumerate(letter[:length//2]):
        a += length - 2 * k
        if i in c:
            c[i] += a
        else:
            c[i] = a
    a = 0
    for k, i in enumerate(letter[length//2:][::-1]):
        a += length - 2 * k
        if i in c:
            c[i] += a
        else:
            c[i] = a
    [print(f"{k}: {c[k]}") for k in sorted(c.keys())]


letter_counter(input())