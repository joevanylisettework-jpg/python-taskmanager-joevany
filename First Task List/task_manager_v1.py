# task_manager_v1.py
# Version 1: Store tasks in a list, add one, display them all.
tasks = [ "Learn Python", "Build a Task Manager"]
dates = ["2026-10-19", "2026-10-19"]

print("=== Task Manager ===")
print("Your task list is as followed. Let's add some tasks.\n")
print(tasks)
print("Dates created:")
print(dates)

third_task = input("Enter your third task: ")
tasks.append(third_task)
third_date = input("Enter the date for the third task: ")
dates.append(third_date)

fourth_task = input("\nEnter your fourth task: ")
tasks.append(fourth_task)
fourth_date = input("Enter the date for the fourth task: ")
dates.append(fourth_date)

fifth_task = input("\nEnter your fifth task: ")
tasks.append(fifth_task)
fifth_date = input("Enter the date for the fifth task: ")
dates.append(fifth_date)

print("\nYour tasks:")
print(tasks)
print("Dates:")
print(dates)
print("\n")
