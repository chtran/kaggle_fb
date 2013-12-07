from tagger.utils.scikit_feature import ScikitFeature
from tagger.feature_selection.porter_tokenizer import PorterTokenizer

sf = ScikitFeature('../data/1percent.json', '../data/sorted_tags.json', tokenizer=PorterTokenizer())
