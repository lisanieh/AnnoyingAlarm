if __name__ == "__main__":
    num = open("num.txt","r").readline()
    correct_answer = open("answers/a"+num+".txt",'r').readline().strip("\n")
    my_answer = open("my_ans.txt","r").readline().strip("\n")
    # print("correct ans = "+correct_answer)
    # print("my ans = "+my_answer)
    try:

        if my_answer == correct_answer: 
            print(1)
            exit(1)
        else: 
            print(0)
            exit(0)
    except KeyboardInterrupt:
        print(1)
        exit(1)

# return 1, if the answer is correct at 50% or more
