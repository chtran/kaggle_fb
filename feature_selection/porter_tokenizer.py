from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
class PorterTokenizer(object):
    def __init__(self):
        self.ls = PorterStemmer()
        self.rx = RegexpTokenizer(r"(?u)\b\w\w+\b")
        self.sw = stopwords.words('english')

    def isNumber(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def qualify(self, word):
        return len(word)>2 and not self.isNumber(word) and word not in self.sw

    def __call__(self, doc):
        return [self.ls.stem(word.lower()) for word in self.rx.tokenize(doc) if self.qualify(word.lower())]
