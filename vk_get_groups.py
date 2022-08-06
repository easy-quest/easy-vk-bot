import time

import vk

from core.core import *

session = vk.Session(access_token=token)  #VK token
api = vk.API(session)
group_id = 'fineline_official'
group_stat = api.groups.getMembers(group_id=group_id, count=10)
groups_dict = {}

if group_stat['count'] <= 1000:
    for mid in group_stat['users']:
        try:
            # time.sleep(1)
            groups = api.users.getSubscriptions(user_id=mid)['groups']
            groups_id = groups['items']
            for gid in groups_id:
                if gid in groups_dict:
                    groups_dict[gid] += 1
                else:
                    groups_dict[gid] = 1
        except:
            pass
else:
    print('>1000')
    exit()

lst_sort = [(k, groups_dict[k])
            for k in sorted(groups_dict, key=groups_dict.get, reverse=True)]
print(lst_sort[:10])
