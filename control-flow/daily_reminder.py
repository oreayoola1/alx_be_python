task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ")
priority = priority.lower()

time_bound = input("Is it time-bound? (yes/no): ")
time_bound = time_bound.lower()

match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"
        
if time_bound == "yes":
    msg = msg + " that requires immediate attention today!"
else:
    msg = msg + ". Consider doing it when you have time."
print("Reminder:", msg)
