"""
Project Title: Attack On Deadline
Group Members: Sofia Palad, Naiah Intong, Isha Shekar
Description: A task reminder system for PSHS students.
"""

def main(): 
  # Setup lists to store data
  task_names = []
  task_deadlines = []

  print("--- Welcome to Attack On Deadline ---")

  while True:
    # Input Implementation
    name = input("Enter task name: ")
    date = input("Enter deadline (YYYY-MM-DD): ")

    task_names.append(name)
    task_deadlines.append(date)

    # Loop control
    choice = input("Add another task? (y/n): ")
    if choice.lower() != 'y':
      break

 print("\nTasks loaded. System ready.")

if __name__ == "__main__":
  main()
