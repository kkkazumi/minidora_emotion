# -*- encoding: UTF-8 -*-
import numpy as np

from test import *

situation_number = 3 # three patterns of situations
action_number = 3 #five patterns of robot's actions
eval_number = 2

max_val=[10,1,5]#situation,action,facial expression
array_num=[situation_number,action_number,eval_number]

def input2NN(array,input_type):
    NN_array=np.zeros(array_num[int(input_type)])
    for i in range(size(array)):
        NN_array[i]=array[i]/max_val[input_type]
    return NN_array


if __name__ == "__main__":

    network = init_network()

    N_layer = [ situation_number+action_number,5,eval_number]
    teaching_num=3#TODO: write csv and count row num
    
    test_situation=np.zeros(int(array_num[0]))
    action_array=np.zeros(int(array_num[1]))
    test_input=np.zeros(int(array_num[0])+int(array_num[1]))

    input_filename="input.csv"
    output_filename="output.csv"

    NN = Neural_Network( N_layer,teaching_num )
    teach_i = np.loadtxt(input_filename,delimiter=",")
    teach_o = np.loadtxt(output_filename,delimiter=",")

    NN.input_date(teach_i,teach_o)
    NN.before_L("hoge")#TODO:cannot write weights in hoge.csv

    #if wait_key>situation_max:
    for cycle in range(situation_number):
        print("input number of situations")
        wait_key=int(raw_input())
        if wait_key>int(max_val[0]):
            message="input number 0 to %s, again" % max_val[0]
            print(message) 
            cycle=cycle-1 #back a cycle
        else:
            test_situation[cycle]=wait_key

    situation_num=input2NN(test_situation,0)
    print situation_num
    test_input=[0.1,0.2,0.5,0,0,1]
    NN.testforward(test_input)
    NN.before_L("hoge")#TODO:cannot write weights in hoge.csv
    test_input=[0.6,0.2,0.1,0,1,0]
    NN.testforward(test_input)


    for cycle in range(action_number):
        for i in range(array_num[1]):
            action_array[i]=0 #clean
        print cycle
        action_array[cycle]=1 #set
        #yosou
        test_input=hstack((situation_num,action_array))
        print(test_input)
        #NN.testforward(test_input)

        #eval_array[cycle]=


