import schedule as sched

class Tasks:
    def __init__(self, name, date):
        self.name = name
        self.date = date

task_list = []

while True:
    #current, next, and seven day notification
    sched.next_day_notification(task_list)
    sched.seven_day_notification(task_list)

    print("\n=======================")
    print("1. Add tasks\n2. Remove tasks\n3. Display Tasks\n4. Exit")
    choice = int(input("Choose a function: "))
    
    #adding tasks
    if choice == 1:
        user_task = input("Enter a task: ")

        print("====DATE====")
        user_date_year = int(input("Enter year: "))
        user_date_month = int(input("Enter month: "))
        user_date_day = int(input("Enter day: "))

        task_date = sched.date_add(user_date_year, user_date_month, user_date_day)
        task = Tasks(user_task, task_date)

        task_list.append(task)

    #removing tasks
    elif choice == 2:
        print("Current Tasks:")

        for i in range(len(task_list)):
            print(f"{i+1}. {task_list[i].name} - {task_list[i].date}")

        user_input = int(input("What task would you like to remove: "))
        task_list.pop(user_input - 1)

    #displaying tasks    
    elif choice == 3:
        print("Current Tasks: ")

        for i in range(len(task_list)):
            print(f"{i+1}. {task_list[i].name} - {task_list[i].date}")
    
    #exit
    elif choice == 4:
        print("Exiting....")
        break

    else:
        print("An error occured")