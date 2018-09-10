import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

import CorpusPreprocess

corpus=CorpusPreprocess.cnkiCorpus2List()