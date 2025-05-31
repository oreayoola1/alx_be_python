task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ")
priority = priority.lower()

time_bound = input("Is it time-bound? (yes/no): ")
time_bound = time_bound.lower()

if priority == "high":
    msg = "'" + task + "' is a high priority task"
elif priority == "medium":
    msg = "'" + task + "' is a medium priority task"
elif priority == "low":
    msg = "'" + task + "' is a low priority task"
else:
    msg = "'" + task + "' has an unknown priority"

if time_bound == "yes":
    msg = msg + " that requires immediate attention today!"
else:
    msg = msg + ". Consider doing it when you have time."

print()
print("Reminder:", msg)
