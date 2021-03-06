import sys
sys.path.append('..')
import numpy as np
# from common.util import most_similar, create_co_matrix, ppmi
from common.util import preprocess, create_co_matrix, ppmi, most_similar

# python with 파일 읽기
# https://wikidocs.net/26

# with open(r"C:\Users\Lee\Documents\steve-home\05_Deep-Learning-from-Scratch-2-RNN.NLP\dataset\kakao_chat.txt", "r", encoding='utf-8') as f:
#     print(f.read())


text = 'I love seongnam-city in Korea.'
text = text.lower()
text = text.replace('.', ' .')
text = text.split(' ')

print('text: ', text)
print('type(text): ', type(text))  # python split(): split a string into a list    
print('indexing-from 2 to all: ', text[2:])

corpora = np.array([1, 2, 3])
corpora = corpora.reshape(1, -1)
print('corpora.shape: ', corpora.shape)