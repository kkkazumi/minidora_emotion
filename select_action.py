# -*- encoding: UTF-8 -*-




if __name__ == "__main__":

    situation_number = 3 # three patterns of situations
    action_number = 5 #five patterns of robot's actions


    N_layer = [ 3,5,1 ]

    NN = Neural_Network( N_layer,teaching_num )

    print("input number of situations")
    wait_key=raw_input()
    #if wait_key>situation_max:
    #    message="input number 0 to %s, again" % situation_max
    #    print(message) 
    situation_num=wait_key

    for test_action in range(1, 5):

        action_num=test_action

