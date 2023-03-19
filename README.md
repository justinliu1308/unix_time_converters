# unix_time_converters
Get and convert Unix time to human readable strings and get next day Unix start times

## Sample Output: convert_unix_time.py
Current local unix time: 1679197805
Current local time:      2023-03-18 23:50:05

## Sample Output: calculate_day_start_unix_times.py
Current local unix time: 1679197869 <br>
Current local time:      2023-03-18 23:51:09 <br>

Below is a list of the local unix times for the start of each day for the next 5 days: <br>
    [1679198400, 1679284800, 1679371200, 1679457600, 1679544000] <br>
Below is a list of the same times in human readable format (ISO 8601): <br>
    ['2023-03-19 00:00:00', '2023-03-20 00:00:00', '2023-03-21 00:00:00', '2023-03-22 00:00:00', '2023-03-23 00:00:00'] <br>