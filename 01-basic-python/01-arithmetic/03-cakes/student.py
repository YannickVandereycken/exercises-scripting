# Write your code here
def cakes(eggs, butter, flour):
    maxeggs=eggs//5
    maxbutter=butter//250
    maxflour=flour//5
    return min(maxbutter,maxeggs,maxflour)