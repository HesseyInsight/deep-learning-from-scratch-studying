# https://brownbears.tistory.com/296
# 상위 폴더 내 파일 참조
# coding: uft-8

import os
import sys

print('currnet path: :', sys.path[0])
print('current working directory: ', sys.path[0])
sys.path.append('..')
# sys.path.append('c:\\Users\\Lee\\Documents\\steve-home\\05_Deep-Learning-from-Scratch-2-RNN.NLP')
# sys.path.append('c:\\Users\\Lee\\Documents\\steve-home\\05_Deep-Learning-from-Scratch-2-RNN.NLP\\dataset')
'''
for path in sys.path:
    print(path)

print(len(sys.path))
'''
print('sys.path:', sys.path)
# from dataset import spiral
# import dataset.spiral as spiral
# from matplotlib.pyplot import plt
from matplotlib import pyplot as plt

x, t = spiral.load_data()
print('x.shape: ', x.shape)
print('t.shape: ', t.shape)