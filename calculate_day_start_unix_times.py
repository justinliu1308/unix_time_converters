import time
from datetime import datetime, timedelta


current_unix_time = int(time.time())                            # Get current Unix time
current_datetime = datetime.fromtimestamp(current_unix_time)    # Convert Unix time to datetime object
print(f"\nCurrent local unix time: {current_unix_time}")
print(f"Current local time:      {current_datetime}\n")

days = 5        # days = how many days in the future you want unix start times for
unix_start_times = []
human_start_times = []
for i in range(days):
    next_day_datetime = current_datetime + timedelta(days=i+1)  # Add days to datetime object
    next_day_datetime = next_day_datetime.replace(hour=0, minute=0, second=0, microsecond=0)    # Set time component to 00:00:00
    next_day_unix_time = int(next_day_datetime.timestamp())     # Convert datetime object back to Unix time for the next day
    unix_start_times.append(next_day_unix_time)
    dt = datetime.fromtimestamp(next_day_unix_time)             # Convert new day Unix time to datetime object
    date_string = dt.strftime("%Y-%m-%d %H:%M:%S")              # Convert datetime object to human-readable string
    human_start_times.append(date_string)
print(f"Below is a list of the local unix times for the start of each day for the next {days} days:")
print("   ", unix_start_times)
print(f"Below is a list of the same times in human readable format (ISO 8601):")
print("   ", human_start_times, "\n")



