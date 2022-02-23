# Write your code here
def rotate(xs,n):
    if n>(len(xs)-1):
        return None
    return xs[n:] + xs[:n]