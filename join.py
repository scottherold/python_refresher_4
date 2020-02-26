# fun with string joins
myList = ["a", "b", "c", "d"]
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "123456789"

newString = ''

# concatenates myList to newString varaible
# this also solves the problem with the trailing comma
newString = " mississippi ".join(numbers)

print(newString)