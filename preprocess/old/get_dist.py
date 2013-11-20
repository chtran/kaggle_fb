def get_dist(filename):
    sf = ScikitFeature(filename)
    training_text = sf.training_text.todense() # N_question x N_word
    training_labels = sf.training_labels # N_question x N_tags

    tag_word_dist = np.dot(training_labels.T, training_text) # N_tags x N_word
    tag_word_dist = tag_word_dist/np.sum(tag_word_dist, axis=1)

    tag_dist = np.sum(training_labels, axis=0)
    tag_dist = tag_dist/np.sum(tag_dist)


if __name__ == "__main__":
    filename = sys.argv[1]
    #tag_to_id, word_to_id =  build_dict(filename)
    tag_word_d, tag_d, word_d = get_dist(filename)
