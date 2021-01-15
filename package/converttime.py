class Time:
    def __init__(self, hour, minute, second, day, week, month, year):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.day = day
        self.week = week
        self.month = month
        self.year = year
        
class Set(Time):
    def convert(self):
        if self.minute > 0:
            self.second = self.minute * 60
            self.year = self.second // 31557600
            self.second %= 31557600
            self.month = self.second // 2629800
            self.second %= 2629800
            self.week = self.second // 604800
            self.second %= 604800
            self.day = self.second // 86400
            self.second %= 86400
            self.hour = self.second // 3600
            self.second %= 3600
            self.minute = self.second // 60
            self.second %= 60
            data = "%d:%d:%d:%d:%d:%d:%d" % (self.year, self.month, self.week, self.day, self.hour, self.minute, self.second)
            return data
        elif self.hour > 0:
        	self.second = self.hour * 3600
        	self.year = self.second // 31557600
        	self.second %= 31557600
        	self.month = self.second // 2629800
        	self.second %= 2629800
        	self.week = self.second // 604800
        	self.second %= 604800
        	self.day = self.second // 86400
        	self.second %= 86400
        	self.hour = self.second // 3600
        	self.second %= 3600
        	self.minute = self.second // 60
        	self.second %= 60
        	data = "%d:%d:%d:%d:%d:%d:%d" % (self.year, self.month, self.week, self.day, self.hour, self.minute, self.second)
        	return data
        elif self.day > 0:
        	self.second = self.day * 86400
        	self.year = self.second // 31557600
        	self.second %= 31557600
        	self.month = self.second // 2629800
        	self.second %= 2629800
        	self.week = self.second // 604800
        	self.second %= 604800
        	self.day = self.second // 86400
        	self.second %= 86400
        	self.hour = self.second // 3600
        	self.second %= 3600
        	self.minute = self.second // 60
        	self.second %= 60
        	data = "%d:%d:%d:%d:%d:%d:%d" % (self.year, self.month, self.week, self.day, self.hour, self.minute, self.second)
        	return data
        elif self.week > 0:
        	self.second = self.week * 604800
        	self.year = self.second // 31557600
        	self.second %= 31557600
        	self.month = self.second // 2629800
        	self.second %= 2629800
        	self.week = self.second // 604800
        	self.second %= 604800
        	self.day = self.second // 86400
        	self.second %= 86400
        	self.hour = self.second // 3600
        	self.second %= 3600
        	self.minute = self.second // 60
        	self.second %= 60
        	data = "%d:%d:%d:%d:%d:%d:%d" % (self.year, self.month, self.week, self.day, self.hour, self.minute, self.second)
        	return data
        elif self.month > 0:
        	self.second = self.month * 2629800
        	self.year = self.second // 31557600
        	self.second %= 31557600
        	self.month = self.second // 2629800
        	self.second %= 2629800
        	self.week = self.second // 604800
        	self.second %= 604800
        	self.day = self.second // 86400
        	self.second %= 86400
        	self.hour = self.second // 3600
        	self.second %= 3600
        	self.minute = self.second // 60
        	self.second %= 60
        	data = "%d:%d:%d:%d:%d:%d:%d" % (self.year, self.month, self.week, self.day, self.hour, self.minute, self.second)
        	return data
        elif self.year > 0:
        	self.second = self.year * 31557600
        	self.year = self.second // 31557600
        	self.second %= 31557600
        	self.month = self.second // 2629800
        	self.second %= 2629800
        	self.week = self.second // 604800
        	self.second %= 604800
        	self.day = self.second // 86400
        	self.second %= 86400
        	self.hour = self.second // 3600
        	self.second %= 3600
        	self.minute = self.second // 60
        	self.second %= 60
        	data = "%d:%d:%d:%d:%d:%d:%d" % (self.year, self.month, self.week, self.day, self.hour, self.minute, self.second)
        	return data
        elif self.second > 0:
            self.year = self.second // 31557600
            self.second %= 31557600
            self.month = self.second // 2629800
            self.second %= 2629800
            self.week = self.second // 604800
            self.second %= 604800
            self.day = self.second // 86400
            self.second %= 86400
            self.hour = self.second // 3600
            self.second %= 3600
            self.minute = self.second // 60
            self.second %= 60
            data = "%d:%d:%d:%d:%d:%d:%d" % (self.year, self.month, self.week, self.day, self.hour, self.minute, self.second)
            return data