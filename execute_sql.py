from exts import db


def dict_fetchall(sql):
    """
    执行原生SQL语句的查询操作
    :param sql: SQL语句
    :return: list
    """
    handler = db.session.execute(sql)
    desc = handler.cursor.description
    handler.cursor.close()
    return [dict(zip([col[0] for col in desc], row)) for row in handler.fetchall()]
