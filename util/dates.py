from datetime import datetime

def get_days_difference(date_str1, date_str2):
    # Step 1: Parse the date strings into datetime objects
    date1 = datetime.strptime(date_str1, '%Y-%m-%d')
    date2 = datetime.strptime(date_str2, '%Y-%m-%d')

    # Step 2: Calculate the time difference between the two dates
    time_difference = abs((date2 - date1))

    # Step 3: Return the number of days as an integer
    return time_difference.days