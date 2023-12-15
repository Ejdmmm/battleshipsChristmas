"""
Date and time in game by our class
"""
import datetime
class MyDate:
    """
    Our class MyDate
    """
    def __init__(self, date):
        self.date = date

    def get_current_date(self):
        """
        Getting current date
        """
        return self.date.strftime("%Y-%m-%d")

    def get_current_time(self):
        """
        Getting current time
        """
        return self.date.strftime("%H:%M:%S")

def get_current_datetime():
    """
    Returning current datetime
    """
    return MyDate(datetime.datetime.now())
