import time
from datetime import datetime


# Converts local unix time to human readable format (ISO 8601): YYYY-MM-DD HH:MM:SS
current_unix_time = int(time.time())                            # Get current Unix time
current_datetime = datetime.fromtimestamp(current_unix_time)    # Convert Unix time to datetime object
date_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S")    # Convert datetime object to human-readable string

# Print output
print(f"\nCurrent local unix time: {current_unix_time}")
print(f"Current local time:      {current_datetime}\n")
