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

# used for location --> location movement, instead of directional input
namedExits = { 1: {"2": 2, "3": 3, "5": 5, "4": 4},
               2: {"5": 5},
               3: {"1": 1},
               4: {"1": 1, "2": 2},
               5: {"2": 2, "1": 1} }

# Use numbers for word versions of locations
# This is done to map directions for location --> location, since
# the location name may not always be in the same direction
vocabulary = { "QUIT": "Q",
               "NORTH": "N",
               "SOUTH": "S",
               "EAST": "E",
               "WEST": "W",
               "ROAD": "1",
               "HILL": "2",
               "BUILDING": "3",
               "VALLEY": "4",
               "FOREST": "5"}

# default location
loc = 1

# game starts
while True:
    # creates available exits based on location
    availableExits = ", ".join(exits[loc].keys())
    
    print(locations[loc])

    # exit game, else combine both exits dictionaries
    if loc == 0:
        break
    else:
        # creates copy of the exits dictionary
        allExits = exits[loc].copy()
        allExits.update(namedExits[loc])
    
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
    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go in that direction")