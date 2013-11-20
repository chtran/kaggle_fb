#! /usr/bin/python
from HTMLParser import HTMLParser
from tagger.utils.stemming.porter2 import stem
import json
import sys
import re

class MLStripper(HTMLParser, object):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def word_map(w):
    if is_number(w):
        return '<Number>'
    return stem(w)

def  main(argv):
    filename = argv[1]
    f = open(filename)
    json_output = json.load(f)
    for row in json_output["data"]:
        s = MLStripper()
        html = row["text"]
        s.feed(html)
        stripped = s.get_data()
        p = re.compile("[=,()<>\n\t\[\]{}*&^%@!:;`\\/]")
        words = filter(lambda x: len(x)>3, p.split(stripped))
        mapped = map(word_map, words)
        row["text"] = " ".join(mapped)
    print json.dumps(json_output)


if __name__ == "__main__":
    main(sys.argv)


