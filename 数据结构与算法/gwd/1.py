'''
[(1,{"date":"2015-3-1"},"jack"),(2,{"date":"2015-3-2"},"tom")...]，写程序根据date先后排序
'''

def sort_func(lst):
	return sorted(lst, key=lambda x: x[1]['date'])

if __name__ == '__main__':
	lst = [(1,{"date":"2015-3-1"},"jack"),(2,{"date":"2015-3-2"},"tom"),(2,{"date":"2015-2-2"},"haha")]
	print('before sorted:', lst)
	print('after sorted:', sort_func(lst))