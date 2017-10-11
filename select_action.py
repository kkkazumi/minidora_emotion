# -*- encoding: UTF-8 -*-



if __name__ == "__main__":

    situation_max=10

    print("input number of situations")
    wait_key=raw_input()
    #if wait_key>situation_max:
    #    message="input number 0 to %s, again" % situation_max
    #    print(message) 
    if wait_key<situation_max:
        situation_num=wait_key

    for test_action in range(1, 5):
        action_num=test_action

