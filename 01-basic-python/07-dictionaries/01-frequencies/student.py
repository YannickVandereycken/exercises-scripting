# Write your code here
def frequencies(xs):
    dict={}

    for x in xs:
        if x in dict:
            i=dict.get(x)+1
            dict.update({x:i})
        else:
            dict.update({x:1})
    return dict