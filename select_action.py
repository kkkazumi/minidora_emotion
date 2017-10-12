# -*- encoding: UTF-8 -*-
import numpy as np

from NN import *

situation_number = 3 # three patterns of situations
action_number = 5 #five patterns of robot's actions
eval_number = 1

max_val=[10,1,5]#situation,action,facial expression
array_num=[situation_number,action_number,eval_number]

def input2NN(array,input_type):
    NN_array=np.zeros(array_num[int(input_type)])
    for i in range(size(array)):
        NN_array[i]=array[i]/max_val[input_type]
    return NN_array


if __name__ == "__main__":

    N_layer = [ 3,5,1 ]
    teaching_num=2
    
    test_situation=np.zeros(int(array_num[0]))
    action_array=np.zeros(int(array_num[1]))

    NN = Neural_Network( N_layer,teaching_num )

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

    for cycle in range(1,action_number):
        for i in range(1,array_num[1]):
            action_array[i]=0 #clean
        print cycle
        action_array[cycle]=1 #set
        #yosou

        #eval_array[cycle]=


