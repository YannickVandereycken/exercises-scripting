# Write your code here
def median(xs):
    sortedxs = sorted(xs)
    middle=len(sortedxs)//2
    if (len(sortedxs)%2)==0:
        return (sortedxs[middle-1]+sortedxs[middle])/2
    return sortedxs[middle]