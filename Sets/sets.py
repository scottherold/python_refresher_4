# fun with sets!
# sets are like dictionaries, but do not contain values
# the keys are still hashed like dictionary values
farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("=" * 40)

# sets can also be created by passing a list as an argument to the 
# set() constructor
wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

# you can append information to sets using the set.add() method
farm_animals.add("horse")
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)

# you can create an empty set by not passing any arguments to the set()
# function
empty_set = set()

# This creates an empty dictionary, so it is why you need to use the 
# set() function
empty_set_2 = {}

# you can pass any sequence into a set() as an argument
# range example
even = set(range(0, 40, 2))
print(even)

# tuple example
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)