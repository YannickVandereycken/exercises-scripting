import sys
import re


for i in range(1,len(sys.argv)):
    with open(sys.argv[i],"r") as file:
        input = file.read()
    
    input = re.sub('#.*$', '', input, flags=re.MULTILINE)
        
    with open(sys.argv[i],"w") as file:
        file.write(input)
