'''
已知文本文件，以 \n 为行结束符，每行包含两个字符串 key和value，中间用 \t 分割，key和value均有可能重复出现，输入文件内容格式举例：
2687694 18070300
2687694 18070300
2687694 18070500
2687694 18070500
2687697 15050000
2687697 15050000
2687697 15050500
2687697 15050500
请写程序统计下列信息：
1） 每个key对应多少不同的唯一value？
2） 每个不同的value出现次数是多少？
并按value次数从大到小输出结果文件(key1:value1,count1;value2,count2....\nkey2:value1,count1;value2,count2....)

输出文件格式举例：
2687694:18070300,2;18070500,2
2687697:15050000,2;15050500,2
'''

import pandas as pd

def fun():
    data = pd.read_table('data.txt', names=['key', 'value'], index_col='key')
    print(data)
    results = []
    index_unique = data.index.unique()
    print(index_unique)
    for inx in index_unique:
        temp = pd.value_counts(data.loc[inx]['value'])
        print(temp)
        for value, count in temp.items():
            result = {}
            result[inx] = (value, count)
            results.append(result)
    return results

print(fun())