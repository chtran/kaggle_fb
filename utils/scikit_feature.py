import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelBinarizer
import json

class ScikitFeature:

    def __init__(self, filename, tags_filename, tag_start=0, tag_end=100, max_features=5000):
        f = open(filename)
        json_output = json.load(f)
        tag_f = open(tags_filename)
        sorted_tags = json.load(tag_f)
        self.tags = set([tag_tuple[0] for tag_tuple in sorted_tags[tag_start:tag_end]])

        text_data = []
        label_data = []
        for row in json_output["data"]:
            text_data.append(row["text"])
            row_tags = filter(lambda t: t in self.tags, row["tags"])
            label_data.append(row_tags)
        print "Loaded label and text data"
        # Process text data
        #self.count_vectorizer = CountVectorizer(max_features=max_features, stop_words='english')
        #sparse_matrix = self.count_vectorizer.fit_transform(text_data)
        self.tfidf = TfidfVectorizer(max_features=max_features, stop_words="english", norm="l2")
        self.training_text = self.tfidf.fit_transform(text_data)
        #self.training_text = self.tfidf.transform(sparse_matrix)
        print "Computed text features"

        # Process label data

        #label_data = [row["tags"] for row in json_output["data"]]
        assert len(text_data)==len(label_data)
        self.label_binarizer = LabelBinarizer()
        self.training_labels = self.label_binarizer.fit_transform(label_data)
        self.training_labels_tuple = tuple([np.nonzero(row)[0].tolist() for row in self.training_labels])
        print "Dimension = " + str(max_features)
        print "N = "+ str(len(label_data))
        print "Num classes = " + str(len(self.tags))

    # Get list of label names from list of label_ids
    def get_labels_from_id(self, label_ids):
        return [self.label_binarizer.classes_[label_id] for label_id in label_ids]

    def get_label_vector(self, labels):
        return self.label_binarizer.transform([labels])[0]

    def get_text_vector(self, text):
        return self.tfidf.transform(text)

    def get_file_text(self, filename):
        f = open(filename)
        json_output = json.load(f)
        text_data = [row["text"] for row in json_output["data"]]
        text_matrix = self.tfidf.transform(text_data)
        return text_matrix

    def get_file_labels(self, filename):
        f = open(filename)
        json_output = json.load(f)
        label_data = [filter(lambda x: x in self.tags, row["tags"]) for row in json_output["data"]]
        file_labels = self.label_binarizer.transform(label_data)
        file_labels_tuple = tuple([np.nonzero(row)[0].tolist() for row in file_labels])
        return file_labels_tuple

    def get_file_ids(self, filename):
        f = open(filename)
        json_output = json.load(f)
        ids = [row['id'] for row in json_output["data"]]
        return ids
