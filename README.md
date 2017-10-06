# common_helper_filter

Generate nice structured output of data.

## time

Examples:
´´´python
from common_helper_filter import time_format

print(time_format(122))
>> 2m, 2s

print(time_format(122).format(description='short'))
>> 2m, 2s

print(time_format(122).format(description='long'))
>> 2 minutes, 2 seconds

print(time_format(122).format(description='none'))
>> 2:2

print(time_format(63072000))
>> 2y, 0d, 0h, 0m, 0s

´´´