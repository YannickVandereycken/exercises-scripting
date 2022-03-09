# Write your code here
def remove_duplicates(xs):
    nodupes=[]
    previous=set()
    for x in xs:
        if(x not in previous):
            previous.add(x)
            nodupes.append(x)
        
    return nodupes