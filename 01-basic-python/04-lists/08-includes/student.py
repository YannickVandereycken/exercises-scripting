# Write your code here
import re


def includes(xs,ys):
    for y in ys:
        if y not in xs:
            return False
    return True
    