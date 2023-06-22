import calendar

print("Program to show the calendar of any month of any year")

year = int (input("Enter the year "))
month = int (input("Enter the month "))
year = int(year)
month = int(month)

print (calendar.month(year, month))

