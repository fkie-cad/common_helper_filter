import pytest

from common_helper_filter import time_format


@pytest.mark.parametrize('input_seconds, description, expected_output', [
    (65, 'none', '1:5'),
    (65, 'short', '1m, 5s'),
    (65, 'long', '1 minutes, 5 seconds'),
    (8643665.1234, 'short', '100d, 1h, 1m, 5s'),
    (63072000, 'long', '2 years, 0 days, 0 hours, 0 minutes, 0 seconds'),
    (0, 'none', '0')
])
def test_time_format_different_descriptions(input_seconds, description, expected_output):
    assert time_format(input_seconds).format(description=description) == expected_output


def test_time_format_simple():
    assert '{}'.format(time_format(65)) == '1m, 5s'
