shopping_list = []

def display_name():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list

    while True:
        display_name()
        break
    choice = input("Enter Your choice: ")

    if choice == 1:
        item = input("what do you want to add ")
        return shopping_list.append(item)
    elif choice == 2:
        item = input("what do you want to remove ")
        if (item in shopping_list):
            return shopping_list.remove(item)
        else:
            print(f"{item} not found")
    elif choice == 3:
        print(shopping_list)
    elif choice == 4:
        print("Goodbye!")
    else:
        print(f"cant find your choice {choice}")


main()