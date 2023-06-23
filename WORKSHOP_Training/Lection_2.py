# # # list_1 = []
# # # list_2 = list()
# # # list_3 = [1, 2, 3, 4]
# # # list_3 = [1, 2, 3, 4]

# # # print(list_1)
# # # print(list_2)
# # # print(*list_3)

# # # for i in list_3:
# # #     print(i)

# # # print(list_3[-2])

# # # list_4 = [1, 5]
# # # print(*list_4)
# # # list_4.append(8)
# # # print(*list_4)
# # # list_4.append(85)
# # # print(*list_4)

# # # list_1 =  []
# # # print(list_1)
# # # for i in range(5):
# # #     list_1.append(i)
# # #     print(*list_1)

# # list_2 = [12, 7, -1, 21, 0, 256, 65, 489, 23, 56]
# # print(list_2)
# # # print(list_2.pop())
# # # print(list_2)
# # # print(list_2.pop())
# # # print(list_2)
# # # print(list_2.pop())
# # # print(list_2)
# # # print(list_2.pop(0))
# # # print(list_2)
# # # print(list_2.insert(2, 11))
# # # print(list_2[2:5:2])
# # print(list_2[2:len(list_2)+2:2])

# # # t = (1, )
# # # print(type(t))

# # v = [1, 8, 9]
# # print(type(v))
# # print(v)

# # v = tuple(v)
# # print(type(v))
# # print(v)

# # a,b,c = v

# # print(a, b, c)

# t = [1, 2, 3, 5,]

# print(t[3])

# # for i in range(len(t)):
# #     print(t[i])

# t[0] = 56
# print(t[0])

# for i in range(len(t)):
#     print(t[i])

# d = {}
# d = dict()

# d['q'] = 'qwerty'
# print(d)

# d['w'] = 'werty'
# print(d['q'])

# dictionary = {}
# dictionary = {'left': '←', 'right': '→', 'up': '↑', 'down': '↓'}
# print(dictionary['left'])

# del(dictionary['left'])
# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()
print(c)
u = a.union(b)
print(u)
i = a.intersection(b)
print(i)
d1 = a.difference(b)
print(d1)
dr = b.difference(a)
print(dr)
q = a.union(b).difference(a.intersection(b))
print(q)

a = {1, 3, 777}

b = frozenset(a)

print(b)

list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1)

list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1)