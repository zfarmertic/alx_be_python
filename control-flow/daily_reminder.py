task = input("Enter your task: ")
priority = input("Priority (high, medium, low): ")
time-bound = input("Is it time-bound? (yes/no): ")

is_time_bound = " "
priority_msg = " "

match priority:
    case 'high':
        priority_msg = f"Task {task} is {priority} priority"
    case 'medium':
        priority_msg = f"Task {task} is {priority} priority"
    case 'low':
        priority_msg = f"Task {task} is {priority} priority"
    case _:
        priority_msg = f"Task {task} is unrecognized"

if time_bound == "yes":
    is_time_bound = " that requires immediate attention today"
elif time_bound == "no":
    is_time_bound = ", which can be scheduled later this week"
else:
    is_time_bound = ", but the time-sensitivity is unclear"


print(f"{priority_msg} {is_time_bound}")
