n = '((4 + 3) * 6 / (2 - 5)) * 6'

n_lst = [int(i) if i.isdigit() else i for i in n]

print(n_lst)
