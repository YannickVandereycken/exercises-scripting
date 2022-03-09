# Write your code here
def from_lists(keys, values):
    result = {}
    for i in range(len(keys)):
        result.update({keys[i]:values[i]})

    return result