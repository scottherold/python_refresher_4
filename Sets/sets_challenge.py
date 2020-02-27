# Create a program that takes some text and returns a list of all the 
# characters in the text that are not vowels, sorted in alphabetical
# order

# you can either enter the text from the keyboard or initialize a string
# variable with the string

# string input
input_string = input("Please enter a string: ").upper()

# string scrub to remove numbers
letter_string = ''.join([i for i in input_string if not i.isdigit()])

# conver to set
input_letter_set = set(letter_string)

# vowel set -- immutable
vowels = frozenset("AEIOU ")

# output
print(sorted(input_letter_set.difference(vowels)))