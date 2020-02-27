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

print("=" * 40)

# updated difference
# this with modify the original set instead of transmuting a new set
print(sorted(even))
print(squares)
even.difference_update(squares)
print(sorted(even))

print("=" * 40)

# symmetric difference
# this is all the memebers that are in one set, or another, but not both
even = set(range(0, 40, 2))
print(sorted(even))
print(sorted(squares))

print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))

print("\nsymmetric squares minus even")
print(squares.symmetric_difference(even))

print("=" * 40)

# symmetric difference update
# this is like symmetric difference, but like update difference, it
# modifies the original set, instead of mutates a new set
print(sorted(even))
print(squares)
even.symmetric_difference_update(squares)
print(sorted(even))

print("=" * 40)

# discard and remove
# There are two methods for removing data from sets, discard() and
# remove()
squares.discard(4)
squares.remove(16)
squares.discard(8) # does, nothing
print(squares)

# you should use a conditional when using remove() in order to avoid
# throwing an error if the data is not present
if 8 in squares:
    squares.remove(8)

# you can also use a try block, and throw an exception if the data is
# not present
try:
    squares.remove(8)
except KeyError:
    print("The item 8 is not a member of the set")

print("=" * 40)

# subset and superset
squares = set(squares_tuple)
print(even)
print(squares)

if squares.issubset(even):
    print("squares is a subset of even")

if even.issuperset(squares):
    print("even is a superset of sqaures")

# frozen set
# frozen sets are immutable sets
even = frozenset(range(0, 100, 2))
print(even)