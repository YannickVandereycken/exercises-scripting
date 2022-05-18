import re

with open("input.txt") as input:
    with open("output.txt","w") as output:
        for line in input:
            line =line.strip()
            match = re.fullmatch(r"(.*:)(-*[0-9]+)/(-*[0-9]+) (.*)",line)
            print(match.group(4))
            one = int(match.group(2))
            two = int(match.group(3))
            for str in match.group(4):
                if str == "+":
                    one+=1
                    two+=1
                if str == "-":
                    one-=1

            # if one<0:
            #     one=0
            output.write(f'{match.group(1)}{one}/{two}\n')
            print(one,two)

