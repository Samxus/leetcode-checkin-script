import pytz
import os
from datetime import datetime, timedelta

CST = pytz.timezone('America/Chicago')
dir_path = 'data/submission_records'


def get_CST_current():
    return datetime.now(CST)


def records_dir_check():
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)


def trans_submission_date(submission_time):
    cur_time = get_CST_current()
    time_li = submission_time.strip().split(' ')
    time_diff = timedelta(days=0)
    # ignore mins and seconds
    # mins and seconds ago means just right now...
    if time_li[1] in 'days':
        if time_li[0] == 'a':
            time_diff = timedelta(days=1)
        else:
            time_diff = timedelta(days=int(time_li[0]))
    elif time_li[1] in 'hours':
        if time_li[0] in 'an':
            time_diff = timedelta(hours=1)
        else:
            time_diff = timedelta(hours=int(time_li[0]))
    submission_time = cur_time - time_diff
    return (submission_time, submission_time.isocalendar())


def create_record(path):
    records_dir_check()
    record_path = dir_path + '/' + path
    file_exist = os.path.exists(record_path)
    if not file_exist:
        file = open(record_path, 'w')
        file.close()
    return record_path
