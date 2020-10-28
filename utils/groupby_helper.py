
# lambda匿名函数的格式：冒号前是参数，可以有多个，用逗号隔开，冒号右边的为表达式。其实lambda返回值是一个函数的地址，也就是函数对象。
# p = lambda x,y:x+y
#
# print(p(2,3))

import itertools


mate_json = [{'icodes':'123','inums':2,'inames':'花洒a-美的'},
             {'icodes': '124', 'inums': 2, 'inames': '花洒a-美的'},
             {'icodes': '123', 'inums': 4, 'inames': '花洒a-美的'},
             {'icodes': '125', 'inums': 2, 'inames': '花洒a-美的'},
             {'icodes': '125', 'inums': 2, 'inames': '花洒a-美的'}]

def group_json(mate_json):
    mate_list = []
    # 分组前先排序

    mate_json.sort(key=lambda x: x["icodes"])
    for key, group in itertools.groupby(mate_json, key=lambda x: x['icodes']):
        count = 0
        fgoods_name = ''
        for i in list(group):

            fcount = i.get('inums') or 0
            fgoods_name = i.get('inames') or ''
            if fgoods_name:
                fgoods_name1 = fgoods_name.rsplit('-',1)
                fgoods_name2 =fgoods_name1[0]
            count += int(fcount)
        mate_list.append({
            'icodes': key,
            'inames': fgoods_name2,
            'inums': count
        })
    return mate_list

if __name__ == '__main__':
    mate_list = group_json(mate_json)
    print(mate_list)