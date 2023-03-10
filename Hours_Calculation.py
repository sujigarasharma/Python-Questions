hours_worked = []
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
for day in days:
    hours = float(input(f"Enter the number of hours worked on {day}: "))
    hours_worked.append(hours)

avg_hours_worked = sum(hours_worked) / len(hours_worked)

hours = int(avg_hours_worked)
minutes = int((avg_hours_worked - hours) * 60)
print(f"The average number of hours worked by the employee is {hours} hours and {minutes} minutes.")
