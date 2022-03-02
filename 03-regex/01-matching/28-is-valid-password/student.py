# Write your code here
import re
def is_valid_password(string):
    return re.search('.{8,}|',string)