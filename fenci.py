import logging
from Env import Const
from collections import defaultdict
import jieba
import CorpusPreprocess

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)
const=Const()

def getWeChatFile(filename):
    text = []
    for line in open(filename):
        text.append(line)
    return text


def getCNKICorpus():
    documents = []
    result = open('/Users/alexma/Desktop/tempresult', 'w')
    for document in getWeChatFile('/Users/alexma/Desktop/4'):
        jieba.load_userdict(const.user_dic)
        text = jieba.lcut(document, cut_all=False)
        texts = []
        for word in text:
            if word not in CorpusPreprocess.chineseStopWordList2List():
                if word in word:
                    texts.append(word)
                    result.write(word)
        documents.append(texts)
    frequency = defaultdict(int)
    for text in documents:
        for word in text:
            frequency[word] += 1
    sorteddic = sorted(frequency.items(), key=lambda e: e[1], reverse=True)
    dicwrite = open(str('/Users/alexma/Desktop/result4'), 'w')
    for item in sorteddic:
            dicwrite.write(item[0] + '\t' + str(item[1]) + '\n')

    return documents


print(getCNKICorpus())
