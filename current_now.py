#!usr/bin/env python

""" MAIN MODULE
This is very useful module. According to the duck typing The time is only time.
Use this module when you should get real current time everywhere, always.
"""

from datetime import datetime

CONSTANT = {'hour': 23}


class CurrentTimeNowAndOnlyNow(object):
    """" This class create the instance of the time """
    _time = dict()  # the dictionary is used to populate the components of the time
    _components = ['year', 'month', 'day', 'hour', 'minute', 'second']

    def __init__(self):
        current_time = datetime.now().strftime("%Y.%m.%d %H:%M:%S")
        self._time[self._components[0]] = current_time[0:4:1]
        self._time[self._components[1]] = current_time[5:7:1]
        self._time[self._components[2]] = current_time[8:10:1]
        self._time[self._components[-3]] = current_time[11:13:1]
        self._time[self._components[-2]] = current_time[14:16:1]
        self._time[self._components[-1]] = current_time[17::1]

    def get_time(self):
        return self._time

    def get_time_plus_some_hours(self):
        self._time = CurrentTimeNowPlus23Hours().get_time()

    def __str__(self):
        temp = range(12)
        for _id, _value in enumerate(self._time):
            if _value == 'year':
                temp[0] = _value
                temp[1] = self._time[_id + 1]
            if _value == 'month':
                temp[2] = _value
                temp[3] = self._time[_id + 1]
            if _value == 'day':
                temp[4] = _value
                temp[5] = self._time[_id + 1]
            if _value == 'hour':
                temp[6] = _value
                temp[7] = self._time[_id + 1]
            if _value == 'minute':
                temp[8] = _value
                temp[9] = self._time[_id + 1]
            if _value == 'second':
                temp[10] = _value
                temp[11] = self._time[_id + 1]
        return "{} - {} - {} - {} - {} - {}".format(temp[0:2], temp[2:4], temp[4:6],
                                                    temp[6:8], temp[8:10], temp[10:])


class CurrentTimeNowPlus23Hours(object):
    time = {}
    time_update = []

    def __init__(self):
        current_time = CurrentTimeNowAndOnlyNow().get_time()
        temp_dict = {}
        set([temp_dict.update({y1: y2}) for y1, y2 in current_time.items()])
        map(lambda (x1, x2): self.time.update({x1: int(x2)}), temp_dict.items())

    def change_time(self):
        self.make_time()

    def make_time(self):
        current_time = self.time
        current_time['hour'] = current_time['hour'] + CONSTANT['hour']
        while ('infinity_loop'):
            try:
                if current_time['hour'] > 24:
                    current_time['hour'] = int(current_time['hour'] - current_time['hour'] + current_time['hour'] - 24)
                else:
                    raise StopIteration
            except StopIteration:
                break

            current_time['day'] += 1

            try:
                if current_time['day'] > 30 and current_time['day'] > 31 and \
                                current_time['month'] in [1, 3, 5, 7, 8, 10, 12] or \
                                                current_time['day'] < 31 and current_time['day'] > 29 and \
                                        current_time['month'] in [2, 4, 6, 9, 11]:
                    current_time['month'] = current_time['month'] + 1
                else:
                    raise StopIteration
            except StopIteration:
                break
            try:
                if current_time['month'] > 12:
                    current_time['year'] += 1
                else:
                    raise StopIteration
            except StopIteration:
                break

        [[self.push(x) for x in items] for items in current_time.items()]

    def push(self, arg):
        self.time_update.append(arg)

    def get_time(self):
        self.change_time()
        return self.time_update




if __name__ == '__main__':
    time = CurrentTimeNowAndOnlyNow()
    time.get_time_plus_some_hours()
    print time
