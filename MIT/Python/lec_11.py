
def silly():
    res = []
    done = False
    while not done:
        elem = raw_input("Enter element. return when done.")
        if elem == "":
            done = True
        else:
            res.append(elem)

    tmp = res[:]
    tmp.reverse()
    isPal = (res == tmp)
    if isPal:
        print "is a palindrose"
    else:
        print "is not a palindrose"

