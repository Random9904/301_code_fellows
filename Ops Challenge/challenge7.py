# 10 fruits in a variable
fruits = ["apple", "banana", "cherry", "lime", "dragonfruit", "watermelon", "grape", "starfruit", "kiwi", "lemon"]

# Print 4th element: lime
# where apple is 1st element
print("Fourth element:", fruits[3])

# Print 6th to 10th: watermelon to lemon
print("Sixth through tenth elements:", fruits[5:])

# Change 7th element (grape) to onion
fruits[6] = "onion"
print("Add onion: ",fruits)

# append(): Adds an element to the end of the list
fruits.append("mango")
print("Add mango: ", fruits)

# copy(): Returns a shallow copy
fruits_copy = fruits.copy()
print("Show copy: ", fruits_copy)

# count(): Returns the number of times "apple" makes an appearance
number_of_apple = fruits.count("apple")
print("Number of apple: ", number_of_apple)

# extend(): Adds the fruits to end of the list
more_fruits = ["orange", "pear"]
fruits.extend(more_fruits)
print("Added fruits: ", fruits)

# index(): Returns the index of the first occurrence of "watermelon"
muh_watermelon = fruits.index("watermelon")
print("Watermelon at: ", muh_watermelon)

# insert(): Inserts "durian" at index 2
fruits.insert(2, "durian")
print("Added durian: ",fruits)

# pop(): Removes and returns the element at the specified position
removed_fruit = fruits.pop(5)
print("Removed: ", removed_fruit)

# remove(): Removes the first occurrence of "durian"
fruits.remove("durian")
print("Took out durian: ", fruits)

# reverse(): Reverses the order of the elements
fruits.reverse()
print("Reverse: ", fruits)

# sort(): Sorts the elements in ascending order
fruits.sort()
print("Sort: ", fruits)

# clear(): Removes all elements from the list
fruits.clear()