import yaml
from datetime import timedelta

from user_utils import read_user
from time_utils import get_CST_current


def check_absence(filepath, check_range, absence_num, absence_type):
    sign_in = {}
    nicks, _ = read_user(filepath)
    today = get_CST_current()
    with open(filepath, 'r') as f:
        obj = yaml.load(f.read(), Loader=yaml.FullLoader)
    for i, id in enumerate(nicks):
        if obj[id] is None or len(obj[id]) == 0:
            sign_in[id] = 'LeetCode id is wrong or submission is empty'
        absence_cur = 0
        for diff in range(1, check_range + 1):
            try:
                check_date = today - timedelta(days=diff)
                if obj[id][check_date.year][check_date.month][check_date.day]['count'] < 1:
                    absence_cur += 1
                else:
                    if absence_type == 'continue':
                        absence_cur = 0
            except:
                absence_cur += 1
            finally:
                if absence_cur == absence_num:
                    sign_in[id] = 'absence'
                    break
    return sign_in
