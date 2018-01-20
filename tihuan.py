# -*- coding:utf-8 -*-

import json
import chardet
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# one word 24
# two word 24
fp = open('2.json','r')
data = json.load(fp)

# stastic
# number = 0
# for i in data:
#     sentence = data[i]
#     if len(sentence) == 3:
#         number += 1
#         print sentence[0] +'    ' +  sentence[1]
#
# print number

yingshe = {
    u'并列连词':'CC',
    u'基数词':'CD',
    u'序数词':'OD',
    u'限定词':'DT',
    u'外来词':'FW',
    u'介词':'IN',
    u'形容词原形':'JJ',
    u'形容词最高级':'JJS',
    u'助动词':'MD',
    u'普通名词':'NN',
    u'专有名词':'NNP',
    u'指示代词':'PRD',
    u'疑问词':'WH',
    u'人称代词':'PRP',
    u'副词':'RB',
    u'小品词':'P',
    u'从属连词':'SC',
    u'符号': 'SYM',
    u'感叹词':'UH',
    u'动词':'VB',
    u'文本错误':'X',
    u'标点符号':'Z',
    u'反身代词':'PRF',
    u'不定代词':'PRI',
    u'关系代词':'PRL',
    u'主谓结构':'SP',
    u'动宾结构':'VO',
    u'介宾结构':'PO',
    u'不定数词':'ID',
}

# yingshe = {
#     '并列连词':'CC',
#     '基数词':'CD',
#     '序数词':'OD',
#     '限定词':'DT',
#     '形容词性物主代词':'DT',
#     '外来词':'FW',
#     '介词':'IN',
#     '形容词原形':'JJ',
#     '形容词最高级':'JJT',
#     '助动词':'MD',
#     '普通名词':'NN',
#     '专有名词':'NNP',
#     '指示代词':'PRD',
#     '疑问词':'WH',
#     '人称代词':'PRP',
#     '副词':'RB',
#     '小品词':'RP',
#     '从属连词':'SC',
#     '符号':'SYM',
#     '感叹词':'UH',
#     '语气词':'UH',
#     '及物动词':'VB',
#     '不及物动词':'VB',
#     '文本错误':'X',
#     '标点符号':'Z',
#     '反身代词':'PRF',
#     '不定代词':'PRI',
#     '关系代词':'PRL',
#     '主谓结构':'SP',
#     '动宾结构':'VO',
#     '介宾结构':'PO'
# }

data_ = {}
for i in data:
    sentence = data[i]
    temp_sententce = []
    # print sentence
    for word in sentence:
        try:
            # for chinese in yingshe:
            #     word = word.replace(chinese, yingshe[chinese])
            if word:
                # print word
                word_ = word.split(' ')[0]
                # print word_
                tag = word.split(' ')[1]
                if tag in yingshe:
                    tag = yingshe[tag]
                word = word_ + ' ' + tag
            temp_sententce.append(word)
        except:
            print 11111
            # raw_input()
            continue

    data_[i] = temp_sententce

f = open('huizong.txt','w')
print len(data_)
for i in data_:
    for j in data_[i]:
        f.write(j)
        f.write('\n')
f.close()
# length = len(data_)
# for i in data_:
#     print i


# for i in xrange(1,11):
#     f = open('data/' + str(i) + '.txt', 'w')
#     for j in xrange(i,length,10):
#         sentence = data_[str(j)]
#         for word in sentence:
#             f.write(word)
#             f.write('\n')
#     f.close()


