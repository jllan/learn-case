import os
import pandas as pd
import csv
import collections

def find_files():
    files = os.listdir('.')
    files = [file for file in files if os.path.splitext(file)[1] in ['.xls', 'xlsx']]
    return files

def handle_file(filename):
    data = pd.read_excel(filename)
    data2 = data.ix[3:, [0, 1, 6, 7, 8, 9]]     # 只取户主编号，户主名，东南西北邻居
    data2.columns = '序号', '户主', '东', '南', '西', '北'  # 重新设置columns
    data3 = data2.dropna(how='all')             # 去除全为空的行
    data4 = data3.fillna(method='ffill')        # 用前向填充的方式填充没有户主名和户主编号的行
    data4 = data4[:-1]
    data5 = data4[data4!='道路'][data4!='沟渠'][data4!='集体地'][data4!='林带']
    data_dict = dict(zip(data5['户主'], data5['序号']))
    # print(data_dict)
    results_dict = collections.OrderedDict()
    for inx, row in data5.iterrows():
        nei = row[['东', '南', '西', '北']][pd.notnull(row)]    # 户主每块地的四邻
        nei_id = [str(data_dict.get(name)) for name in nei if name in data_dict]  # 户主每块地的四邻的id
        ids = results_dict.get(row['户主'], set())    # 用一个set()来保存四邻的id，初始为空set
        ids.update(nei_id)
        results_dict[row['户主']] = ids

    result_filename = os.path.join(save_directory, filename.split('.')[0]+'_result.csv')
    with open(result_filename, 'w') as csvfile:
        fieldnames = ['序号', '户主', '四邻']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for key, value in results_dict.items():
            writer.writerow({'序号': data_dict[key], '户主': key, '四邻': value})
    return result_filename.split('/')[-1]


if __name__ == '__main__':
    save_directory = 'csv_directory'
    if not os.path.exists(save_directory):
        os.mkdir(save_directory)
    files = find_files()
    if files:
        for file in files:
            handle_file(file)
