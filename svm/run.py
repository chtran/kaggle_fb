from subprocess import call
for i in range(0,21):
    input_name = "../data/test/test_"+str(i)+".json"
    output_name = "../results/5percent/0_100/test_"+str(i)+".csv"
    call(["python","scikit_svm.py","get_tags",input_name,output_name])

