#!/usr/bin/python3.5
if name == 'Alice':
    print('Hi,Alice.')
else:
    print('Hello,stranger.')


if name == 'Alice':
    print('Hi,Alice.')
elif age < 12:
    print('You are not Alice, kiddo')
elif age > 2000:
    print('Unlike you,Alice is not an immortal vampire.')
elif age >100:
    print('You are not Alice, grannie.')


if name == 'Alice':
    print('Hi,Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')


spam = 0
while spam < 5:
    print ('Hello,world.')
    spam = spam +1

spam = 0
if spam < 5:
    print ('Hello,world.')
    spam = spam +1


name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print ('Thank you!')