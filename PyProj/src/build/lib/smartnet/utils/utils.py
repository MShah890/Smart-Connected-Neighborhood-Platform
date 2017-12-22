import datetime
import time


def to_py_date(java_timestamp):
    try:
        seconds = java_timestamp / 1000
        sub_seconds  = (java_timestamp % 1000.0) / 1000.0
        date = datetime.datetime.fromtimestamp(seconds + sub_seconds)
    except:
        #some error here. return None
        return None

    return date

def to_java_date(py_timestamp):
    try:
        java_date =  int(time.mktime(py_timestamp.timetuple())) * 1000 + py_timestamp.microsecond / 1000
        return java_date
    except:
        #some error here, return None
        return None
