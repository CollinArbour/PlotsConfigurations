#!/usr/bin/env python3

def parseOut(line):
    itr1 =  line.strip().split('ALL_')[-1]
    return itr1.split('.root')[0]

def parseIn(line):
    return line.split('/')[-2]

with open('./mComplete.txt','r') as fl:
    finished = fl.readlines()

with open('./orig_dirs.txt','r') as fl:
    orig = fl.readlines()

opStat =  {}
toKeep = []

for i,line in enumerate(finished):
    job = parseOut(line)
    opStat[job] = 'Completed'

for line in orig:
    job = parseIn(line)
    
    try:
        status = opStat[job]
    except:
        opStat[job] = 'FAILED'
        toKeep.append(line)
        print(f'{job} - Failed')

with open('toSubmit.txt','w') as fl:
    fl.writelines(toKeep)
