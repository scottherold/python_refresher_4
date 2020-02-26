# more dictionary fun
fruit = {"orange": "a sweet, orange citrus fruit",
            "apple": "good for making cider",
            "lemon": "a sour, yellow citrus fruit",
            "grape": "a small, sweet fruit growing in bunches",
            "lime": "a sour, green citrus fruit"}

print(fruit)

# # prints all keys
# fruit_keys = fruit.keys()
# print(fruit_keys)

# # adds a new key/value pair to the dictionary
# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)

print(fruit)

# produces a tuple of dictionary key/value pairs
print(fruit.items())

# converts data into tuple
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

# You can also create a dictionary from a tuple using the dict()
# function
print(dict(f_tuple))