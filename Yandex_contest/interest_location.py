from collections import deque
from typing import List


def longest(lst: List[str]) -> List[List[int]]:
    result = []
    tmp = deque()
    for i in lst:
        i = int(i)
        if i not in tmp:
            tmp.append(i)
        elif tmp[0] == i:
            tmp.append(tmp.popleft())
        else:
            result.append(list(tmp))
            tmp.clear()
    result.append(list(tmp))
    lst_out.append(max(result, key=len))


def join_lst(lst: List[List[int]]) -> List[int]:
    result = lst[0]
    for j in lst[1:]:
        result.extend()
    return result


lst_out = []
lst_in = [longest(input().split()) for i in range(3)]

print(len(lst_out))
print(lst_out)
print(join_lst(lst_out))
