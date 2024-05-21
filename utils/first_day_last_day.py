from datetime import datetime, timedelta


def first_day_last_day(date_string):
    date = datetime.strptime(date_string, "%Y-%m-%d")
    # Get the first day of the month
    first_day = date.replace(day=1)
    # Get the last day of the month
    next_month = date.replace(day=28) + timedelta(days=4)  # Add 4 days to ensure moving to the next month
    last_day = next_month - timedelta(days=next_month.day)
    # Print the first and last dates
    return {first_day:first_day.strftime("%Y-%m-%d"), last_day:last_day.strftime("%Y-%m-%d")}