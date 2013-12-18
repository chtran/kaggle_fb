from tagger.naive.save_distribution import SaveDistribution
import sys

filename = sys.argv[1]
tags_filename = sys.argv[2]
vocab_filename = sys.argv[3]

sd = SaveDistribution(save_directory='data', filename, tags_filename, vocab_filename)
