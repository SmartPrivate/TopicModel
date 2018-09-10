import logging
from Env import Const

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

const = Const()
wordlist = []
for line in open(str(const.LDA_result_file_name), 'r'):
    for word in line.replace(' ', '').replace('"', '').split('+'):
        wordlist.append(word.split('*'))
    wordlist.pop()
file = open('/Users/alexma/Documents/showResults.txt', 'w', encoding='UTF-8')
for line in wordlist:
    file.write(line[0] + ' ' + line[1] + '\n')
print(wordlist)
