#! /usr/bin/python
import json
import sys
import numpy as np
from scipy import io
from stemming.porter2 import stem
# N=num words, T=num tags
# tag_word_d: TxN 
# tag_d: Tx1
# word_d: Nx1

E = 1e-10
def get_tags(text, ids, distributions):
    tag_to_id = ids["tag_to_id"]
    word_to_id = ids["word_to_id"]
    id_to_tag = ids["id_to_tag"]
    id_to_word = ids["id_to_word"]
    tag_word_d = distributions["tag_word_d"]
    tag_d = distributions["tag_d"]
    word_d = distributions["word_d"]
    tag_d = (tag_d + E)/np.sum(tag_d)

    tag_word_d = tag_word_d + E
    row_sums = np.sum(tag_word_d, axis=1)
    tag_word_d = tag_word_d/row_sums[:, np.newaxis]


    words = map(lambda w: stem(w.lower()), text.split())
    word_ids = [word_to_id[word] for word in words if word in word_to_id]
    n_tags = len(tag_to_id)
    n_words = len(word_to_id)
    tag_scores = np.zeros(n_tags)
    for j in range(n_tags):
        tag_scores[j] = np.sum(np.log(tag_word_d[j, word_ids])) + len(word_ids)*np.log(tag_d[j])
        #tag_scores[j] = np.sum(tag_word_d[j, word_ids])
    sorted_tag_ids = np.argsort(tag_scores)
    return [id_to_tag[str(tag_id)] for tag_id in sorted_tag_ids[-5:]]

def test(filename, ids, distributions):
    f = open(filename)
    json_output = json.load(f)
    correct = 0
    total_guess = 0
    total_tags = 0
    for row in json_output["data"]:
        tags = get_tags(row["text"], ids, distributions)
        total_guess += len(tags)
        this_correct = len(filter(lambda t: t.lower() in row["tags"], tags))
        correct += len(filter(lambda t: t.lower() in row["tags"], tags))
        total_tags += len(row["tags"])
    p = (float(correct)/total_guess)
    r = (float(correct)/total_tags)
    print "Precision: %f %%" % (p*100)
    print "Recall: %f %%" % (r*100)
    print "Score: %f" % (2*p*r/(p+r))

if __name__ == "__main__":
    feature_folder = sys.argv[1]
    filename = sys.argv[2]
    distributions = io.loadmat(feature_folder+'distributions.mat')
    id_file = open(feature_folder+'ids.json')
    ids = json.load(id_file)

    test(filename, ids, distributions)

    
