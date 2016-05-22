#-*- encoding: utf-8 -*-
'''
Created on 2016-05-22 15:45:47
Updated on 2016-05-22 15:46:57

@author: Srgzyq
'''


def maxVal(w, v, i, aW):
    '''
            v 价值，w 重量, i 深度,向量减一,下标值
    '''
    # print 'maxVal called with', i, aW
    global numCalls
    numCalls += 1
    # 最后一个元素
    if i == 0:
        # 依然可以放下最后一个物品
        if w[i] <= aW:
            return v[i]
        else:
            return 0

    # 不是最后一个元素，也不能放入
    without_i = maxVal(w, v, i - 1, aW)
    if w[i] > aW:
        return without_i
    else:
        with_i = v[i] + maxVal(w, v, i - 1, aW - w[i])
    return max(with_i, without_i)


def fastMaxVal(w, v, i, aW, m):
    global numCalls
    numCalls += 1
    try:
        return m[(i, aW)]
    except KeyError:
        if i == 0:
            if w[i] <= aW:
                m[(i, aW)] = v[i]
                return v[i]
            else:
                m[(i, aW)] = 0
                return 0
        without_i = fastMaxVal(w, v, i - 1, aW, m)
        if w[i] > aW:
            m[(i, aW)] = without_i
            return without_i
        else:
            with_i = v[i] + fastMaxVal(w, v, i - 1, aW - w[i], m)
            res = max(with_i, without_i)
            m[(i, aW)] = res
            return res


def maxVal0(w, v, i, aW):
    m = {}
    return fastMaxVal(w, v, i, aW, m)

if __name__ == '__main__':
    # weights = [1, 5, 3, 4]
    # vals = [15, 10, 9, 5]
    # numCalls = 0
    # res = maxVal(weights, vals, len(vals) - 1, 8)
    # print 'max Val = ', res, 'numCalls of calls = ', numCalls

    weights = [1, 1, 5, 5, 3, 3, 4, 4]
    vals = [15, 15, 10, 10, 9, 9, 5, 5]
    # weights = [5, 3, 2]
    # vals = [9, 7, 8]
    weight = 8
    numCalls = 0
    res = maxVal(weights, vals, len(vals) - 1, weight)
    print 'max Val = ', res, 'numCalls of calls = ', numCalls

    numCalls = 0
    res = maxVal0(weights, vals, len(vals) - 1, weight)
    print 'max Val = ', res, 'numCalls of calls = ', numCalls
