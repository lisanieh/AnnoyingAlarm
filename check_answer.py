if __name__ == "__main__":
    num = open("num.txt","r").readline()
    correct_answer = open("answers/a"+num+".txt",'r').readline().strip("\n")
    my_answer = open("my_ans.txt","r").readline().strip("\n")
    # print("correct ans = "+correct_answer)
    # print("my ans = "+my_answer)
    int p = 0
    for s in my_answer:
        for a in correct_answer:
            if s == a:
                p = p + 1
    if p > 0: 
        print(1)
        exit(1)
    else: 
        print(0)
        exit(0)

# return 1, if the answer is correct at 50% or more
