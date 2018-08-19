#！/usr/bin/python3.5

##执行没有结果
def spam():
    global eggs
    eggs = 'spam' #global

    def bacon():
        eggs = 'bacon' #local
    def ham():
        print(eggs) #global

    eggs = 42
    spam()
    print(eggs) 




