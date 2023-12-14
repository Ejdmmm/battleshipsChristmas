import datetime
class MyDate:
    def __init__(self, date):
        self.date = date

    def get_current_date(self):
        return self.date.strftime("%Y-%m-%d")

    def get_current_time(self):
        return self.date.strftime("%H:%M:%S")

def get_current_datetime():
    return MyDate(datetime.datetime.now())