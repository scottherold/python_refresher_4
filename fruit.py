# even more fun with dictionaries

fruit = {"orange": "a sweet, orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage": "every child's favorite",
       "sprouts": "mmmm, lovely",
       "spinach": "can I have more fruit, please"}

print(veg)

# # this combines the two dictionaries
# # update changes the original dictionary
# veg.update(fruit)
# print(veg)

# to mutatue the dictionary (create a new version), use .copy()
# then update the newly created dictionary.
nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)
print(veg)
print(fruit)