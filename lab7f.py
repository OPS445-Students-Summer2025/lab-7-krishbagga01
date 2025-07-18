#!/usr/bin/env python3
# Student ID: 148191232

class Time:
    """Time object representing hours, minutes, and seconds."""

    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Used by print()."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Used in interactive shell."""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def format_time(self):
        """Return formatted time string."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def time_to_sec(self):
        """Convert time to total seconds."""
        return self.hour * 3600 + self.minute * 60 + self.second

    def valid_time(self):
        return 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60

    def change_time(self, seconds):
        total = self.time_to_sec() + seconds
        new_time = sec_to_time(total)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second
        return None

    def sum_times(self, t2):
        total = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total)

    def __add__(self, t2):
        """Enable t1 + t2 for Time objects."""
        return self.sum_times(t2)

def sec_to_time(seconds):
    """Convert total seconds to Time object."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
