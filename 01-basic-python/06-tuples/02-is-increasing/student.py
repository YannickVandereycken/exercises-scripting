# Write your code here
def is_increasing(ns):
    for i in range(len(ns)-1):
        if(ns[i+1]<ns[i]):
            return False
    return True