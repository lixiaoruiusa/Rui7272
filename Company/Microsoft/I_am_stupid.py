# from collections import OrderedDict
#
# od=OrderedDict()
#
# od['k1']='egon'
# od['k2']='tom'
# od['k3']='jack'
# print(od)
# print(od.pop("k3"))
# print(od)
# print(od.popitem())
# print(od)
# # print(od.popitem(last=False))

# result = []
# if result is None:
#     print("n")

a = 3
b = 3
result = []
if a == b:
    while a:
        result.append("a")
        result.append("b")
        a -= 1
print("".join(result))