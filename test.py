import jieba

jieba.set_dictionary('dict.txt.big')

text = '我來到北京清華大學'
text = "我想查詢實驗室有關Computer Vision的資訊"
print('預設:', '|'.join(jieba.cut(text, cut_all=False, HMM=True)))