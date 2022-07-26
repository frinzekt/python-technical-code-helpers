import datetime
from main import (
    rate_limit_fix_window,
    LIMIT,
    RateLimitException,
    database,
    rate_limit_fix_window_wrapper,
)

import pytest


@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    """Fixture to execute asserts before and after a test is run"""
    # Setup: fill with any logic you want
    for key in list(database.keys()):
        database.pop(key)

    yield  # this is where the testing happens

    # Teardown : fill with any logic you want


def test_rate_limit_default_parameters_exceeding(mocker):
    """
    GIVEN: the default configurations (LIMIT = 5, DURATION_OF_TIME = 60)
    WHEN:  6 requests are hit for every second
    THEN:  the rate limit exception is raised
    """
    # Mock the values coming out of the datetime
    mocker = mocker.patch(
        "main.get_time_now",
        # A minute interval
        side_effect=[
            datetime.datetime(2020, 1, 1, 0, 0, second) for second in range(LIMIT + 1)
        ],
    )

    KEY = "test"

    # Test that the default parameters are used when no parameters are passed in.

    # Setup with no exception
    for _ in range(LIMIT):
        rate_limit_fix_window(KEY)

    # Except an exception for the last one
    with pytest.raises(RateLimitException):
        rate_limit_fix_window(KEY)


def test_rate_limit_default_parameter_not_exceeding(mocker):
    """
    GIVEN: the default configurations (LIMIT = 5, DURATION_OF_TIME = 60)
    WHEN:  5 requests are hit for every minute
    THEN:  no exception is raised
    """
    # Mock the values coming out of the datetime
    mocker = mocker.patch(
        "main.get_time_now",
        # A minute interval
        side_effect=[
            datetime.datetime(2020, 1, 1, 0, minute, 0) for minute in range(LIMIT + 1)
        ],
    )

    KEY = "test"

    # No exception are raised
    for _ in range(LIMIT + 1):
        rate_limit_fix_window(KEY)


def test_rate_limit_decorator_exceeding(mocker):
    """
    GIVEN: the default configurations (LIMIT = 5, DURATION_OF_TIME = 60)
    AND:   Is set on a particular function
    WHEN:  5 requests are hit for every minute
    THEN:  no exception is raised
    """
    # Mock the values coming out of the datetime
    mocker = mocker.patch(
        "main.get_time_now",
        # A minute interval
        side_effect=[
            datetime.datetime(2020, 1, 1, 0, 0, second) for second in range(LIMIT + 1)
        ],
    )

    KEY = "test"

    @rate_limit_fix_window_wrapper(KEY)
    def test_function():
        pass

    # No exception are raised
    for _ in range(LIMIT):
        test_function()

    # Except an exception for the last one
    with pytest.raises(RateLimitException):
        test_function()
