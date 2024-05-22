from datetime import datetime, timedelta


def first_day_last_day(date_string):
    try:
    # Handle different date string formats
        if len(date_string) == 7:  # Format "YYYY-MM"
            date_string += "-01"  # Assume the first day of the given month
        
        # Parse the date
        date = datetime.strptime(date_string, "%Y-%m-%d")
        
        # Get the first day of the month
        first_day = date.replace(day=1)
        
        # Get the last day of the month
        next_month = date.replace(day=28) + timedelta(days=4)  # Add 4 days to ensure moving to the next month
        last_day = next_month - timedelta(days=next_month.day)
        
        return {"first_day": first_day.strftime("%Y-%m-%d"), "last_day": last_day.strftime("%Y-%m-%d")}
    except Exception as e:
        return ValueError("Error in first_day_last_day",e)



def first_year_day_last_year_day(date_string):
    try:
        # Handle different date string formats
        if len(date_string) == 4:  # Format "YYYY"
            date_string += "-01-01"  # Assume January of the given year
        elif len(date_string) == 6 or len(date_string) == 7:  # Format "YYYY-M" or "YYYY-MM"
            parts = date_string.split('-')
            if len(parts[1]) == 1:  # If month is single digit
                parts[1] = '0' + parts[1]  # Zero-pad the month
            date_string = parts[0] + '-' + parts[1] + "-01"

        # Parse the date
        date = datetime.strptime(date_string, "%Y-%m-%d")
        
        # Get the first day of the month
        first_day = date.replace(day=1)
        
        # Get the last day of the month
        next_month = date.replace(day=28) + timedelta(days=4)  # Add 4 days to ensure moving to the next month
        last_day = next_month - timedelta(days=next_month.day)
        
        return {"first_day": first_day.strftime("%Y-%m-%d"), "last_day": last_day.strftime("%Y-%m-%d")}
    except Exception as e:
        return ValueError("Error in first_year_day_last_year_day",e)