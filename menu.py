'''
Menu structure that can be used in Python
- Display options
- Prompt user (string)
- run appropriate option / or prompt again
'''


# In the assessment you'd need to authenticate first

# Café ordering option
# Variable for user prompting
user_choice = "" # Give it an empty value

while user_choice != "4":   # will change when menu is displayed
    print("""Welcome to the café
1 - Coffee
2 - Croissant
3 - Wine
4 - Exit the café""")
    
    # That's where we actually set up the variable
    # For user selection
    user_choice = input("What is your selection?")

    # Main match case
    match user_choice:
        case "1":
            option1()
        case "2":
            option2
        case "3":
            option3
        case "4":
            print("You chose to quit. Bye.")
        case _:
            print("You have not entered a valid option.")

# For each case you can set up a function
def option1():
    pass

def option2():
    pass

def option3():
    pass