import os

def create_filename(filename):
    """
    生成一个当前目录下不存在的文件名，如当存在'a_1.mp3'则生成'a_2.mp3'
    :param filename:
    :return:
    """
    while os.path.exists(filename):
        name, suffix = os.path.splitext(filename)
        filename = name.split('_')[0] + '_' + str(int(name.split('_')[1]) + 1) + suffix
        create_filename(filename)
    return filename

create_filename('a_1.mp3')

