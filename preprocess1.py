# -*- coding:utf-8 -*-

for i in xrange(1,11):
    f = open('data/'+ str(i) +'.txt','r')
    g = open('process3_1/' + str(i) + '.txt','w')
    for i in f.readlines():
        # print i
        try:
            word = i.split(' ')[0]
            tag = i.split(' ')[1]
            new_i = word + ' ' + word[0:3] + ' ' + word[-3:] + ' ' + word[0:2] + ' ' + word[-2:] + ' ' + word[0:4] + ' ' + word[-4:] + ' ' + tag
            g.write(new_i)
        except:
            g.write(i)

    f.close()
    g.close()