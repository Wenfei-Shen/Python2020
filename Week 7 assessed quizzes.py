# 4

def dict_build(keys, values):
    len1 = len(keys)
    len2 = len(values)
    if len1 != len2:
        return None
    else:
        res_dic = { keys[i] : values[i] for i in range(0, len1)}
        return res_dic


print(dict_build(['a','c'],[1,2,3])== None)