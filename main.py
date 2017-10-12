from neuralnetwork import *
import numpy as np

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

    nn = Neural(input_size, hidden_size, output_size)
    nn.train(X, T, epsilon, mu, epoch)
    #nn.error_graph()

    C, Y = nn.predict(X)

    for i in range(N):
        x = X[i, :]
        y = Y[i, :]
        c = C[i]

        print x
        print y
        #print c
        print ""
