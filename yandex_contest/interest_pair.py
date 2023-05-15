from collections import Counter
from typing import List


def search_pair(lst: List[Counter]) -> int:
    l_w = len(lst[0])
    k = 0
    result = 0
    for i in lst:
        k += 1
        for j in lst[k:]:
            (tmp := Counter(i)).subtract(j)
            tmp_lst = sorted(i for i in tmp.values() if i in (1, -1))
            if len(tmp_lst) == 2 and tmp_lst == [-1, 1]:
                result += 1
    return result


lst = [Counter(input()).most_common() for i in range(int(input()))]
# print(search_pair(lst))
# (tmp := lst[0]).subtract(lst[2])
print(lst[0])
