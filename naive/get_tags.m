% tag_words =  P(word|tag) [KxD]
% tags = P(tag) [Kx1]
% test_vector = NxD
function get_tags(tag_words, tags, test_vector)
    log_tag_words = log(tag_words);
    log_tags = log(tags)
    N = size(test_vector, 1);
    question_tags = log(test_vector*tag_words) + repmat(log(tags)',N,1);
end