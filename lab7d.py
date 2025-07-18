#!/usr/bin/env python3
# Student ID: 148191232

class Time:
    """Simple object type for time of the day.
       Attributes: hour, minute, second
       Methods: format_time, sum_times, change_time, time_to_sec, valid_time
    """

    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def format_time(self):
        """Return formatted time as string."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def time_to_sec(self):
        """Convert self to seconds since midnight."""
        minutes = self.hour * 60 + self.minute
        return minutes * 60 + self.second

    def valid_time(self):
        """Validate time attributes."""
        return 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60

    def change_time(self, seconds):
        """Add or subtract seconds to/from self."""
        total = self.time_to_sec() + seconds
        updated = sec_to_time(total)
        self.hour, self.minute, self.second = updated.hour, updated.minute, updated.second
        return None

    def sum_times(self, t2):
        """Add self with another Time object."""
        total = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total)

def sec_to_time(seconds):
    """Convert seconds to Time object."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
