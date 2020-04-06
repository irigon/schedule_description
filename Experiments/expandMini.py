from sys import argv

STR = 'x,y'
hours = '00'

with open (argv[1], 'r') as fd:
    lines = fd.readlines()
    for line in lines:
        if line.strip() == '':
            STR = 'y,x'
            continue
        parts = line.split()
        if len(parts) < 2:
            parts.insert(0, hours)
        hours, minutes = parts
        print('{}:{}:00,{}'.format(hours,minutes,STR))
