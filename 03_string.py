mystr = "shivajii maharaj ki jay"

# STRING LENGTH
print(len(mystr))  # Gives the total number of characters in the string
print(type(mystr))

# STRING SLICING
# Syntax: [start:stop]

print(mystr[0:10])  # Prints characters from index 0 to 9
print(mystr[:20])    # If the start value is empty, Python starts from index 0
print(mystr[0:])     # If the stop value is empty, Python goes until the end
print(mystr[:])      # Prints the whole string
print(mystr[::])     # Prints the whole string with the default step value


# EXTENDED STRING SLICING
# Syntax: [start:stop:step]

print(mystr[0:20:2])  # Prints every 2nd character from index 0 to 19
print(mystr[0::3])     # Starts from index 0 and prints every 3rd character until the end


# REVERSE STRING SLICING

print(mystr[::-1])       # Reverses the whole string
print(mystr[::-2])       # Reverses the string and prints every 2nd character

print(mystr[-10:-2])     # Prints characters from index -10 to -3
print(mystr[-2:-10:-1])  # Prints characters in reverse from index -2 to -9


# STRING METHODS

print(mystr.isalnum())     # Checks if the string contains only letters and numbers
print(mystr.isalpha())     # Checks if the string contains only letters
print(mystr.isnumeric())   # Checks if the string contains only numbers
print(mystr.count("j"))    # Counts how many times "j" appears in the string
print(mystr.find("ki"))    # Gives the starting index of "ki" and gives -1 if it is not found
print(mystr.capitalize())  # Makes the first letter uppercase and the remaining letters lowercase
print(mystr.upper())       # Converts all letters into uppercase
print(mystr.lower())       # Converts all letters into lowercase


# There are many more interesting string methods to explore :)