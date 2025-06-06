# Write a function is_subsequence() that takes in a list of integers lst and a list of integers sequence as parameters. Given these two lists, determine whether the sequence list is a subsequence of the lst list. A subsequence of a list is a set of numbers that aren't necessarily adjacent but are in the same relative order as they appear in the list. Return True if sequence is a subsequence, and False otherwise.

# def is_subsequence(lst, sequence):
#     pass
# Example Usage:

# lst = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]
# print(is_subsequence(lst, sequence))
# Example Output: True

# def is_subsequence(lst, sequence):
#     counter = 0
#     sequenceCounter = len(sequence)
#     for value in lst:
#         for seqValue in sequence:
#             if value == seqValue:
#                 counter+=1
    
#     return counter == sequenceCounter

# lst = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]

# print(is_subsequence(lst, sequence))



# Write a function create_dictionary() that takes in a list of keys and a list of values as parameters. The function returns a dictionary where each item in keys is paired with a corresponding item in values.

# keys[i] should be paired with values[i] in the dictionary where 0 <= i <= len(keys). You may assume keys and values are the same length.

# def create_dictionary(keys, values):
#     pass
# Example Input:

# keys = ["peanut", "dragon", "star", "pop", "space"]
# values = ["butter", "fly", "fish", "corn", "ship"]
# Example Output:

# # {"peanut": "butter", "dragon": "fly", "star": "fish", "pop": "corn", "space": "ship"}

# def create_dictionary(keys, value):
#     index = 0
#     d = {}
#     for Keys in keys:
#         d[Keys] = value[index]
#         index+=1
#     return d



# keys = ["peanut", "dragon", "star", "pop", "space"]
# values = ["butter", "fly", "fish", "corn", "ship"]

# print(create_dictionary(keys, values))




# Write a function print_pair() that takes in a dictionary dictionary and a key target as parameters. The function looks for the target and when found, it prints the key and it's associated value as "Key: <key>" followed by "Value: <value>". If target is not in dictionary, print "That pair does not exist!".

# def print_pair(dictionary, target):
#     pass
# Example Usage:

# dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
# print_pair(dictionary, "patrick")
# print_pair(dictionary, "plankton")
# print_pair(dictionary, "spongebob")
# Example Output:

# Key: patrick
# Value: star
# That pair does not exist!
# Key: spongebob
# Value: squarepants


# def print_pair(dictionary, target):


#     if dictionary.get(target) != None:
#         print("Key: ", target)
#         print("Value: ", dictionary[target])
#     else:
#         print("That pair does not exist!")

# dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
# print_pair(dictionary, "patrick")
# print_pair(dictionary, "plankton")
# print_pair(dictionary, "spongebob")



# Write a function keys_v_values() that takes in a dictionary dictionary whose keys and values are both integers. The function should find the sum of all keys in the dictionary and the sum of all values.
# If the sum of all keys is greater than the sum of all values, the function should return the string "keys".
# If the sum of all values is greater than the sum of all keys, the function should return the string "values".
# If keys and values have equal sums, the function should return the string "balanced".

# def keys_v_values(dictionary):
#     pass
# Example Usage:

# dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
# greater_sum = keys_v_values(dictionary1)
# print(greater_sum)

# dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
# greater_sum = keys_v_values(dictionary2)
# print(greater_sum)
# Example Output:

# values
# keys

def keys_v_values(dictionary):
    keyCounter = 0
    valueCounter = 0

    for keys in dictionary:
        keyCounter += keys
    for values in dictionary:
        valueCounter += dictionary.get(values)

    if keyCounter > valueCounter: 
        s = "keys"
        return s
    
    elif keyCounter < valueCounter:
        s = "value"
        return s
    
    elif keyCounter == valueCounter:
        s = "balanced"
        return s
    
dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)
        







        


