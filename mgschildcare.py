def drop_off():
    child_name = input("Enter the name of the child: ")
    roll.append(child_name)


def pick_up():
    child_name = input("Enter the name of the child you want to pick up: ")
    if child_name in roll:
        roll.remove(child_name)
        print(f"{child_name} has been removed from the roll.")
    else:
        print("Sorry, we have no child by that name")


def calc_cost(number):
    rate = 12.00
    hours = int(input("How many hours to charge for: "))
    cost = number * hours * rate
    print(f"The cost for {number} of children for {hours} hours is ${cost}")


def print_roll():
    print("Children currently staying with MGS Childcare: ")
    for child in roll:
        print(f"\t{child}")
    print()


def end_program():
    print("Goodbye!")


roll = []

print(
    "---------------------------------------------------------")
print("Welcome to the MGS Childcare service!")
print("What would you like to do? Please choose one of the items below")
print(
    "---------------------------------------------------------")

choice = 0
while choice != 5:
    print("What do you want to do?")
    print()
    print("1 Drop off a child")
    print("2 Pick up a child")
    print("3 Calculate cost")
    print("4 Print child roll")
    print("5 Exit the system")
    print()
    print("=========================================================")

    choice = int(input("Enter your choice (number between 1 and 5): "))
    if choice == 1:
        drop_off()

    elif choice == 2:
        pick_up()

    elif choice == 3:
        calc_cost(len(roll))

    elif choice == 4:
        print_roll()

    elif choice == 5:
        end_program()

    else:
        print("Must be an integer between 1 and 5!")
