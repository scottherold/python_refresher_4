# data
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = { 0: {"Q": 0},
          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
          2: {"N": 5, "Q": 0},
          3: {"W": 1, "Q": 0},
          4: {"N": 1, "W": 2, "Q": 0},
          5: {"W": 2, "S": 1, "Q": 0}}

vocabulary = { "QUIT": "Q",
               "NORTH": "N",
               "SOUTH": "S",
               "EAST": "E",
               "WEST": "W"}

# split() is used to split strings
# by default, split() splits at the space, unless a delimiter is
# provided
# print(locations[0].split())
# print(locations[3].split(","))
# print(' '.join(locations[0].split()))

# default location
loc = 1

# game starts
while True:
    # creates available exits based on location
    availableExits = ", ".join(exits[loc].keys())
    
    print(locations[loc])

    # exit game
    if loc == 0:
        break

    # provides available exits
    direction = input("Avaible exits are " + availableExits+ " ").upper()
    print()

    # Parse user input, using our vocabulary dictionary if necessary
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            # will take the first word found in the user input, if in
            # the vocabulary dictionary
            if word in vocabulary:
                direction = vocabulary[word]
                break

    # check if directional key exists
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")