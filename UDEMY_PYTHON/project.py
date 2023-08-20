# ---->>>> Greeting Project <<<<-----
# WAP that input to prompt a user for their name & then welcome them.

name=input("Enter your name: ")
print(f'Hello {name}.')
print(f'Welcome to the Python')

# ------------ PROJECT 2: -----------------
# ------>>>>> Group Name Generator <<<<------
#     1. Create a gretting to the program.
#     2. Ask the user to their favourite color.
#     3. Ask the user to the favourite animal.
#     4. Combine the name of their favourite color and animal and show them their group.

print("Welcome to the Group Name Generator.")
color=input("What's your favourite color?\n").capitalize()
animal=input("What's your favourite animal?\n").capitalize()
print(f"Your group name could be {color} {animal}s")