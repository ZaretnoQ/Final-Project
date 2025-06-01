import datetime as dt

def date_add(year, month, day):
    return dt.date(year, month, day)

def next_day_notification(task_list):
    today = dt.date.today()

    for i in task_list:
        diff = i.date - today

        if diff.days == 0:
            print("=======================")
            print("There's an upcoming task due today!")
            break
        elif diff.days == 1:
            print("=======================")
            print("There's an upcoming task due tomorrow!")
            break
        
def seven_day_notification(task_list):
    today = dt.date.today()

    for i in task_list:
        diff = i.date - today

        if diff.days >= 0 and diff.days <= 7:
            print("=======================")
            print("There's an upcoming tasks within the week!")
            break