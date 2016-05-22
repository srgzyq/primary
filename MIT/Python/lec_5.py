# -*- coding:utf-8 -*- #
def squareRootBi(x, epsilon):
	assert x >=0, 'x must be non-negative, not ' + str(x)
	assert epsilon > 0, 'epsilon must be positive, not ' + str(epsilon)
	low = 0
	high = max(x,1.0)
	guess = (low + high)/2.0
	ctr = 1
	while abs(guess**2 - x) > epsilon and ctr <= 100:
		# print 'low: ', low, 'high: ', high, 'guess: ', guess
		if guess ** 2 < x:
			low = guess
		else:
			high = guess
		guess = (low + high) /2.0
		ctr += 1
	assert ctr <= 100 , 'Iteration count excooded'
	print "Bi method. "+" Num. iterations: "+ str(ctr)+ " Estimate: "+ str(guess)
	return guess

def squareRootNR(x, epsilon):
	assert x >=0, 'x must be non-negative, not ' + str(x)
	assert epsilon > 0, 'epsilon must be positive, not ' + str(epsilon)
	x = float(x)
	guess = x/2.0
	#guess = 0.001
	diff = guess ** 2 - x
	ctr = 1
	while abs(diff) > epsilon and ctr <= 100:
		#print 'Error: ', diff, 'guess:', guess
		guess = guess - diff/(2.0*guess)
		diff = guess**2 - x
		ctr += 1
	assert ctr <= 100 , 'Iteration count excooded'
	print "squareRootNR method. "+" Num. iterations: "+ str(ctr)+ " Estimate: "+ str(guess)
	return guess


def testBi():
	print "squareRootBi(4, 0001)"
	squareRootBi(4, 0.0001)
	print "squareRootBi(9, 0.0001)"
	squareRootBi(9, 0.0001)
	print "squareRootBi(2, 0.0001)"
	squareRootBi(2, 0.0001)
	print "squareRootBi(0.25, 0.0001)"
	# 不在二分查找的区间
	squareRootBi(0.25, 0.0001)

squareRootNR(4, 0.0001)
squareRootNR(0.25, 0.0001)
#testBi()