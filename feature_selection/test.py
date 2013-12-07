from tagger.utils.scikit_feature import ScikitFeature
from tagger.feature_selection.lancaster_tokenizer import LancasterTokenizer

sf = ScikitFeature('../data/1percent.json', '../data/sorted_tags.json', tokenizer=LancasterTokenizer())
