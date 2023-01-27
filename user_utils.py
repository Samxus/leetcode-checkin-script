import yaml
from datetime import datetime


def read_user(file='./data/user.yaml'):
    with open(file=file) as f:
        content = yaml.load(f, Loader=yaml.FullLoader)
    nick_names = list(content.keys())
    real_names = list(content.values())
    return nick_names, real_names


def record_submission(record, filepath):
    with open(filepath, 'r') as f:
        obj = yaml.load(f.read(), Loader=yaml.FullLoader)
    for name, submissions in record.items():
        for question, (time, calender) in submissions:
            question = str(question)
            if obj[name] is None or name not in obj:
                obj[name] = {}
            if time.year not in obj[name]:
                obj[name][time.year] = {}
            if time.month not in obj[name][time.year]:
                obj[name][time.year][time.month] = {}
            if time.day not in obj[name][time.year][time.month]:
                obj[name][time.year][time.month][time.day] = {'questions': {}}
            if question not in obj[name][time.year][time.month][time.day]['questions']:
                obj[name][time.year][time.month][time.day]['questions'][question] = time.strftime('%y-%m-%d')
            obj[name][time.year][time.month][time.day]['count'] = len(
                obj[name][time.year][time.month][time.day]['questions'])
    with open(filepath, 'w') as f:
        yaml.dump(obj, f)


def user_init(user_list, record_name):
    with open(record_name, 'r') as f:
        obj = yaml.load(f.read(), Loader=yaml.FullLoader)
    if obj is None:
        obj = {}
    for user in user_list:
        if user not in obj:
            obj[user] = {}
    with open(record_name, 'w') as f:
        yaml.dump(obj, f)
