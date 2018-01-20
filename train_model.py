# -*- coding:utf-8 -*-
import os

def train(filename):
    print filename
    os.system("crf_learn -c 3 template5 " + filename + " " + filename + ".model")

if __name__ == '__main__':

    for i in xrange(8,9):
        train('process3/' + str(i) + '.txt')