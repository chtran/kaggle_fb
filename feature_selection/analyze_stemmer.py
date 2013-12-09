import json
from tagger.utils.scikit_feature import ScikitFeature
import sys

filename = sys.argv[1]
tag_filename = sys.argv[2]


sf = ScikitFeature(filename, tag_filename, max_features=5000)
vocab = sf.tfidf.vocabulary_
vocab = {k:int(vocab[k]) for k in vocab}

print json.dumps(vocab)
