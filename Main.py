from Remove_chores import Completed_chores

user_name = input("What's your name?")
print()
print(f"Welcome {user_name}, please choose from the MENU")
print("1. Add Chore")
print("2. Check Chores")
print("3. Remove Chore")
print("4. Finished Chore")
print("5. What's done?")
print()

completed_chores = Completed_chores(user_name)

while True:
    user_input = input("(Enter your option by number)")
    if user_input == "1":
        user_inp = input("What are you adding: ")
        completed_chores.add_chores(user_inp.lower())
        print()
    elif user_input == "2":
        completed_chores.check_list()
        print()
    elif user_input == "3":
        user_inp = input("What are you removing: ")
        completed_chores.remove_chore(user_inp.lower())
        print()
    elif user_input == "4":
        user_inp = input("What did you finish: ")
        completed_chores.finished_chore(user_inp.lower())
        print()
    elif user_input == "5":
        completed_chores.left_over_chores()
        print()
    else:
        print("You stupid son of a bit** put a number that you learned at school")
        print("Or you never went to one??!!!!!!!!!!")
        print()




