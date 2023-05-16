# import collections.abc as coll
#
# class c(coll.Generator()):
#     def send(self, message):
#         pass
#
#     def throw(self, value):
#         pass
#
# print(type(c))


# print(("NO", "YES")[sum((a:=sorted(list(int(input()) for _ in range(3))))[:2])>a[2]])


lst = [input() for _ in range(4)]

for i in range(len(lst)):
    lst[i] = lst[i].replace('+7','8').replace('-','').replace('(','').replace(')','')
    lst[i] = (lst[i][-7:-1], lst[i][1:4] if len(lst[i]) > 8 else '495')
    if i > 0:
        print(('NO', 'YES')[lst[0] == lst[i]])