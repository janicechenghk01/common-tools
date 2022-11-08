import time
import datetime

def convert_str_to_unix(s='2022-11-08 23:59:24'):
    # convert string to unix time, e.g. 2022-11-08 to 1667921099
    fmt = "%Y-%m-%d %H:%S:%M"
    dt = datetime.datetime.strptime(s, fmt)
    return int(time.mktime(dt.timetuple()))
