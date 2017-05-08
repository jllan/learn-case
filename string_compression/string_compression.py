# 算法一
def str_compress1(string):
    result = []
    current = string[0]
    count = 1
    for s in string[1:]:
        if s == current:
            count += 1
        else:
#           result += current + str(count)
            result.append(current)
            result.append(str(count))
            current = s
            count = 1
#   result += current + str(count)
    result.append(current)
    result.append(str(count))
#   return result
    return ''.join(result)



# 算法二
# 使用itertools模块的groupby方法
from itertools import groupby

def str_compress2(string):
    result = []
    for key, group in groupby(string):
        result.append(key)
        result.append(str(len(list(group))))
    return ''.join(result)


if __name__ == '__main__':
    s = 'abbbbffcccdddcc'
    print(str_compress1(s))
    print(str_compress2(s))
