# Create a function which concatenates the number 7 to the end of every chord in a list. Ignore all chords which already end with 7.

# Examples:
# jazzify(["G", "F", "C"]) ➞ ["G7", "F7", "C7"]

# jazzify(["Dm", "G", "E", "A"]) ➞ ["Dm7", "G7", "E7", "A7"]

# jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]) ➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]

# jazzify([]) ➞ []

# Notes:
# Return an empty list if the given list is empty.
# You can expect all the tests to have valid chords.


def jazzify(lst): 
	for i in range(len(lst)):
			if not lst[i].endswith('7'):
				lst[i] = lst[i] + '7'
	return lst

print(jazzify(["G", "F", "C"]))
print(jazzify(["Dm", "G", "E", "A"]))
print(jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]))
print(jazzify([]))