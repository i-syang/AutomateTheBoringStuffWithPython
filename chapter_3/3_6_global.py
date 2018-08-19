#！/usr/bin/python

def spam():
    print(eggs)
    eggs = 'spam local'

eggs = 'global'
spam()
