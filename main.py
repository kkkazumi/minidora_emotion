from neuralnetwork import *
import numpy as np
import csv

situation_number = 1 # three patterns of situations
action_number = 1 #five patterns of robot's actions
eval_number = 2


if __name__ == '__main__':

    input_filename="input.csv"
    output_filename="output.csv"

    hidden_size = 2
    output_size = 2
    epsilon = 0.1
    mu = 0.9
    epoch = 10000

    wait_situation=0

    for i in range(1,10):

        print(i)
        X = np.loadtxt(input_filename,delimiter=",")
        T = np.loadtxt(output_filename,delimiter=",")

        N = X.shape[0] # number of data

        input_size = X.shape[1]
        test=np.zeros((11,input_size))
        nn = Neural(input_size, hidden_size, output_size)
        nn.train(X, T, epsilon, mu, epoch)

        for action in range(0,10):
            wait_action=int(action)/10.0
            #print([wait_situation,wait_action])
            test[action,:]=np.array([wait_situation,wait_action])

        C, Y=nn.predict(test)
        best=Y[:,0].argmax()
        print("selected: ",test[best,:])

        #action!#TODO
        


        print("input your evaluation to the robot's behavior (0-10)")
        evaluation=int(raw_input())/10.0
        #evaluation!#TODO:facial expression and so on

        #add supervisor data
        f=open(input_filename,'ab')
        r=open(output_filename,'ab')
        csvWriterf=csv.writer(f)
        csvWriterr=csv.writer(r)
        csvWriterf.writerows([test[best,:]])
        csvWriterr.writerows([[evaluation,0]])
        f.close()
        r.close()

        wait_situation=test[best,1]

