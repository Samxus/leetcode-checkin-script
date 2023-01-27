import argparse

from user_utils import read_user, user_init, record_submission
from time_utils import create_record
from parser import parse_multi_users_submissions
from review_utils import check_absence

if __name__ == '__main__':
    arguments = argparse.ArgumentParser()
    arguments.add_argument('--user_list', default='./data/user.yaml')
    arguments.add_argument('--record_output', default='test_record.yaml')
    arguments.add_argument('--update_submission', default=False)
    arguments.add_argument('--check_range', default=3)
    arguments.add_argument('--absence_num', default=3)
    arguments.add_argument('--absence_type', default='continue')
    argv = arguments.parse_args()

    record_path = create_record(argv.record_output)
    if argv.update_submission:
        nicks, real_names = read_user(argv.user_list)
        user_init(nicks, record_path)
        all_records = parse_multi_users_submissions(nicks)
        record_submission(all_records, record_path)
    print(check_absence(record_path, argv.check_range, argv.absence_num, argv.absence_type))
