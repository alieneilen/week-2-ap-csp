
# ----------------------------------------
# . Working with Strings
# ----------------------------------------

# Strings are sequences of characters enclosed in quotes (' ' or " ")
# greeting = "Hello"
# name = "World"

# # ----------------------------------------
# # Basic String Operations
# # ----------------------------------------

# # 1. Concatenation: Combining strings using the + operator
# message = greeting + " " + name
# print("Concatenated String:", message)  # Output: Hello World

# ----------------------------------------
# 2. String Functions
# ----------------------------------------

# phrase = "Python is FUN!"
# name= "EILEN" 
# # Convert all characters to lowercase
# print("Lowercase:", phrase.lower())  # Output: python is fun!
# print ("Lowercase name:", name.lower())
# # Convert all characters to uppercase
# print("Uppercase:", phrase.upper())  # Output: PYTHON IS FUN!
# print("Uppercase name:", name.capitalize)
# # # Check if all characters are uppercase
# print("Is Uppercase?", phrase.isupper())  # Output: False
# print("Is Uppercase?", name.isupper())
# # # Find the length of the string
# # print("Length of phrase:", len(phrase))  # Output: 14

# # # ----------------------------------------
# # # 3. Indexing and Slicing
# # # ----------------------------------------
# chicago_mayor = "Johnson" #this is a string variable. it is a word. 
# # want to print the first letter fo the mayor
# print("First letter of mayor's name:", chicago_mayor[0])
# #it will give you the J because 0 means the first character of the string
# print("Last letter of mayor's name:", chicago_mayor[-1])
# #get Jogn
# print ("First four letters of mayor's name", chicago_mayor[0:4])
#  # first number is inclusive. so 0 will print J. The second number is exclusive. 4 will not print the fourth value. It will NOT print the 4th and stop at the 3rd. 
# print ("Last three letters of mayor's name", chicago_mayor[-3:])
# last_name = "Medina"
# print ("Print last three character of last name", last_name[3:])
# print("First letter of last name", last_name[0])
# #----------------------------
# poppings = "supercalifragilisticexpialidocious"
# print ("Print Docious:", poppings[-7:])
# print ("Uppercase:", poppings.upper())
# print ("Print out super:", poppings[0:5])

# #will give you the length of "poppins"
# print (len(poppings)) #output:34
# declaration_of_independance = "When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation."
# #indexing: Acces characters by position 
# print ("first character:", phrase[0])


# # Indexing: Access characters by position (0-based index)
# print("First character:", phrase[0])  # Output: P
# print("Last character:", phrase[-1])  # Output: !

# # Slicing: Get a range of characters (start inclusive, end exclusive)
# print("Characters 1 to 4:", phrase[1:4])  # Output: yth

# # Example combining everything:
# print("Formatted Example:", (greeting + " " + name + "!").upper())
# # Output: HELLO WORLD!


# # ----------------------------------------
# # 7. Strings: Advanced Concepts
# # ----------------------------------------

# # Creating Strings: use single or double quotes
# greeting1 = 'Hello'
# greeting2 = "Hi there"

# # Printing Strings
# print(greeting1)
# print(greeting2)

# # ----------------------------------------
# # String Methods
# # ----------------------------------------

sentence = "Python is fun to learn"

# .split(): Splits the string into a list of words
words = sentence.split()
print("Split result:", words)
words2 = sentence.join("")
print (words2)

# .format(): Allows inserting values into strings using {}
name = "Marvin"
age = 35
intro = "My name is {} and I am {} years old.".format(name, age)
print(intro)

# You can also use f-strings (Python 3.6+)
intro_fstring = f"My name is {name} and I am {age} years old."
print(intro_fstring)
