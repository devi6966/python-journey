var1="helloo jii its me"
var2=7
var3=5.5
var4="\tdevi"

#print values inside variable
print(var1,var2,var3)

#print type of data store in that variable
print(type(var1),type(var2),type(var3))

#add 2 variable
print(var1 + var4)
print(var2 - var3)

'''
int()
float() All these are used to switch variable type
str()
'''
var10= "20"
var40="80"
print(int(var10) + int(var40))
print(100 * str(int(var10) + int(var40))) # it'll print "100" 100 times
print(100 * (int(var10) + int(var40))) #o/p-->10000
print(100 * int(var10) + int(var40)) #o/p = 2080

print("Enter a random number:")
var_store = input()
print("You choose/type number is:",var_store)#store as a string
print("You choose/type number is:",int(var_store)+10)#Converts input to int temporarily and adds 10

