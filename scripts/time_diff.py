"""
This script calculates the difference between time stamps(exclusive of date)

Basic usage includes:
    python -m time_diff <hours>:<minutes> <AM/PM> <hours>:<minutes> <AM/PM>
"""

import sys
from datetime import datetime

def time_difference(start_time, end_time):
    try:
        start = datetime.strptime(start_time, "%I:%M %p")
        end = datetime.strptime(end_time, "%I:%M %p")
        diff = end - start
        hours, remainder = divmod(diff.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        return hours, minutes
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("\033[01;92mUsage: python -m time_diff.py <start_time> <end_time>\033[0m")
        sys.exit(1)

    start_time = sys.argv[1] + " " + sys.argv[2]
    end_time = sys.argv[3] + " " + sys.argv[4]

    hours, minutes = time_difference(start_time, end_time)

    print(f"\033[01;93m{hours}\033[0m \033[01;92mhr(s)\033[0m \033[01;93m{minutes}\033[0m \033[01;92mmin(s)\033[0m")

