# -*- coding:utf-8 -*- #
# 
# code file for lecture 8

# b次循环，每次有三次基本操作，一次比较，一次乘法，一次减法
# 循环外有2次基本操作
# 2 + 3b
# 300-902,3000-9002,30000-90002
# 不关心附加常量
# b 线性
def exp1(a, b):
	ans = 1
	while (b > 0):
		ans *= a
		b -= 1
	return ans

# 一次比较 一次乘法 一次减法 当b-k=1 停止
# 线性增长
# t(b)=3 + t(b-1)
# 	  =3 + 3 + t(b-2)
# 	  =3k + t(b-k)
# 	  当 b-k = 1 停止 k = b-1
# 	  =3(b-1) + t(1)
# 	  =3(b-1) + 2
# 	  =3b-1
# 	  
def exp2(a, b):
	if b == 1:
		return a
	else: return a * exp2(b-1)

# 如何 b是偶数
# t(b) = 6 + t(b/2)
# b 是 奇数
# t(b) = 6 + t(b-1) 
#  	   = 6 + (6 + t((b-1)/2)
#  	   = 12 + t((b-1)/2)
#  	   = 12 + t(b/2)
#  	   = 12 + 12 + t(b/4)
#	   = 12k + t(b/2^k)
#	   当b/2^k = 1 停止 k = log2(b)
#
#	   O(logb) 对数级

def exp3(a, b):
	if b == 1:
		return a
	if (b%2)*2 == b:
		return exp3(a*a, b/2)
	else: return a*exp3(a,b-1)

# O(n*m) if m == n O(n^2)
def g(n, m):
 	x = 0
 	for i in range(n):
 		for j in range(m):
 			x += 1
 	return x

# 汉诺塔
#o(2^n)
def towers(size,fromStack,toStack,spareStack):
	if size == 1:
		print "Move disk from",fromStack," to ", toStack
	else:
		towers(size-1,fromStack,spareStack,toStack)
		towers(1,fromStack,toStack,spareStack)
		towers(size-1,spareStack,toStack,fromStack)

#towers(3,'A','B','C')

def search(s, e):
	answer = None
	i = 0
	numCompares = 0
	while i < len(s) and answer == None:
		numCompares += 1
		if e == s[i]:
			answer = True
		elif e < s[i]:
			answer = False
		i += 1
	print answer, numCompares

def bsearch(s, e, first, last):
	print first,last
	if (last - first) < 2:
		return s[first] == e or s[last] == e
	mid = first + (last - first)/2
	if s[mid] == e: return True
	if s[mid] > e: return bsearch(s,e,first,mid-1)
	return bsearch(s,e,mid+1,last)

def wsearch(s,e,first,last):
	while (last - first) >= 0:
		mid = first + (last - first)/2
		print "first=%d,last=%d,mid=%d" % (first, last, mid)
		if (last - first) < 2:
			return s[first] == e or s[last] == e
		if s[mid] == e: return True
		if s[mid] > e:
			last = mid - 1
		else:
			first = mid +1


#s = [1,2,3,4,5,6]
#print "bsearch: " , bsearch(s,4,0,len(s)-1)
#print "wsearch: " , wsearch(s,4,0,len(s)-1)

s = range(10000000)
print "bsearch: " , bsearch(s,-1,0,len(s)-1)
print "wsearch: " , wsearch(s,-1,0,len(s)-1)