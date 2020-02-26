# data -- refactored into a single dictionary
locations = {0: {"desc": "You are sitting in front of a computer learning Python",
                 "exits": {},
                 "namedExits": {}},
             1: {"desc": "You are standing at the end of a road before a small brick building",
                 "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                 "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}},
             2: {"desc": "You are at the top of a hill",
                 "exits": {"N": 5, "Q": 0},
                 "namedExits": {"5": 5}},
             3: {"desc": "You are inside a building, a well house for a small stream",
                 "exits": {"W": 1, "Q": 0},
                 "namedExits": {"1": 1}},
             4: {"desc": "You are in a valley beside a stream",
                 "exits": {"N": 1, "W": 2, "Q": 0},
                 "namedExits": {"1": 1, "2": 2}},
             5: {"desc": "You are in the forest",
                 "exits": {"W": 2, "S": 1, "Q": 0},
                 "namedExits": {"2": 2, "1": 1}}
            }

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
# refactored to utilize nested dictionaries
while True:
    # creates available exits based on location
    availableExits = ", ".join(locations[loc]['exits'].keys())
    
    print(locations[loc]['desc'])

    # exit game, else combine both exits dictionaries
    if loc == 0:
        break
    else:
        # creates copy of the exits dictionary
        allExits = locations[loc]['exits'].copy()
        allExits.update(locations[loc]['namedExits'])
    
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