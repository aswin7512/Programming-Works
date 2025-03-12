from jovian.pythondsa import evaluate_test_case
test={
    "input":{"list":[5,3,6,8,9]},
    "output":[6,4,7,9,10]
}
def inc1(list):
    for i in range(len(list)):
        list[i]+=1
    return list
evaluate_test_case(inc1,test)
