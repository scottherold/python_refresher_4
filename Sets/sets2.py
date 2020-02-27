even = set(range(0, 40, 2))
print(even)

print(len(even))

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)
print(len(squares))

# union
# this is how you combine two sets
# remember, values DO NOT DUPLICATE
print(even.union(squares))
print(len(even.union(squares)))

print(squares.union(even))
print(len(squares.union(even)))

print("-" * 40)

# intersects
# these are values that are present in both sets
print(even.intersection(squares))
print(even & squares)
print(squares.intersection(even))
print(squares & even)

print("-" * 40)

# sorting
print(sorted(even))
print(sorted(squares))

print("-" * 40)

# subracting
# subtracting set b from set a results in any data in set b, being
# being removed from set a
print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("\nsquares minus evens")
print(squares.difference(even))
print(squares - even)