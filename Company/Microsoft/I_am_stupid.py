from collections import OrderedDict

od=OrderedDict()

od['k1']='egon'
od['k2']='tom'
od['k3']='jack'
print(od)
print(od.pop("k3"))
print(od)
print(od.popitem())
print(od)
# print(od.popitem(last=False))