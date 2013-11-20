#! /usr/bin/python
from sys import stdin
import sys

def main(argv):
    dict = {}
    for line in stdin:
        fields = line.split(",")
        id = fields[0]
        tags = fields[1].split()
        if id not in dict:
            dict[id] = []
        dict[id].extend(tags)
    for id in dict:
        print id+","+" ".join(dict[id])
