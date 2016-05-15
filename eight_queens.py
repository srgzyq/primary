# --coding:utf-8-- #


def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        # print i
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False


def printMap(state, x=4, y=4):
    for y1 in range(y):
        for x1 in range(x):
            if state[y1] == x1:
                print "X",
            else:
                print "O",
        print "\n"


def fourbase():
    x = 4

    # 第一行x 4
    state.append(2)

    # 第二行
    for i in range(x):
        if not conflict(state, i):
            state.append(i)
            break

    # 第三行
    # print conflict(state,0)
    for i in range(x):
        if not conflict(state, i):
            state.append(i)
            break

    for i in range(x):
        if not conflict(state, i):
            state.append(i)
            break


def fourBack(num=4, result=[]):
    for x in range(num):
        if not conflict([], x):
            for i in range(num):
                if not conflict([x], i):
                    for j in range(num):
                        if not conflict([x, i], j):
                            for k in range(num):
                                if not conflict([x, i, j], k):
                                    result.append([x, i, j, k])
                                    print [x, i, j, k]


def queens(num=4, state=(), result=[]):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                # print state + (pos,)
                result.append(state + (pos,))
            else:
                queens(num, state + (pos,), result)


if __name__ == '__main__':
    # 下标表示y纵轴 值表示x横轴
    # 数组长度为，需要查找的层数
    state = []

    rs = []
    queens(8, (), rs)
    # print rs
    print "8 皇后拥有的种类:", len(rs)
    print "8 皇后拥有的3种:"
    printMap(rs[3], 8, 8)
