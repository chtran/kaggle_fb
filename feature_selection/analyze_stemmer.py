from nltk.stem.porter import PorterStemmer
import json
from tagger.utils.scikit_feature import ScikitFeature
import sys

filename = sys.argv[1]
tag_filename = sys.argv[2]


sf = ScikitFeature(filename, tag_filename, max_features=10000)
ls = PorterStemmer()
vocab = sf.tfidf.vocabulary_.keys()

print json.dumps(sorted(vocab))
