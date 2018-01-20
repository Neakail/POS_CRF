# -*- encoding:utf-8 -*-

number = 10
g = open('process_data/' + str(number) + '.txt', 'w')

for i in xrange(1,11):
    if i != number:
        filename = 'data/' + str(i) + '.txt'
        f =  open(filename,'r')
        for content in f.readlines():
            g.write(content)


g.close()