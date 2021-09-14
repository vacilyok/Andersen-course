import requests
import sys


def display_count_user_labels(label_dict):
    print('\n\n***************************************************************')
    print('\tUsers with labels:')
    print('***************************************************************')
    for user in label_dict:
        if (label_dict[user] > 0):
            print(f"\t{user} - {label_dict[user]} labels")


def display_active_user(sorted_user):
    if len(sorted_user) == 0:
        return
    print('\n\n***************************************************************')
    print('\tActive users:')
    print('***************************************************************')
    for user in sorted_user:
        if user[1] > 1:
            print(f"\t{user[0]} - ", user[1], ' pull requests')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = 'https://github.com/vacilyok/Andersen-course'
        print(f"\n\nLink to repository: {url}")
    gitHubdata = url.split('/')
    git_repo = gitHubdata[-1]
    git_user = gitHubdata[-2]
    page = 1
    open_request = 0
    users = []
    label_dict = {}
    while True:
        r = requests.get(
            f'https://api.github.com/repos/{git_user}/{git_repo}/pulls?per_page=100&page={page}&state=open')
        result = r.json()
        count_request = len(result)
        open_request = open_request + count_request
        if count_request == 0:
            break
        for elem in result:
            user = elem['user']['login']
            users.append(user)
            labels_count = len(elem['labels'])
            if user in label_dict:
                label_dict[user] = label_dict[user] + labels_count
            else:
                label_dict[user] = labels_count
        page = page + 1

    users_dict = dict((i, users.count(i)) for i in users)
    sorted_user = [(k, users_dict[k]) for k in sorted(
        users_dict, key=users_dict.get, reverse=True)]
    display_active_user(sorted_user)
    display_count_user_labels(label_dict)
    print(f'\n\nIn repo {url} open request: {open_request}\n\n')
