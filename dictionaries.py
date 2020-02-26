# fun with dictionaries

# dictionaries are like JavaScript objects; key/value pairs
fruit = {"orange": "a sweet, orange citrus fruit",
            "apple": "good for making cider",
            "lemon": "a sour, yellow citrus fruit",
            "grape": "a small, sweet fruit growing in bunches",
            "lime": "a sour, green citrus fruit",

            # if you assign a value to a key already used, python will
            # automatically use the last value assigned. For example
            # Python will use this value, instead of the value above
            "apple": "round and crunchy"}

# prints the entire dictionary
print(fruit)
print(fruit["lemon"])

# how to assign a new value to the dictionary
fruit["pear"] = "an odd shaped apple"

print(fruit)

# if you assign a new value to an existing key, it will overwrite the 
# existing value
fruit["lime"] = "great with tequila"
print(fruit)

# the del command removes an item from the dictionary
# if you forget to specify a key, the del command will delete the entire 
# dictionary
del fruit["lemon"]
print(fruit)

# will delete the entire dictionary
# del fruit

# the .clear() method will remove all data from the dictionary, but not
# delete the dictionary itself
fruit.clear()
print(fruit)