# Using input to play with dictionaries

fruit = {"orange": "a sweet, orange citrus fruit",
            "apple": "good for making cider",
            "lemon": "a sour, yellow citrus fruit",
            "grape": "a small, sweet fruit growing in bunches",
            "lime": "a sour, green citrus fruit"}

print(fruit)

# user input to access a fruit
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break

#     # default values can be used if a dictionary key is not found
#     description = fruit.get(dict_key, "We don't have a " + dict_key)
#     # fruit.has_key(dict_key) -- This has been deprecated in python3
#     print(description)

#     if dict_key in fruit:
#         # uses the dictionary .get() method to access the value from the 
#         # provided key
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("we don't have a " + dict_key)

# # iterating through dictionary keys, but the order may not be the same
# for snack in fruit:
#     print(fruit[snack])

# # will print in order
# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print('-' * 40)

# # how to sort keys
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()

# # the above sort in a single line
# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

# this will reduce the code even further
for f in sorted(fruit.keys()):
    print(f + ' - ' + fruit[f])