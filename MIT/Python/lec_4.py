def sqrt(x):
	ans = 0
	if x >= 0:
		while ans * ans < x: ans = ans + 1
		if ans * ans != x:
			print x, 'is not a perfect square'
			return None
		else: return ans
	else:
		print x, 'is a negative number'
		return None

def solve(numLegs, numHeads):
	for numChicks in range(0,numHeads + 1):
		numPigs = numHeads - numChicks
		totLegs = 4 * numPigs + 2 * numChicks
		if totLegs == numLegs:
			return [numPigs, numChicks]
	return [None, None] 

def barnYard():
	heads = int(raw_input('Enter number of heads: '))
	legs = int(raw_input('Enter number of legs: '))
	pigs, chickens = solve(legs, heads)
	if pigs == None:
		print "There "
	else:
		print "Number of pigs: ", pigs
		print "Number of chickens: ", chickens

def solve1(numLegs, numHeads):
	for numSpiders in range(0, numHeads + 1):
		for numChicks in range(0, numHeads - numSpiders + 1):
			numPigs = numHeads - numChicks - numSpiders
			totLegs = 4 * numPigs + 2 * numChicks + 8 * numSpiders
			if totLegs == numLegs:
				return [numPigs, numChicks, numSpiders]
	return [None, None, None]

def barnYard1():
	heads = int(raw_input('Enter number of heads: '))
	legs = int(raw_input('Enter number of legs: '))
	pigs, chickens, spiders = solve1(legs, heads)

	if pigs == None:
		print "There is no numbers"
	else:
		print "Number of pigs" , pigs
		print "Number of chickens", chickens
		print "Number of spiders", spiders

def solve2(numLegs, numHeads):
	solutionFound = False
	for numSpiders in range(0, numHeads + 1):
		for numChicks in range(0, numHeads - numSpiders + 1):
			numPigs = numHeads - numChicks - numSpiders
			totLegs = 4 * numPigs + 2 * numChicks + 8 * numSpiders
			if totLegs == numLegs:
				print "Number of pigs: " + str(numPigs)
				print "Number of chickens: " + str(numChicks)
				print "Number of spiders: " + str(numSpiders)
				solutionFound = True
	if not solutionFound: print "There is no solution"

def isPalindrome(s):
	if len(s) <= 1: return True
	else: return s[0] == s[-1] and isPalindrome(s[1:-1])

def isPalindrome1(s, indent):
	print indent, 'isPalindrome called with', s
	if len(s) <= 1:
		print indent, 'About to return True from base'
		return True
	else:
		ans = s[0] == s[-1] and isPalindrome1(s[1:-1],indent+indent)
		print indent, 'About to return', ans
		return ans

def fib(x):
	if x == 0 or x == 1: return 1
	else: return fib(x-1) + fib(x-2)

print fib(36)

#print isPalindrome('abcba')
#print isPalindrome('abc')
#print isPalindrome1('abceecba',' ')

#barnYard1()
#barnYard()

#a=sqrt(16)
#print a
#test = sqrt(34)
#print test == None

#def f(x):
#	x = x + 1
#	return x

#x = 3
#z = f(x)
#print x
#print z