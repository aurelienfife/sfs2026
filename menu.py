'''
Menu structure that can be used in Python
- Display options
- Prompt user (string)
- run appropriate option / or prompt again
'''

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
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            print("You chose to quit. Bye.")
        case _:
            print("You have not entered a valid option.")