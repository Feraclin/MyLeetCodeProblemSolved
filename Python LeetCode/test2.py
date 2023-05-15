
from typing import List, Dict

lst_dct =  [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]
def remove_duplicates(lst: List[Dict]) -> None:
    lst_dct1 = [] # Дополнительные списки задействуют дополнительную память (возможно просто вывести новый список без дубликатов)
    lst_n = [] # список номеров дубликатов(длина k)
    for k, i in enumerate(lst): # цикл по всем элементам O(n)
        if i not in lst_dct1: # Проверка каждого элемента в списке уникальных значений сложность зависит от длины списка уникальных в худшем случае n
            lst_dct1.append(i)
        else:
            lst_n.append(k)

    for i in reversed(lst_n): # Цикл O(k)
        lst.pop(i) # Удаление дубликатов в обратном порядке O(1)

remove_duplicates(lst_dct)
print(lst_dct)