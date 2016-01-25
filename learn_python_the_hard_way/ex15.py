# -*- coding: utf-8 -*- #
from sys import argv

# 命令行获取文件名
script, filename = argv
# 打开文件
txt = open(filename)

print "Here's your file %r:" % filename
# 打印文件内容
print txt.read()

#txt.truncate()

# 关闭文件
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
