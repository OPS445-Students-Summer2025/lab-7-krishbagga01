#!/usr/bin/env python3

class Time:
    """Simple object type for time of the day."""
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string."""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def valid_time(t):
    """Check if the time values are within valid ranges."""
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

def sum_times(t1, t2):
    """Add two time objects and return the result."""
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    while sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
    while sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum

def change_time(time, seconds):
    """Modify a time object by adding (or subtracting) seconds."""
    time.second += seconds

    if valid_time(time) is not True:
        # Handle overflow
        while time.second >= 60:
            time.second -= 60
            time.minute += 1
        while time.minute >= 60:
            time.minute -= 60
            time.hour += 1

        # Handle underflow (negative seconds)
        while time.second < 0:
            time.second += 60
            time.minute -= 1
        while time.minute < 0:
            time.minute += 60
            time.hour -= 1
