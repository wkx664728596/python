# -*- coding: utf-8 -*-


from spyne import Application, rpc, ServiceBase
from spyne import Integer, Unicode, Array, ComplexModel, Iterable, String,table

from helper.db_hepler import updateSql

from helper.log_helper import write_log
import json
from helper.checkin_helper import check_hr_user,hr_user_list
# 换宿
class CheckSwitchService(ServiceBase):
    @rpc(Unicode,Unicode, _returns=String)
    def hs_switch_drom(self, method, data_json):
        try:
            print(method)
            print(data_json)
            data_list = json.loads(data_json)
            info = []

            for i in data_list:
                fswitch_person_num = i.get('fswitch_person_num')  # 工号
                if not fswitch_person_num:
                    return json.dumps({"success": 0,
                                     "state": "500",
                                     "message": "工号不存在",
                                     })
                # 校验录入人员信息,获取人员信息
                user_msg = check_hr_user(fswitch_person_num)
                if user_msg:
                    i['fduty_code'] = user_msg.get('fduty_code')
                    i['femp_gender'] = user_msg.get('femp_gender') or ''
                else:
                    rs = {
                        '工号': fswitch_person_num,
                        '姓名': i.get('fswitch_person_name')
                    }

                    info.append(rs)
            if info:
                return json.dumps({"success": 0,
                                   "state": "500",
                                   "message": "hr系统暂无人员信息,%s不存在,请稍后操作或检查人员工号"%info
                                   })


            for data in data_list:
                fswitch_person_num = data.get('fswitch_person_num')  # 工号
                fswitch_person_name = data.get('fswitch_person_name')  # 姓名
                fswitch_date = data.get('fswitch_date')  # 申请入住日期
                fswitch_person_degree = data.get('fswitch_person_degree')
                fswitch_person_company = data.get('fswitch_person_company')
                fswitch_person_dept = data.get('fswitch_person_dept').lower()
                fremark = data.get('fremark') or ''
                inten_area = data.get('inten_area') or ''
                inten_room = data.get('inten_room') or ''
                inten_room_detail = data.get('inten_room_detail') or ''
                fduty_code = data.get('fduty_code') or ''
                femp_gender = data.get('femp_gender') or ''



                # 插入待入住人员信息到待入住表
                insert_fcheck_user = """
                xxxxxx
                """ 

                updateSql(insert_fcheck_user)
            rs =  json.dumps({
              "success": 1,
              "state": "200",
              "message": "人员换宿请求提交成功",
            }
            )
            # 写入oa 日志 自定义 方法 写入数据库
            write_log(method, "xxxx", data_json, rs,'success')
            return rs
        except Exception:
            rs = json.dumps({"success": 0,
                             "state": "500",
                             "message": "异常",
                             })
            write_log(method, "http://60.12.95.62:5001/?wsdl", data_json, rs, 'error')
            return rs
