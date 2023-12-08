import pickle
from datetime import datetime

# class
class PlayedTime:
# Constructor
    def __init__(self):
        self._date = datetime.now()

    def print_date(self):
        print(f"time is {self._date}")
