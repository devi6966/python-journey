mynames=["devi","chinku","tiki","chinka","sakuni",3]
print(mynames)

numbers=[1,21,13,7,5,16]
print(numbers)
numbers.sort()
numbers.reverse()
print(numbers)

#LIST SLICING
#numbers[start:stop]

print(numbers[:])
print(numbers[1:5])

#EXTENDED SLICING
#numbers[start:stop:step]

print(numbers[::])
print(numbers[1::2])
print(numbers[1:6:2])

#NEGATIVE EXTENDED LIST SLICING
print(numbers[6:1:-1])
print(numbers[::-1])
print(numbers[::-2])

#SOME SPECIAL FUNCTIONS
num = [75,3,9,25,11,48,11]
num.append("devi") #Add new object at the end
num.insert(1,12) #Adds a new item at the given index without replacing any existing item
num.remove(11) #Remove using value
print(num.pop(6)) #Remove using index and return the removed item.
num[2]=7 #Replace tha value of that exact index
print(num)
b=num.copy()# copy() -> Returns a shallow copy of the list
print(b)