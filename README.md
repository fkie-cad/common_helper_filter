# common_helper_filter
[![Build Status](https://travis-ci.org/fkie-cad/common_helper_filter.svg?branch=master)](https://travis-ci.org/fkie-cad/common_helper_filter)

Generate nice structured output of data.

## time

Converts seconds in nicly formated strings.

Examples:
```python
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

```
