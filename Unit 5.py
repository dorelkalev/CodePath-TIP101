# # Step 1: Copy the following code into Replit.

# # Step 2: Add a line of code (outside of the class) to instantiate an instance of the class Pokemon and store it in a variable named my_pokemon. The Pokemon instance created should have name "Pikachu" and its types should be ["Electric"].

# class Pokemon:
#     def __init__(self, name, types):
#         self.name = name
#         self.types = types
#         self.is_caught = False

# my_pokemon = Pokemon("Pikachu", ["Electric"])

# # Step 1: Add the print_pokemon definition below to your code on Replit.

# # Step 2: Instantiate an instance of the class Pokemon and store it in a variable named squirtle. The Pokemon instance created should have name "Squirtle" and its types should be ["Water"].

# # Step 3: Call the method print_pokemon() on your new Pokemon instance squirtle.

# class Pokemon:
#     def __init__(self, name, types):
#         self.name = name
#         self.types = types
#         self.is_caught = False

#     def print_pokemon(self):
#         print({
#             "name": self.name,   # Output: "name": "Squirtle",
#             "types": self.types, # Output: "types": ["Water"],
#             "is_caught": self.is_caught # Output: "is_caught": False
#         })

# squirtle = Pokemon("Squirtle", ["Water"])
# squirtle.print_pokemon()

# # Using your code from Problem 2, update your squirtle Pokemon so that is_caught is updated to True. Use the print_pokemon() function to verify that squirtle's is_caught property was updated.

# # Expected Output:

# # {
# #     "name": "Squirtle",
# #     "types": ["Water"],
# #     "is_caught": True
# # }

# squirtle.is_caught = True
# squirtle.print_pokemon()

# # Update the Pokemon class with a new method catch() that takes in no parameters except self.

# # The method should update the Pokemon's is_caught attribute to True and not return any value.

# # class Pokemon():
# # 	...
	
# # 	def catch(self):
# # 		pass
# # Example Usage:

# # my_pokemon = Pokemon("rattata", ["Normal"])
# # my_pokemon.print_pokemon()

# # my_pokemon.catch()
# # my_pokemon.print_pokemon()
# # Example Output:

# # {
# #     "name": "Rattata",
# #     "types": ["Normal"],
# #     "is_caught": False
# # }

# # {
# #     "name": "Rattata",
# #     "types": ["Normal"],
# #     "is_caught": True
# # }

# class Pokemon():
#     def __init__(self, name, types):
#         self.name = name
#         self.types = types
#         self.is_caught = False

#     def print_pokemon(self):
#         print({
#             "name": self.name,   # Output: "name": "Squirtle",
#             "types": self.types, # Output: "types": ["Water"],
#             "is_caught": self.is_caught # Output: "is_caught": False
#         })
        
#     def catch(self):
#         self.is_caught = True
            
# my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.catch()
# my_pokemon.print_pokemon()

# Update the Pokemon class with a new method choose() that takes in no parameters except self.

# If the Pokemon is caught, the method should print the string "<Pokemon name> I choose you!".

# Otherwise, it should print "<Pokemon name> is wild! Catch them if you can!".

# class Pokemon():
# 	...
	
# 	def choose(self):
# 		pass
# Example Usage:

# my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.choose()
# my_pokemon.catch()
# my_pokemon.choose()
# Example Output:

# {
#     "name": "Rattata",
#     "types": ["Normal"],
#     "is_caught": False
# }

# Rattata is wild! Catch them if you can!
# Rattata I choose you!

# class Pokemon():
#     def __init__(self, name, types):
#             self.name = name
#             self.types = types
#             self.is_caught = False

#     def print_pokemon(self):
#         print({
#             "name": self.name,   # Output: "name": "Squirtle",
#             "types": self.types, # Output: "types": ["Water"],
#             "is_caught": self.is_caught # Output: "is_caught": False
#         })
        
#     def catch(self):
#         self.is_caught = True
            
#     def choose(self):
#         if self.is_caught == True:
#             print(self.name + " I choose you!")
#         else:
#             print(self.name + " is wild! Catch them if you can!")
            


        
# # Example Usage:

# my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.choose()
# my_pokemon.catch()
# my_pokemon.choose()



# Update the Pokemon class with a new method add_type() that takes in a string new_type as a parameter.

# It should add new_type to the Pokemon's list of types.

# class Pokemon():
# 	...
	
# 	def add_type(self, new_type):
# 		pass
# Example Usage:

# jigglypuff = Pokemon("Jigglypuff", ["Normal"])
# jigglypuff.print_pokemon()

# jigglypuff.add_type("Fairy")
# jigglypuff.print_pokemon()
# Example Output:

# {
#     "name": "Jigglypuff",
#     "types": ["Normal"]
#     "is_caught": False
# }

# {
#     "name": "Jigglypuff",
#     "types": ["Normal", "Fairy"]
#     "is_caught": False
# }

#class Pokemon():
#     def __init__(self, name, types):
#             self.name = name
#             self.types = types
#             self.is_caught = False

#     def print_pokemon(self):
#         print({
#             "name": self.name,   # Output: "name": "Squirtle",
#             "types": self.types, # Output: "types": ["Water"],
#             "is_caught": self.is_caught # Output: "is_caught": False
#         })
        
#     def catch(self):
#         self.is_caught = True
            
#     def choose(self):
#         if self.is_caught == True:
#             print(self.name + " I choose you!")
#         else:
#             print(self.name + " is wild! Catch them if you can!")
            
	
#     def add_type(self, new_type):
#         self.types.append(new_type)
	
# jigglypuff = Pokemon("Jigglypuff", ["Normal"])
# jigglypuff.print_pokemon()

# jigglypuff.add_type("Fairy")
# jigglypuff.print_pokemon()



# Write a function add_first() that takes in a head of a linked list and a new_node from the Node class as parameters.

# It should insert new_node as the new head of the linked_list. The function returns new_node.

# Note: The "head" of a linked list is the first element in the linked list. Equivalent to lst[0] of a normal list.

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next
		
		
# def add_first(head, new_node):
# 	pass
# Example Usage:

# # Using the Linked List from Problem 2
# print(node_1.value, "->", node_1.next.value)

# new_node = Node("Ditto")
# node_1 = add_first(node_1, new_node)

# print(node_1.value, "->", node_1.next.value)
# Example Output:

# Jigglypuff -> Wigglytuff 
# Ditto -> Jigglypuff

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
		

def add_first(head, new_node):
	head.next = head
	head = new_node
	

# Using the Linked List from Problem 2
node_1 = Node("Jigglypuff")

print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)

print(node_1.value, "->", node_1.next.value)
