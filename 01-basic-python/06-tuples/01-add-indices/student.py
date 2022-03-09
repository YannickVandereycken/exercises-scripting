# Write your code here
def add_indices(xs):
    ys =[]
    for x in range(len(xs)):
        ys.append(x)
    return list(zip(ys,xs))