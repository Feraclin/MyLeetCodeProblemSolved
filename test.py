from array import array
from datetime import datetime

print(datetime.now())
f = open('input.txt', 'r').readlines()

n, m, k = tuple(map(int, f[0].strip().split()))


def prefix_sum(strg: str) -> array:
    lst = strg.strip().split()
    prefix_lst: list[int] = list()
    prefix_lst.append(int(lst[0]))
    for i in lst[1:]:
        prefix_lst.append(prefix_lst[-1] + int(i))
    return array('l', prefix_lst)

def prefix_matrix(lst: list[array]) ->  list[array]:
    for i in range(1, len(lst)):
        for j in range(len(lst[i])):
            lst[i][j] += lst[i-1][j]
    return lst


matrix = prefix_matrix([prefix_sum(row) for row in f[1:n+1]])

def sum_in_rect(lst: list[array], ask: tuple[int]) -> str:
    a = lst[ask[2] - 1][ask[3] - 1]  # правый нижний общая сумма
    b = ((0, lst[ask[0] - 2][ask[1] - 2])[ask[0] > 1 and ask[1] > 1])  # левый верхний добавления вычтенным двумя углами
    c = ((0, lst[ask[0] - 2][ask[3] - 1])[ask[0] > 1])  # правый верхний сумма
    d = ((0, lst[ask[2] - 1][ask[1] - 2])[ask[1] > 1])  # левый нижний сумма
    res = a + b - c - d
    return str(res) + '\n'

with open('output.txt', 'w') as out:
    lst = [(sum_in_rect(matrix, (tuple(map(int, t.strip().split()))))) for t in f[n+1:]]
    out.writelines(lst)
print(datetime.now())