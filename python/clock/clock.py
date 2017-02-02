class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.rollover()

    def __repr__(self):
        return "%02d:%02d" % (self.hour, self.minute)

    def __eq__(self, compare_to):
        return repr(self) == repr(compare_to)

    def add(self, minutes):
        self.minute += minutes
        return self.rollover()

    def rollover(self):
        self.hour += self.minute // 60
        self.hour %= 24
        self.minute %= 60
        return self
