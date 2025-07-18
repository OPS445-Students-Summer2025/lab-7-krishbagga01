#!/usr/bin/env python3
# Student ID: 148191232

class Time:
    """Time object representing hours, minutes, and seconds."""

    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Return a nicely formatted time string for print()."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Return a time string with '.' for interactive mode."""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def format_time(self):
        """Return time as a string."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def time_to_sec(self):
        minutes = self.hour * 60 + self.minute
        return minutes * 60 + self.second

    def valid_time(self):
        return 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60

    def change_time(self, seconds):
        total = self.time_to_sec() + seconds
        nt = sec_to_time(total)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second
        return None

    def sum_times(self, t2):
        total = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total)

def sec_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
