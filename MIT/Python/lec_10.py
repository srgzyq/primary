def merge(left, right):
	result = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i = i + 1
		else:
			result.append(right[j])
			j = j + 1

	while (i < len(left)):
		result.append(left[i])
		i = i + 1

	while (j < len(right)):
		result.append(right[j])
		j = j + 1

	return result


def mergesort(L):
	print L
	if len(L) < 2:
		return L[:]
	else:
		middle = len(L) / 2
		left = mergesort(L[:middle])
		#print "left= ", left
		right = mergesort(L[middle:])
		#print "right= ", right
		together = merge(left,right)
		print 'merge: ', together
		return together

#mergesort([1,4,3,6,5,2,8,7])

def readFloat(requestMsg, errorMsg):
	while True:
		val = raw_input(requestMsg)
		try:
			val = float(val)
			return val
		except:
			print(errorMsg)

#print readFloat('Enter float: ', 'Not a float.')

def readVal(valType, requestMsg, errorMsg):
	while True:
		val = raw_input(requestMsg)
		try:
			val = valType(val)
			return val
		except:
			print(errorMsg)

#print readVal(int, 'Enter int: ', 'Not an int.')

class GetGradesError(Exception):
	pass
		

def getGrades(fname):
	try:
		gradesFile = open(fname, 'r')
	except IOError:
		print "Could not open", fname
		raise GetGradesError
		
	print 'hello'
	grades = []
	for line in gradesFile: grades.append(float(line))
	return grades

try:
	grades = getGrades('qlgrades.txt')
	grades.sort()
	median = grades[len(grades)/2]
	print 'Median grade is', median
except GetGradesError:
	print 'Wboops'