# Write your code here
def format_time(h,m,s):
    h=str(h).zfill(2)
    m=str(m).zfill(2)
    s=str(s).zfill(2)
    return f'{h}:{m}:{s}'
