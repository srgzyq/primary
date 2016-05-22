def select(s):
	for i in range(len(s)):
		#print "i=",i
		#print s
		minIndex = i
		minValue = s[i]
		#print "minIndex=%d,minValue=%d,i=%d" % (minIndex,minValue,i)
		for j in range(i+1,len(s)):	
			#print "s[%d]=%d,minValue=%d"%(j,s[j],minValue)
			if minValue > s[j]:
				minValue = s[j]
				minIndex = j
				#print "s[%d]=%d,minValue=%d"%(j,s[j],minValue) 

		temp = s[i]
		s[i] = minValue
		s[minIndex] = temp 
		print s
	#return s

def bobbleSort(L):
	for j in range(len(L)):
		for i in range(len(L)-1):
			if L[i] > L[i+1]:
				temp = L[i]
				L[i] = L[i+1]
				L[i+1] = temp
		print L

def bobbleSort2(L):
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(L)-1):
			if L[i] > L[i+1]:
				temp = L[i]
				L[i] = L[i+1]
				L[i+1] = temp
				swapped = True
		print L

print "run selective test 1"
s = [1,6,3,4,5,2,-1,0]
#select(s)
#bobbleSort(s)
bobbleSort2(s)