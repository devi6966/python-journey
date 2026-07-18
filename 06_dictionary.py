#Dictionary is key-value pairs

d1 = { }
print(type(d1))

d2 = { "devi":"paneer" , "spandan":"lays" }
print(d2)

d3 = {"rudra":"rice","subham":{"breakfast":"bread","lunch":"roti","dinner":"paratha"}}
print(d3["subham"])
print(d3["subham"]["lunch"])

d4={"jayanti":[1,2,3,4],"baba":(12,11,18,93)}
print(type(d4["jayanti"]))
print(type(d4["baba"]))
d4["dibya"] = "soyabin"
print(d4)
del d4["dibya"]
print(d4)
print(d4.items())
#FUNCTIONS OF DICTIONARY
for value in d4.values():
    print(value)
for key in d4.keys():
    print(key)
for key,value in d4.items():
    print(key,"=",value)
