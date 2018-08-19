#!/usr/bin/python3.5

filename = "/home/isyang/Code/AutomateTheBoringStuffWithPython/chapter_8/8_2_3_write_file.txt"

baconFile = open(filename, 'w')         # 创建写
baconFile.write('hello world\n')
baconFile.close()

baconFile = open(filename, 'a')         # 加， append
baconFile.write('aaaaaaaaaaaaaaaaaaaaaaaaaa')
baconFile.close()

baconFile = open(filename, 'r')              # 读
content = baconFile.read()
baconFile.close()

print(content)



