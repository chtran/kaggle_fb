#! /usr/bin/python
import json
import sys
import numpy as np
from scipy import io
from tagger.utils.process import get_vector

EPSILON = 0

def get_dist(filename):
    tag_to_id, word_to_id = build_dict(filename)
    f = open(filename)
    json_output = json.load(f)
    n_tags = len(tag_to_id)
    n_words = len(word_to_id)
    n_questions = len(json_output["data"])
    tag_word_d = np.ones((n_tags, n_words))*EPSILON
    tag_d = np.zeros(n_tags)
    word_d = np.zeros(n_words)
    document_matrix = np.zeros((n_questions, n_words))
    labels = np.zeros((n_questions, n_tags))
    
    for qid, row in enumerate(json_output["data"]):
        text = row["text"]
        tag_ids = [tag_to_id[tag] for tag in row["tags"] if tag in tag_to_id]
        if len(tag_ids) == 0: continue
        tag_d[tag_ids] += 1
        vector = get_vector(text, word_to_id)
        document_matrix[qid, :] = vector.T
        labels[qid, tag_ids] = 1
        
        words = map(lambda w: w.lower(), text.split())
        for word in words:
            if word in word_to_id:
                word_id = word_to_id[word]
                word_d[word_id] += 1
                tag_word_d[tag_ids, word_id] += 1.0/len(tag_ids)
    tag_d = tag_d/sum(tag_d)
    word_d = word_d/sum(word_d)
    row_sums = tag_word_d.sum(axis=1)
    tag_word_d = tag_word_d/row_sums[:, np.newaxis]
    io.savemat('distributions.mat', mdict={
        'tag_word_d': tag_word_d,
        'tag_d': tag_d,
        'word_d': word_d
    })
    good_qids = [qid for qid in range(0,n_questions) if np.sum(labels[qid,:]) > 0]
    document_matrix = document_matrix[good_qids,:]
    labels = labels[good_qids, :]
    io.savemat('features.mat', mdict={
        'document_matrix': document_matrix,
        'labels': labels
    })

    id_to_tag = {tag_id: tag for tag,tag_id in tag_to_id.items()}
    id_to_word = {word_id: word for word,word_id in word_to_id.items()}
    ids = {
            'tag_to_id': tag_to_id, 
            'word_to_id': word_to_id,
            'id_to_tag': id_to_tag,
            'id_to_word': id_to_word
            }
    f = open('ids.json', 'w')
    f.write(json.dumps(ids))
    f.close()
    return tag_word_d, tag_d, word_d

def  build_dict(filename):
    f = open(filename)
    json_output = json.load(f)
    word_counts = {}
    tag_counts = {}
    for row in json_output["data"]:
        #1. Get all tags
        for tag in row["tags"]:
            if tag in tag_counts: tag_counts[tag]+=1
            else: tag_counts[tag]=1
        #2. Get all words
        text = row["text"]
        words = map(lambda w: w.lower(), text.split())
        for word in words:
            if word in word_counts: word_counts[word]+=1
            else: word_counts[word]=1
    threshold = np.sort(word_counts.values())[-35]
    print 'count threshold is:', threshold
    good_words = [word for word in word_counts if (word_counts[word] > 10 and word_counts[word] < threshold)]
    good_tags = [tag for tag in tag_counts if tag_counts[tag] > 1]
    word_to_id = {word:id for id,word in enumerate(good_words)}
    tag_to_id = {tag:id for id,tag in enumerate(good_tags)}
    return tag_to_id, word_to_id

if __name__ == "__main__":
    filename = sys.argv[1]
    #tag_to_id, word_to_id =  build_dict(filename)
    tag_word_d, tag_d, word_d = get_dist(filename)
