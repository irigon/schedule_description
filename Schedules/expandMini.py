from sys import argv
import argparse

hours = '00'

parser = argparse.ArgumentParser()
parser.add_argument("mini_file", help="file with the minimal description of a schedule")
parser.add_argument("ini", help="file with the minimal description of a schedule")
parser.add_argument("end", help="file with the minimal description of a schedule")
args = parser.parse_args()

print (args.ini, args.end)
str_normal   = args.ini + ',' + args.end
str_inverted = args.end + ',' + args.ini

#import pdb; pdb.set_trace()
STR = str_normal
with open (args.mini_file, 'r') as fd:
    lines = fd.readlines()
    for line in lines:
        if line.strip() == '':
            STR = str_inverted
            continue
        parts = line.split()
        if len(parts) < 2:
            parts.insert(0, hours)
        hours, minutes = parts
        print('{}:{}:00,{}'.format(hours,minutes,STR))
