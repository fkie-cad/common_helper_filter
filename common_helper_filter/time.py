from collections import namedtuple

TimeStruct = namedtuple('time', ['y', 'd', 'h', 'm', 's'])


class time_format():

    description = {
        'long': [' years, ', ' days, ', ' hours, ', ' minutes, ', ' seconds'],
        'short': ['y, ', 'd, ', 'h, ', 'm, ', 's'],
        'none': [':', ':', ':', ':', '']
    }

    def __init__(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        years, days = divmod(days, 365)
        self.time = TimeStruct(y=years, d=days, h=hours, m=minutes, s=seconds)

    def __str__(self):
        return self.format()

    def __repr__(self):
        return self.__str__()

    def format(self, description='short'):
        pointer = 0
        output = ''
        while pointer < len(self.time) - 1:
            if self.time[pointer] > 0:
                break
            pointer += 1
        while pointer < len(self.time) - 1:
            output += '{:.0f}{}'.format(self.time[pointer], self.description[description][pointer])
            pointer += 1
        output += '{:.0f}{}'.format(self.time[pointer], self.description[description][pointer])
        return output
