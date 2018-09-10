import logging
from Env import Const

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

from gensim import corpora, models, similarities
import CorpusPreprocess

const = Const()


# region 功能函数
def writeResult2File(topicList):
    topics = []
    for topic in topicList:
        topics.append(str(topic[1]))
    f = open(const.LDA_result_file_name, 'w')
    for topic in topics:
        f.write(topic + '+')
    f.close()


# endregion 功能函数

documents = CorpusPreprocess.getCNKICorpus()  # 文本预处理
wordDictionary = corpora.Dictionary(documents)  # 文本向量转换
corpus = [wordDictionary.doc2bow(document) for document in documents]  # 语料转换
ldaTopic = models.LdaModel(corpus, id2word=wordDictionary, num_topics=10)  # 调用主题模型LDA函数
topicList = ldaTopic.print_topics(10)  # 获取排名前10高频主题进行分析
writeResult2File(topicList)  # 将结果写入文件
