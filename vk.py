#!/data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-

from core.core import *


def get_wall_posts(group_name):
    url = f"https://api.vk.com/method/wall.get?domain={group_name}&count=40&access_token={token}&v=5.131"
    r = requests.get(url)
    data = r.json()

    if os.path.exists(f'groups/{group_name}'):
        print(f"Директория с именем {group_name} уже существует!")
    else:
        os.makedirs('groups/' + group_name)

    with open(f'groups/{group_name}/{group_name}.json', 'w',
              encoding='utf-8') as f:
        json.dump(data, f, indent=3, ensure_ascii=False)


def frends():
    response = requests.post(
        f'https://api.vk.com/method/friends.get?user_id=581057984&access_token={token}&v=5.131',
        params=params,
        headers=headers)
    print(response.json())


def main():
    group_name = 'kuban24_tv'
    get_wall_posts(group_name)
    frends()


if __name__ == '__main__':
    main()
