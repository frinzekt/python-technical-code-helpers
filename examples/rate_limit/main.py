import datetime

# Key-Value store database (assume this is an ORM to a caching database like Redis, memcache, etc.)
"""
Database structure
   "key": {
        "number_of_requests": <value>,
        "first_request_time": <value>,
    }
"""
database = {}

LIMIT = 5  # request per minute
DURATION_OF_TIME = 60


def get_time_now() -> datetime.datetime:
    """
    This function is used to get the current time.

    TODO: Use the datetime library for the particular API
    """
    return datetime.datetime.now()


class RateLimitException(Exception):
    """
    This exception is raised when the rate limit is exceeded.
    """

    pass


def rate_limit_fix_window(
    key: str, limit=LIMIT, duration_of_time=DURATION_OF_TIME
) -> None:
    """
    This function is used to rate limit the number of requests to the API by `limit` requests per `duration_of_time`.


    :param key: The key to rate limit. Note: You can use this to rate limit a particular API, or a user of the API or combination of both (whatever that fits).
    :raise: Exception if more than a certain limit
    """
    now = get_time_now()

    if key not in database:
        database[key] = {
            "number_of_requests": 0,
            "first_request_time": now,
        }

    # Make sure we are only comparing within a fixed window
    time_between_first_request_and_now: datetime.timedelta = (
        now - database[key]["first_request_time"]
    )
    if time_between_first_request_and_now.total_seconds() > duration_of_time:
        database[key]["number_of_requests"] = 0
        database[key]["first_request_time"] = now

    if database[key]["number_of_requests"] >= limit:
        raise RateLimitException("Rate limit exceeded")

    # Update the database
    database[key]["number_of_requests"] += 1


def rate_limit_fix_window_wrapper(
    key: str, limit=LIMIT, duration_of_time=DURATION_OF_TIME
):
    """
    This is a wrapper for `rate_limit_fix_window`
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            rate_limit_fix_window(key, limit, duration_of_time)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@rate_limit_fix_window_wrapper("test")
def sample_function():
    print("hello_world")
