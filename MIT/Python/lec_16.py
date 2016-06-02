#-*- encoding: utf-8 -*-
'''
Created on 2016-06-02 14:25:15

@author: Srgzyq
'''


class Person(object):
    """docstring for Person"""

    def __init__(self, family_name, first_name):
        self.family_name = family_name
        self.first_name = first_name

    def familyName(self):
        return self.family_name

    def firstName(self):
        return self.first_name

    def __cmp__(self, other):
        return cmp((self.family_name, self.first_name), (other.familyName(), other.firstName()))

    def __str__(self):
        return "<Person: %s %s>" % (self.family_name, self.first_name)

    def say(self, toWhom, something):
        return self.first_name + " " + self.family_name + " says to " + toWhom.firstName() + ' ' + toWhom.familyName() + ":" + something

    def sing(self, toWhom, something):
        return self.say(toWhom, something + " tra la la")


class MITPerson(Person):
    nextIDNum = 0

    def __init__(self, familyName, firstName):
        Person.__init__(self, familyName, firstName)
        self.idNum = MITPerson.nextIDNum
        MITPerson.nextIDNum += 1

    def getIdNum(self):
        return self.idNum

    def __str__(self):
        return "MIT Person: %s %s" % (self.family_name, self.first_name)

    def __cmp__(self, other):
        return cmp(self.idNum, other.idNum)


class UG(MITPerson):

    def __init__(self, familyName, firstName):
        MITPerson.__init__(self, familyName, firstName)
        self.year = None

    def setYear(self, year):
        if year > 5:
            raise OverflowError("Too many")
        self.year = year

    def getYear(self):
        return self.year

    def say(self, toWhom, something):
        return MITPerson.say(self, toWhom, "Excuse me, but " + something)


class Prof(MITPerson):

    def __init__(self, familyName, firstName, rank):
        MITPerson.__init__(self, familyName, firstName)
        self.rank = rank
        self.teaching = {}

    def addTeaching(self, term, subj):
        try:
            self.teaching[term].append(subj)
        except KeyError:
            self.teaching[term] = [subj]

    def getTeaching(self, term):
        try:
            return self.teaching[term]
        except KeyError:
            return None

    def lecture(self, toWhom, something):
        return self.say(toWhom, something + ' as it is obvious')

    def say(self, toWhom, something):
        if type(toWhom) == UG:
            return MITPerson.say(self, toWhom, 'I do not understand why you say ' + something)
        elif type(toWhom) == Prof:
            return MITPerson.say(self, toWhom, 'I really liked your parper on ' + something)
        else:
            return self.lecture(something)


class Faculty(object):
    """docstring for Faculty"""

    def __init__(self):
        self.names = []
        self.IDs = []
        self.members = []
        self.place = None

    def add(self, who):
        if type(who) != Prof:
            raise TypeError('not a professor')
        if who.getIdNum() in self.IDs:
            raise ValueError('duplicate ID')
        self.names.append(who.familyName())
        self.IDs.append(who.getIdNum())
        self.members.append(who)

    def __iter__(self):
        self.place = 0
        return self

    def next(self):
        if self.place >= len(self.names):
            raise StopIteration
        self.place += 1
        return self.members[self.place - 1]


if __name__ == '__main__':
    grimson = Prof('Grimson', 'Eric', 'Full')
    lozano = Prof('Lozano-Perez', 'Tomas', 'Full')
    guttag = Prof('Cuttag', 'John', 'Full')
    barzilay = Prof('Barzilay', 'Regina', 'Associate')
    course6 = Faculty()
    course6.add(grimson)
    course6.add(lozano)
    course6.add(guttag)
    for p in course6:
        print p.familyName()

    ug = UG('Doe', 'Jane')
    print ug.say(grimson, 'I do not understand')
    print grimson.say(ug, 'you do not understand')
    print grimson.say(guttag, 'why the sky is blue')
    print ug.sing(ug, 'I think I finally understand')
    # me = Prof('Grimson', 'Eric', 'Full')
    # me.addTeaching('F08', '6.00')
    # me.addTeaching('S09', '6.00')
    # me.addTeaching('S09', '6.xxx')
    # print me.getTeaching('F08')
    # print me.getTeaching('S09')
    # print me.getTeaching('S08')
    # print me.teaching
    # ug = UG("xiao", "mei")
    # print me.say(ug, "study")
    # print ug.familyName()
    # a = MITPerson("xiao", "mei")
    # print ug == a
    # c = Person("shi", "xin")
    # print c == ug
    # p1 = MITPerson("xiao", "mei")
    # print p1.getIdNum()
    # print p1
    # p2 = MITPerson("sr", "gzyq")
    # print p2.getIdNum()
    # print p2
    # print p1.say(p2, "study")
    # a = Person("shi", "rui")
    # print a.say(a, "learn to python!")

    # b = Person("shi", "rui")
    # c = Person("shi", "xin")
    # print a.sing(c, "beijing")
    # print a.sing(a, "beijing")
    # print a
    # print c
    # print a == b
    # print a == c
