# # 6
# # 100
# # 1
# # 100
# # 1
# # 100
# # 1
# # 5
a = [10,10,5,10,8]
b = [1, 1, 1]
c = [3, 4]
d = [100,1,100,1,100,1]
#
# def good_str(lst: list[int]) -> int:
#     if len(lst) < 2:
#         return 0
#     tmp = min(lst)
#
#     lst1 = [i - tmp for i in lst]
#
#     lst_lst = []
#     tmp_lst = []
#     for i in lst1:
#         if i > 0:
#             tmp_lst.append(i)
#         elif i <= 0 < len(tmp_lst):
#             lst_lst.append(tmp_lst)
#             tmp_lst = []
#     return min(lst) * (len(lst) - 1) + sum(good_str(i) for i in lst_lst)
#
# print(good_str(a))
# print(good_str(b))
# print(good_str(c))
# print(good_str(d))

"""26
48
75
74
60
36
79
59
99
66
61
86
64
1
86
56
97
58
90
82
65
15
78
47
7
41
63"""
def good_str(lst: list[int]) -> int:
    if len(lst) < 2:
        return 0
    tmp = min(lst)

    lst1 = [i - tmp for i in lst]

    lst_lst = []
    tmp_lst = []
    for i in lst1:
        if i > 0:
            tmp_lst.append(i)
        elif i <= 0 < len(tmp_lst):
            lst_lst.append(tmp_lst)
            tmp_lst = []
    if 0 < len(tmp_lst):
        lst_lst.append(tmp_lst)

    return min(lst) * (len(lst) - 1) + sum(good_str(i) for i in lst_lst)

n = int(input())
print(good_str([int(input()) for i in range(n)]))
print(good_str(a))
print(good_str(b))
print(good_str(c))
print(good_str(d))