from neuralnetwork import *
import numpy as np

situation_number = 1 # three patterns of situations
action_number = 1 #five patterns of robot's actions
eval_number = 2


if __name__ == '__main__':

    input_filename="input.csv"
    output_filename="output.csv"

    X = np.loadtxt(input_filename,delimiter=",")
    T = np.loadtxt(output_filename,delimiter=",")

    #X = numpy.array([[0, 0], [0.1, 1], [1, 0], [1, 1],[0.4,0.6]])
    #T = numpy.array([[1, 0], [0, 1], [0, 1], [1, 0],[0.2,0.3]])

    N = X.shape[0] # number of data

    input_size = X.shape[1]
    hidden_size = 2
    output_size = 2
    epsilon = 0.1
    mu = 0.9
    epoch = 10000

    test=np.zeros((11,input_size))
    nn = Neural(input_size, hidden_size, output_size)
    nn.train(X, T, epsilon, mu, epoch)
    #nn.error_graph()

    #action selection
    print("input situation from 0 to 10")
    wait_situation=int(raw_input())/10.0

    for action in range(0,10):
        wait_action=int(action)/10.0
        print([wait_situation,wait_action])
        test[action,:]=np.array([wait_situation,wait_action])

    C, Y=nn.predict(test)
    print(Y)
    print(max(Y[:,0]))
    print(Y[:,0].argmax())
