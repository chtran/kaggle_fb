from nltk.stem.porter import PorterStemmer
import json
from tagger.utils.scikit_feature import ScikitFeature
import sys

filename = sys.argv[1]
tag_filename = sys.argv[2]


sf = ScikitFeature(filename, tag_filename, max_features=10000, tokenizer=None)
ls = PorterStemmer()
origin_vocab = sf.tfidf.vocabulary_.keys()
stemmed_vocab = list(set(map(ls.stem, origin_vocab)))

print "Reduced from",len(origin_vocab),"to",len(stemmed_vocab)
