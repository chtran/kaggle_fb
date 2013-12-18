import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from tagger.feature_selection.porter_tokenizer import PorterTokenizer
import json

class SaveDistribution:

    def __init__(self,
            tags_filename, vocab_filename,
            max_features=10000, tokenizer=PorterTokenizer()):
        tag_f = open(tags_filename)
        sorted_tags = json.load(tag_f)
        self.tags = set([tag_tuple[0] for tag_tuple in sorted_tags])
        self.save_directory = save_directory

        vocab_f = open(vocab_filename)
        self.vocab = json.load(vocab_f)

    def write_for_train(filename, save_directory):
        tokenizer = PorterTokenizer()
        csvfile = open(filename)
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')

        for i,row in enumerate(reader):
            row_text = row["text"]+" "+row["title"]
            vector = get_text_vector(row_text)
            row_tags = filter(lambda t: t in self.tags, row["tags"])

            for tag in row_tags:
                with open(save_directory+"/"+tag+".txt","a") as tag_file:
                    tagfile.write(vector+"\n")
            print "i=%d done" % i

    def write_for_test(filename, save_directory):
        tokenizer = PorterTokenizer()
        csvfile = open(filename)
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')

        f = open(save_directory+"/"+filename+".txt","a")
        for i,row in enumerate(reader):
            row_text = row["text"]+" "+row["title"]
            vector = get_text_vector(row_text)
            f.write(vector+"\n")
        f.close()

    def get_text_vector(text):
        word_ids = set([int(vocab[word]) for word in set(tokenizer.__call__(row_text)) if word in vocab])
        vector = [1 if i in word_ids else 0 for i in list(range(max_features))]
        return vector

