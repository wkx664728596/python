

# from config import *
# from dev_config import *
from app_resource import db_url
from sqlalchemy import create_engine
db_engine = create_engine(db_url)


def getCountSql(sql):

    """
    返回count语句的数量结果
    print("result:%s"%getCountSql("SELECT count(*) FROM zqt_doc"))
    :param sql:
    :return:
    """
    r = db_engine.execute(sql)
    ru = r.fetchall()[0][0]
    return ru


def updateSql(sql,pargm=None):
    """
    执行更新语句
    :param sql:
    :return:
    """
    if not pargm:
        sql = sql.replace('%','%%')
    r = db_engine.execute(sql, pargm) if pargm else db_engine.execute(sql)
    try:
        return r.fetchone()
    except Exception as e:
        print(e)
        return r.rowcount

def getSelectSql(sql,pargm=None):
    """
    返回select语句的结果集
    :param sql:
    :return:
    """
    if not pargm:
        sql = sql.replace('%','%%')
    try:
        r = db_engine.execute(sql, pargm) if pargm else db_engine.execute(sql)
    except Exception:
        r = db_engine.execute(sql, pargm) if pargm else db_engine.execute(sql)
    return r.fetchall()


