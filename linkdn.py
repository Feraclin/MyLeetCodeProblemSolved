def haffman(lst: str) -> None:
    from collections import Counter
    dct_let = {}
    a = '00'
    b = '10'
    flag = True

    if len(set(lst)) < 5:
        a = '0'
        for j in sorted(Counter(lst).most_common(), reverse=True, key=lambda x: x[1]):
            dct_let[j[0]] = a
            a = '1' + a
        if len(set(lst)) > 1:
            dct_let[j[0]] = dct_let.get(j[0])[:-1]
    else:
        for j in sorted(Counter(lst).most_common(), reverse=True, key=lambda x: (x[1], 1/ord(x[0]))):
            if flag:
                dct_let[j[0]] = a
                a = '1' + a
                flag = False
                tmp1 = j[0]
            else:
                dct_let[j[0]] = b
                b = '0' + b
                flag = True
                tmp2 = j[0]
        if len(set(lst)) > 1:
            dct_let[tmp1] = dct_let.get(tmp1)[:-1]
            if flag:
                dct_let[tmp2] = dct_let.get(tmp2)[1:]
    print(dct_let)
    res = ''.join([dct_let.get(i) for i in lst])
    print(len(dct_let), len(res))
    [print(f'{k}: {v}') for k, v in dct_let.items()]
    print(res)


haffman('accepted')
# accepted
# 6 20
# p: 110
# a: 111
# c: 10
# t: 011
# d: 010
# e: 00
# 11110100011001100010
haffman('abacabad')
