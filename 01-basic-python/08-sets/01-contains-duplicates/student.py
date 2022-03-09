# Write your code here
#def contains_duplicates(xs):
#   previous=set()
#    for x in xs:
#        temp = previous
#        previous.add(x)
#        if(len(temp)==len(previous)):
#            return True
#    return False

def contains_duplicates(xs):
    if(len(set(xs))<len(xs)):
        return True
    return False