# Write your code here
def target_sum(xs,target):
    for i in range(len(xs)):
        for j in range(len(xs)):
            if((xs[i]+xs[j])==target):
                return True
    return False