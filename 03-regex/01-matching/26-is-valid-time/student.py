# Write your code here
import re
def is_valid_time(string):
    return re.fullmatch('[0-9][0-9]:[0-9][0-9]:[0-9][0-9](\\.[0-9][0-9][0-9])?',string)