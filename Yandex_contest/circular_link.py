from typing import List, Dict


def find_circular(dct: Dict[str, List[str]]) -> List[str|int]:
    result = []
    for k, v in dct.items():
        if v[0] == '1':
            v[1] = int(v[1])
            result.append(v[1])
        if v[0] == '2':
            v[1] = v[1].replace('*', ' * ').replace('+', ' + ').replace('-', ' - ').split()
            # print(v[1])
            for n, i in enumerate(v[1]):
                if i[0] == 'C' and dct.get(i)[0] == '2':
                    return [-1, ]
                elif i[0] == 'C':
                    v[1][n] = str(dct.get(i)[1])
            # print(v[1])
            v[1] = eval(''.join(v[1]))
            result.append(v[1])
    return result


dct_in = {f'C{i + 1}': input().split(maxsplit=1) for i in range(int(input()))}
print(find_circular(dct_in))
