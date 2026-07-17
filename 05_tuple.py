'''
Tuple is an ordered and immutable collection of items.

✅ Ordered
✅ Allows duplicate values
❌ Cannot be modified (Immutable)
'''

tup=(11,) # A single-element tuple must have a trailing comma
print(type(tup))

tp = (7,6,88,12,19)
print(tp)
print(len(tp))
print(tp.count(12))# count() -> Returns how many times a value appears
print(tp.index(12))# index() -> Returns the index of the first matching value
print(sum(tp))

t=(12,8,[7,18,45])#A list can be store inside a tuple
print(t)
t[2].pop(0)#A tuple is immutable but list inside a tuple can be modified
print(t)