import json

# def clear_json(dct: dict) -> dict | None:
#     st = [dct]
#     print(st)
#     while st:
#         current = st.pop()
#         for key, value in list(current.items()):
#             if isinstance(value, dict):
#                 st.append(value)
#                 if not value:
#                     del current[key]
#             elif isinstance(value, list):
#                 for item in value:
#                     if isinstance(item, dict):
#                         st.append(item)
#                 value[:] = [item for item in value if not (isinstance(item, dict) and not item)]
#                 if not value:
#                     del current[key]
#     if dct:
#         print(dct)
#         return dct

# def clear_json(dct: dict) -> dict | None:
#     for key, value in list(dct.items()):
#         if isinstance(value, dict):
#             clear_json(value)
#             if not value:
#                 del dct[key]
#         elif isinstance(value, list):
#             for item in value:
#                 if isinstance(item, dict):
#                     clear_json(item)
#             value[:] = [item for item in value if not (isinstance(item, dict) and not item)]
#             if not value:
#                 del dct[key]
#     if dct:
#         return dct

# def clear_json(b: dict) -> dict | None:
#     for c, d in list(b.items()):
#         if isinstance(d, dict):
#             clear_json(d)
#             if not d:
#                 del b[c]
#         elif isinstance(d, list):
#             for e in d:
#                 if isinstance(e, dict):
#                     clear_json(e)
#             d[:] = [e for e in d if not (isinstance(e, dict) and not e)]
#             if not d:
#                 del b[c]
#     if b:
#         print(b)
#         return b

# def clear_json(json_dict):
#     # Проходим по каждому ключу и значению в словаре
#     for key, value in list(json_dict.items()):
#         # Если значение является словарем, вызываем функцию clear_json рекурсивно для этого словаря
#         if isinstance(value, dict):
#             clear_json(value)
#             # Если словарь пустой, удаляем его из родительского словаря
#             if not value:
#                 del json_dict[key]
#         # Если значение является списком, проходим по каждому элементу списка
#         elif isinstance(value, list):
#             for item in value:
#                 # Если элемент является словарем, вызываем функцию clear_json рекурсивно для этого словаря
#                 if isinstance(item, dict):
#                     clear_json(item)
#             # Используем срез списка value[:] для изменения списка на месте
#             # Удаляем пустые словари из списка, используя генератор списков
#             value[:] = [item for item in value if not (isinstance(item, dict) and not item)]
#             # Если список пустой, удаляем его из родительского словаря
#             if not value:
#                 del json_dict[key]
#     # Возвращаем очищенный словарь
#     if json_dict:
#         return json_dict

from json import loads


def delete_empty_pairs(data):
    match data:
        case dict():
            data = {k: delete_empty_pairs(v) for k, v in data.items() if v}
            res = {k: v for k, v in data.items() if v}
        case list():
            data = [delete_empty_pairs(v) for v in data if v]
            res = [v for v in data if v]
        case _:
            return data
    if res:
        return res



# print(clear_json(loads(input())))

# assert(delete_empty_pairs(json.loads('{"a": {}}')) is None)
assert(delete_empty_pairs(json.loads('{"a": {"b":{}, "c": 1}}')) == {"a":{"c": 1}})
assert(delete_empty_pairs(json.loads('{"a": {"b":{}, "c": 1, "e":[1, {"f":[]}]}}')) == {"a":{"c": 1, "e": [1]}})
assert(delete_empty_pairs(json.loads('{"a": {"b":{}, "c": 1, "e":[1, {"f": {"g":{}}}]}}')) == {"a":{"c": 1, "e": [1]}})
print([json.loads('{"a": {"b":{}, "c": 1, "e":[1, {"f":[]}]}}')])