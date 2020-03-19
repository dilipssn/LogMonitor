# Reference: https://github.com/swadhikar/log_parser/

# file size find
import os
import time
import json
import datetime
from util import pretty_print
from dataclasses import asdict


def get_file_size(filename):
    return os.stat(filename).st_size


previous_file_size = 0


def has_logged(filename):
    global previous_file_size
    current_file_size = get_file_size(filename)

    print(f'Current file size: {current_file_size}')
    print(f'Previos file size: {previous_file_size}')

    if current_file_size > previous_file_size:
        return True

    # update the previous file size
    previous_file_size = current_file_size

    return False


is_logged = has_logged('__init__.py')
print(is_logged)

is_logged = has_logged('__init__.py')
print(is_logged)

# json read
with open('../config/apps.json') as f:
    json_data = json.load(f)
    print(type(json_data))
    print(type(json_data[0]))
    print(type(json_data[1]))
    pretty_print(json_data)


# class
class LogLine:
    """
        Represent as object: 03/18/2020 18:16:35.866: Java is being overtaken by python
    """

    def __init__(self, line):
        self.timestamp = None
        self.message = None
        self.parse_line(line)

    def parse_line(self, line):
        """Split timestamp and message from line and store in object"""
        timestamp_str = line[:23]
        self.message = line[25:]

        # Convert time string to python datetime.datetime
        self.timestamp = datetime.datetime.strptime(timestamp_str, '%m/%d/%Y %H:%M:%S.%f')

        # 03/18/2020 18:16:35.866 <class 'str'>
        # print(timestamp_str, type(timestamp_str))
        # print(self.timestamp, type(self.timestamp))


curr_time = datetime.datetime.now()
time.sleep(3)
new_curr_time = datetime.datetime.now()
print('TIme diff:')
print(new_curr_time - curr_time)
print(new_curr_time > curr_time)

print(datetime.datetime.now(), type(datetime.datetime.now()))
# 2020-03-19 16:01:13.872628
# %Y-%M-%d %H:%m:%s.%f

# log line
last_stored_line = LogLine('03/18/2020 18:16:35.866: Java is being overtaken by python')


# new_line = LogLine('03/18/2020 18:18:35.866: Python is used in ML')
new_line = LogLine('03/18/2020 18:16:37.866: Python is used in ML')
# print(new_line.timestamp)

if new_line.timestamp > last_stored_line.timestamp:
    print('Detected new logs!')
else:
    print('Nothing is logged')


# dataclass
d = {
    'name': 'Swadhi',
    'age': 30
}

print(d.get('name'))
print(d.get('age'))

from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int


user_1 = User(**d)
print(user_1.name)
print(user_1.age)

app = {
    "app_name": "trial_app",
    "servers": [
        "10.197.0.1",
        "10.197.0.2"
    ]
}


@dataclass
class App:
    app_name: str
    servers: list

    def __post_init__(self):
        """Create a new variable server"""
        self.server = self.servers[-1]


trial = App(**app)
print(trial.servers)
print(trial.server)
print(asdict(trial))
