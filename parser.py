import lxml.html
from download_utils import download_content
from time_utils import trans_submission_date
import time

base_url = 'https://leetcode.com/'


def parse_one_submissions(user_name):
    content = download_content(base_url + user_name)
    tree = lxml.html.fromstring(content)
    submissions_col = tree.xpath(
        '//div[@class="shadow-level3 dark:shadow-dark-level3 bg-layer-1 dark:bg-dark-layer-1 rounded-lg px-4 pt-4 pb-4"]//div[@class="flex flex-col"]')[
        0]
    submissions = submissions_col.xpath('./a')
    print(submissions)
    return_list = []
    for sub in submissions:
        under_div = sub.xpath('./div')[0]
        question_title = under_div.xpath('./span[1]/text()')[0]
        question_finished_time = trans_submission_date(under_div.xpath('./span[2]/text()')[0])
        return_list.append((question_title, question_finished_time))
    return return_list


def parse_multi_users_submissions(user_list):
    res = {}
    for user in user_list:
        time.sleep(1)
        return_list = parse_one_submissions(user)
        res[user] = return_list
    return res
