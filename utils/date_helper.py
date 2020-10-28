
import datetime
import json

#
class DateEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o,(datetime.datetime,datetime.date)):
            return  o.strftime('%Y-%m-%d')
        super(DateEncoder,self).default(o)


# 处理日期格式错误
# 在controller 中return json.dumps({"code": 200, "msg": "获取成功",
                           # "count": rowscount[0][0], "data": rs}, cls=DateEncoder)