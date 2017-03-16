#_*_coding:utf-8 _*_

#用二分法求平方根
def sqrt_dichotomy(x, max, min=0):
	print x, min, max
	mid = (min + max)/2.0
	print mid
	if (mid * mid) - x > 0.0001:
		max = mid
		sqrt_dichotomy(x, max, min)
	if (mid * mid) - x < -0.0001:
		min = mid
		sqrt_dichotomy(x, max, min)
	else:
		return mid

if __name__ == '__main__':
	x = 1024
	max = x
	print sqrt_dichotomy(x, max)
