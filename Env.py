import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


class Const(object):
    __CNKI_FILE_NAME = '/Users/alexma/Documents/DataSource/wenjian.txt'
    __CHINESE_STOP_WORD_LIST_FILE_NAME = '/Users/alexma/Documents/DataSource/ChineseStopWords.txt'
    __ENGLISH_STOP_WORD_LIST_FILE_NAME = '/Users/alexma/Documents/DataSource/EnglishStopWords.txt'
    __WOS_FILE_NAME = '/Users/alexma/Documents/DataSource/WOS.txt'
    __USER_DIC = '/Users/alexma/Documents/DataSource/UserDic.txt'
    __LDA_RESULT_FILE_NAME = '/Users/alexma/Documents/Result/LDAResult.txt'
    __DIC_RESULT_FILE_NAME='/Users/alexma/Documents/Result/dicResult.txt'
    __HIGH_FREQUENCY_KEYWORD_FILE_NAME='/Users/alexma/Documents/Result/highFrequencyKeywordResult.txt'

    @property
    def cnki_file_name(self):
        return self.__CNKI_FILE_NAME

    @property
    def chinese_stop_word_list_file_name(self):
        return self.__CHINESE_STOP_WORD_LIST_FILE_NAME

    @property
    def english_stop_word_list_file_name(self):
        return self.__ENGLISH_STOP_WORD_LIST_FILE_NAME

    @property
    def wos_file_name(self):
        return self.__WOS_FILE_NAME

    @property
    def user_dic(self):
        return self.__USER_DIC

    @property
    def LDA_result_file_name(self):
        return self.__LDA_RESULT_FILE_NAME

    @property
    def dic_result_file_name(self):
        return self.__DIC_RESULT_FILE_NAME

    @property
    def high_frequency_keyword_file_name(self):
        return self.__HIGH_FREQUENCY_KEYWORD_FILE_NAME
