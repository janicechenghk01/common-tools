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


def get_time_diff(start, end):
    c_start = datetime.fromtimestamp(round(start / 1000))
    c_end = datetime.fromtimestamp(round(end / 1000))
    seconds = (c_end - c_start).total_seconds()
    return seconds 


def date_generator(numdays=2):
    base = datetime.today()
    date_list = [(base - timedelta(days=x)).strftime('%Y-%m-%d') for x in range(numdays)]
    return date_list