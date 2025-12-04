from datetime import datetime, date, timedelta

def display_current_datetime():
    current_date = datetime.now()
    format_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(format_date)
    return current_date

display_current_datetime()

def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    current_day = datetime.now().date()
    time_delta = timedelta(days=days_to_add)
    future_date = current_day + time_delta
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(formatted_future_date)
calculate_future_date()




