Task = input("Enter your task ")
Priority = input("Priority (high, medium, low) ")
time_bound = input("Is it time-bound? ")

match Priority:
    case "high":
        if time_bound == "yes":
            print(f"{task_description}' is a high priority task that requires immediate attention today!")
        else:
            print("you still have time")
    case "meduim":
        if time_bound == "yes":
            print("Get involved")
        else:
            print("nothing to worry about")
    case "low":
        if time_bound == "yes":
            print("You still have to do it anyways")
        else:
            print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
        
