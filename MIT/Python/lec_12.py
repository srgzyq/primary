# -*- coding: utf-8 -*-
def fib(n):
    global numCalls
    numCalls += 1
    # print "fib called with", n
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

numCalls = 0
n = 30
res = fib(n)
print 'fib of', n, '=', res, 'numCalls =', numCalls


def fastFib(n, memo):
    global numCalls
    numCalls += 1
    # print "fib called with", n
    if not n in memo:
        memo[n] = fastFib(n - 1, memo) + fastFib(n - 2, memo)
    return memo[n]


def fib1(n):
    memo = {0: 1, 1: 1}
    return fastFib(n, memo)

numCalls = 0
n = 50
res = fib1(n)
print 'fib of', n, '=', res, 'numCalls =', numCalls


def fastFibOther(n):
    # 迭代效率更高
    global numCalls
    numCalls += 1
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, b + a
        numCalls += 1
    return b

numCalls = 0
n = 50
res = fastFibOther(n)
print 'fib of', n, '=', res, 'numCalls =', numCalls
