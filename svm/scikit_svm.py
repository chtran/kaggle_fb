from nltk.stem.porter import PorterStemmer
from tagger.utils.scikit_feature import ScikitFeature
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
import sys
import pickle
import csv
import numpy as np

class ScikitSVM:
    def __init__(self, train_file, tags_file, tag_start, tag_end):
        self.sf = ScikitFeature(train_file, tags_file, tag_start, tag_end, max_features=10000)
        print "done getting features"
        self.classifier = OneVsRestClassifier(LinearSVC(C=32,random_state=0), n_jobs=1)
        self.classifier.fit(self.sf.training_text, self.sf.training_labels_tuple)
        print "done fitting"

    def predict(self, text):
        text_vector = self.sf.get_text_vector(text)
        labels = self.classifier.predict(text_vector)
        return self.sf.get_labels(labels)

    def test(self, test_file):
        test_matrix = self.sf.get_file_text(test_file)
        predicted_labels = self.classifier.predict(test_matrix)
        predicted_label_names = [self.sf.get_labels_from_id(label_ids) for label_ids in predicted_labels]
        true_labels = self.sf.get_file_labels(test_file)
        N_question = len(predicted_labels)
        N_true_tags = 0.0
        N_predict_tags = 0.0
        N_correct = 0.0
        F1 = []
        for i in range(N_question):
            N_true_tags += len(true_labels[i])
            N_predict_tags += len(predicted_labels[i])
            this_correct = 0.
            for predict_label_id in predicted_labels[i]:
                if (predict_label_id in true_labels[i]):
                    this_correct += 1
            N_correct += this_correct
            if this_correct == 0:
                F1.append(0)
            else:
                p = this_correct / len(predicted_labels[i])
                r = this_correct / len(true_labels[i])
                F1.append(2*p*r/(p+r))
        print N_correct,N_predict_tags,N_true_tags
        p= N_correct / N_predict_tags
        r= N_correct / N_true_tags
        print "Precision: %f %%" % (p*100)
        print "Recall: %f %%" % (r*100)
        print "Mean F1: %f" % (np.average(F1))

    def get_tags(self, test_file, output_file):
        print "Getting tags for "+test_file
        new_csv = open(output_file, 'w')
        writer = csv.writer(new_csv, delimiter=',', quotechar='"')
        test_matrix = self.sf.get_file_text(test_file)
        predicted_labels = self.classifier.predict(test_matrix)
        predicted_label_names = [self.sf.get_labels_from_id(label_ids) for label_ids in predicted_labels]
        ids = self.sf.get_file_ids(test_file)
        for i,id in enumerate(ids):
            tags = " ".join(predicted_label_names[i])
            writer.writerow([id, tags])
        new_csv.close()
        print "Done."

if __name__ == "__main__":
    command = sys.argv[1]

    if command == "train":
        input_file = sys.argv[2]
        tags_file = sys.argv[3]
        tag_start = 0
        tag_end = 25
        if (len(sys.argv)>4):
            tag_start = int(sys.argv[4])
            tag_end = int(sys.argv[5])
        svm = ScikitSVM(input_file, tags_file, tag_start, tag_end)
        with open('scikit_svm.dat', 'wb') as output:
            pickle.dump(svm, output, pickle.HIGHEST_PROTOCOL)
    elif command == "test":
        test_file = sys.argv[2]
        with open('scikit_svm.dat', 'rb') as input:
            svm = pickle.load(input)
        svm.test(test_file)
    elif command == "get_tags":
        test_file = sys.argv[2]
        output_file = sys.argv[3]
        with open('scikit_svm.dat', 'rb') as input:
            svm = pickle.load(input)
        svm.get_tags(test_file, output_file)
    else:
        print "scikit_svm [train] [input_file] [tags_file] ([tag_start] [tag_end])"
        print "scikit_svm [test] [test_file]"
        print "scikit_svm [get_tags] [test_file] [output_file]"

