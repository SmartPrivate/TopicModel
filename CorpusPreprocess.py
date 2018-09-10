import logging
import jieba
from Env import Const
from collections import defaultdict

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

const = Const()


def getCNKICorpus():
    documents = []
    for document in cnkiCorpus2List():
        jieba.load_userdict(const.user_dic)
        text = jieba.lcut(document, cut_all=False)
        texts = []
        for word in text:
            if word not in chineseStopWordList2List():
                texts.append(word)
        documents.append(texts)
    frequency = defaultdict(int)
    for text in documents:
        for word in text:
            frequency[word] += 1
    sorteddic = sorted(frequency.items(), key=lambda e: e[1], reverse=True)
    dicwrite = open(str(const.dic_result_file_name), 'w')
    for item in sorteddic:
        if item[1] > 50:
            dicwrite.write(item[0] + '\t' + str(item[1]) + '\n')
    return [[word for word in text if frequency[word] > 1] for text in documents]


def getWOSCorpus():
    documents = []
    frequency = defaultdict(int)
    for document in wOSCorpus2List():
        texts = []
        for word in document:
            if word not in englishStopWordList2List():
                texts.append(word)
                frequency[word] += 1
        documents.append(texts)
    sortedFrequency = sorted(frequency.items(), key=lambda e: e[1], reverse=True)
    return [[word for word in text if frequency[word] > 1] for text in documents]


def chineseStopWordList2List():
    texts = []
    for line in open(const.chinese_stop_word_list_file_name):
        texts.append(line.rstrip('\n'))
    return texts


def cnkiCorpus2List():
    texts = []
    keywords = []
    for line in open(const.cnki_file_name):
        # if line.startswith('Title'):
        #   texts.append(line.strip()[11:])
        if line.startswith('Keyword'):
            keywords.append(line.replace(';;',';').replace(',',';')[14:].split(';'))
        if line.startswith('Summary'):
            texts.append(line.replace(',', '').replace(' ', '').replace('\n','')[13:])
        else:
            continue
    frequency = defaultdict(int)
    for keyword in keywords:
        for word in keyword:
            frequency[word] += 1
    sorteddic = sorted(frequency.items(), key=lambda e: e[1], reverse=True)
    dicwrite = open(str(const.high_frequency_keyword_file_name), 'w')
    for item in sorteddic:
        dicwrite.write(item[0] + '\t' + str(item[1]) + '\n')
    return texts


def wOSCorpus2List():
    documents = []
    for line in open(const.wos_file_name):
        texts = line.split('\t')
        for text in texts:
            if text == '':
                continue
            if text.find(';'):
                text = text.replace(';', ' ')
            documents.append(text.lower().split())
    return documents


def englishStopWordList2List():
    texts = []
    for line in open(const.english_stop_word_list_file_name):
        texts.append(line.rstrip('\n'))
    return texts
