from sqlalchemy import create_engine
# sqlalchemy数据库
engine = create_engine(db_url,echo=True)
connection = engine.connect()

# update 为utils中 工具类
# 开启事务 不回 读到commit 前的修改数据


# sql 事务开启demo 手动
@app.route('/insert/demo')
def insert_demo():
    try:
        tran = connection.begin()
        up_sql = "insert into js_demo(f1, f2) VALUES ( '%s','%s')"%('test1','test1')
        updateSql(up_sql)
        up_sql1 = "insert into js_demo(f1, f2) VALUES ('%s','%s')"%('test2','test2')
        updateSql(up_sql1)
        up_sql2 = "insert into js_demo(f1, f2) VALUES ('%s','%s')"%('test3','test3')
        updateSql(up_sql2)
        tran.commit()
        tran.close()

        return make_response('success',200)
    except:
        # 回滚
        tran.rollback()
        tran.close()
        return make_response('error',500)
