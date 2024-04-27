import sys

def calculate_time_difference(start_time, end_time):
    """Calculates the difference between two time durations in HH:MM format.

    Args:
        start_time (str): Time duration in HH:MM format (e.g., "1:18").
        end_time (str): Time duration in HH:MM format (e.g., "2:18").

    Returns:
        str: The difference between the two time durations in HH:MM format,
             or an error message if the input is invalid.
    """

    try:
        hours_start, minutes_start = start_time.split(':')
        hours_end, minutes_end = end_time.split(':')

        if not hours_start.isdigit() or not minutes_start.isdigit() \
           or not hours_end.isdigit() or not minutes_end.isdigit():
            return "Invalid input format. Please provide time durations in HH:MM format (e.g., 1:18)."

        start_minutes = int(hours_start) * 60 + int(minutes_start)
        end_minutes = int(hours_end) * 60 + int(minutes_end)

        # Handle negative differences by swapping start and end times if necessary
        if end_minutes < start_minutes:
            start_minutes, end_minutes = end_minutes, start_minutes

        # Calculate the difference in minutes
        difference_minutes = end_minutes - start_minutes

        # Convert difference to HH:MM format
        hours, minutes = divmod(difference_minutes, 60)
        return f"{hours:02d}:{minutes:02d}"

    except ValueError:
        return "Invalid input. Please provide time durations in HH:MM format (e.g., 1:18)."

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: time_duration_diff.py <start_time> <end_time>")
        sys.exit(1)

    start_time, end_time = sys.argv[1], sys.argv[2]
    difference = calculate_time_difference(start_time, end_time)
    print(difference)

