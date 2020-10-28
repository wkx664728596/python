def rows_2_dic(fields,rows):
    rs = []
    for row in rows:
        dic = {}
        for index, value in enumerate(fields):
            dic[value] = row[index]
        rs.append(dic)
    return rs