# -*- coding: utf-8 -*- #
from sys import argv

# 获取文件名
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C."
print "If you do want that, hit RETURN."

raw_input("?")

# 打开文件
print "Opening the file..."
target = open(filename, 'w')

# 清空文件
# write 模式不需要 清空函数
#print "Truncating the file.   Goodbye!"
#target.truncate()

# 输入需要写入文件的内容
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# 写入文件
print "I'm going to write these to the file."

target.write(line1 + '\n' + line2 + '\n' + line3)

'''
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
'''

print "And finally, we close it."
target.close()
