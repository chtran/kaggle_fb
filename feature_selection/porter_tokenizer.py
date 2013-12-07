from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
class PorterTokenizer(object):
    def __init__(self):
        self.ls = PorterStemmer()
        self.rx = RegexpTokenizer(r"(?u)\b\w\w+\b")

    def isNumber(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def __call__(self, doc):
        return [self.ls.stem(t) for t in self.rx.tokenize(doc) if not self.isNumber(t)]
