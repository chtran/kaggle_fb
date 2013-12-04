import sys
from subprocess import call
import os
from os.path import isdir
if !isdir("../results/5percent/"+range):
    call(["mkdir", "../results/5percent/"+range)
range = sys.argv[1]
for i in range(0,21):
    input_name = "../data/test/test_"+str(i)+".json"
    output_name = "../results/5percent/"+range+"/test_"+str(i)+".csv"
    call(["python","scikit_svm.py","get_tags",input_name,output_name])

