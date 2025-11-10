# task = input("Enter your task: ")
# Priority = input("Priority (high, medium, low): ")
# time_bound = input("Is it time-bound? (yes/no): ")

# match Priority:
#     case "high":
#         if time_bound == "yes":
#             print(f"{task}' is a high priority task that requires immediate attention today!")
#         else:
#             print("you still have time")
#     case "meduim":
#         if time_bound == "yes":
#             print("Get involved")
#         else:
#             print("nothing to worry about")
#     case "low":
#         if time_bound == "yes":
#             print("You still have to do it anyways")
#         else:
#             print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
#     case _:
#         print("")
        
## daily_reminder.py 🔔

# --- 1. Prompt for Task Details ---

# Get the task description
task = input("Please enter the task description: ")

# Get the task priority (convert to lowercase for robust matching)
priority = input("What is the task's priority (high, medium, low)?: ").lower()

# Ask if the task is time-bound (convert to lowercase for robust checking)
time_bound = input("Is the task time-bound (yes or no)?: ").lower()

# Initialize the base reminder message
base_message = ""
urgent_tag = ""

# --- 2. Process Task Based on Priority (Match Case) ---

match priority:
    case "high":
        base_message = f"🚨 Reminder: Your HIGH priority task '{task}' must be focused on."
    case "medium":
        base_message = f"💡 Note: Your MEDIUM priority task '{task}' should be addressed soon."
    case "low":
        base_message = f"🧘 Relax: Your LOW priority task '{task}' can be done when convenient."
    case _:
        # Default case for invalid priority input
        base_message = f"⚠️ Alert: The task '{task}' has an unrecognized priority, but needs attention."

# --- 3. Modify Reminder for Time Sensitivity (If Statement) ---

# Check if the task is time-bound
if time_bound == "yes":
    # Append the urgent tag to the existing message
    urgent_tag = " that requires immediate attention today!"
else:
    # Set a default tag if not time-bound
    urgent_tag = " that can be done at a flexible pace."

# --- 4. Output the Customized Reminder ---

# Combine the base message and the time-sensitivity tag
final_reminder = base_message + urgent_tag

print("\n" + "="*40)
print("CUSTOMIZED DAILY REMINDER")
print("="*40)
print(final_reminder)
print("="*40)