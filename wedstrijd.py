import re
def nummer_einde(string):
 return re.fullmatch('.*[0-9]$',string)