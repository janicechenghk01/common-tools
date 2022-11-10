import time
from datetime import datetime
from datetime import timedelta


def convert_str_to_unix(s='2022-11-08 23:59:24'):
    # convert string to unix time, e.g. 2022-11-08 to 1667921099
    fmt = "%Y-%m-%d %H:%S:%M"
    dt = datetime.strptime(s, fmt)
    return int(time.mktime(dt.timetuple()))


# https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date
def convert_unix_to_str(ts=1666634754):
    # convert unix time to string, e.g. 1666634754 to 2022-10-24 18:05:54
    fmt = '%Y-%m-%d %H:%M:%S'
    dt = datetime.utcfromtimestamp(ts)
    return dt.strftime(fmt)


def get_previous_n_day(n=2):
    fmt = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    future_day = now - timedelta(days=n)
    return future_day.strftime(fmt)