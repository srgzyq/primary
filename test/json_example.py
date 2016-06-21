#-*- encoding: utf-8 -*-
'''
Created on 2016-06-21 14:56:52

@author: Srgzyq
'''
try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name='Bob', age=20, score=88)
# 把任意对象序列化成一个str,然后就可以把这个str写入文件
print pickle.dumps(d)

# pickle.dump 直接将内容序列化之后写入文件
#f = open('dump.txt', 'wb')
#d = pickle.dump(d, f)
# f.close()

# pickle.load 将序列转化给对象
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print d

# Json 不同语言之间的传递和序列化
# dumps 返回字符串
import json
d = dict(name='Bob', age=20, score=88)
s = json.dumps(d)
print "type: " + str(type(s)) + " s= " + s

# loads 将字符串转化为对象
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
s = json.loads(json_str)
print "type: " + str(type(s))
print s
