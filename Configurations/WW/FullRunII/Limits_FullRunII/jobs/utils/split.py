#!/usr/bin/env python3

import json
import argparse
parser = argparse.ArgumentParser()

mops = ['cW','cHDD','cHWB','cHl3','cHq3','cll1']

parser.add_argument('-mdl','--model',dest='model',default='float',help='First operator to compare')
parser.add_argument('-w','--wkspc',dest='workspace',default='allOps_model.root')
parser.add_argument('-op1','--op1',dest='op1',help='First operator to compare')
parser.add_argument('-op2','--op2',dest='op2',default=None,help='Second operator to compare')
parser.add_argument('-pts','--points',type=int,dest='pts',help='Toal number points to perform scan over')
parser.add_argument('-ppj','--pointsPerJob',type=int,dest='ppj',help='Submit jobs that only look at these many points')

args = parser.parse_args()

model = args.model
workspace = args.workspace
op1 = args.op1
op2 = args.op2

if op1 not in mops:
    print(f'{op1} is not a valid opion\nPlease choose amongst: {print(mops)}')
    exit()

if op2:
    if op2 not in mops:
        print(f'{op2} is not a valid opion\nPlease choose amongst: {print(mops)}')
        exit()
else:
    print('Only 1 Operator argument, performing 1D scan')
    

pts = args.pts
ppj = args.ppj

njobs = int(pts / ppj)

othops = [f'k_{op}=0' for op in mops if op!=op1 and op!=op2]
pothops = ','.join(othops)

if model.lower() == 'float':
    print('Using "FLOAT" mode')
    frz_ops = 'FLOAT'
elif model.lower() == 'fixed':
    print('Using "FIXED" mode')
    frz_ops = ''.join(pothops.split('=0'))
else:
    print('Model not supported')
    quit()


if (njobs * ppj) != pts:
    print('not an even split of points between jobs')
    exit()
elif op2:
    print(f'\nRequesting scan between {op1} and {op2}, with {pts} points, ')
    print(f'Where the WCs ({othops}) are set to {model}')
    print(f'At requested {ppj} points per job, there will be a total of {njobs} jobs submitted\n')
else:
    print(f'\nRequesting 1D scan of {op1}, with {pts} points, ')
    print(f'Where the WCs ({othops}) are set to {model}')
    print(f'At requested {ppj} points per job, there will be a total of {njobs} jobs submitted\n')



refVals = json.load(open('./utils/refVals.json'))
rng1 = refVals['Ranges'][op1]
if op2:
    rng2 = refVals['Ranges'][op2]
    tosub = open(f'./{op1}_{op2}_sendCMDs.sub','w')
else:
    tosub = open(f'./{op1}_1D_sendCMDs.sub','w')

tosub.write('universe    = vanilla\n')

if op2:
    tosub.write('executable  = src/runSplit.sh\n')
else:
    tosub.write('executable  = src/1D_runSplit.sh\n')

tosub.write('arguments   = $(myargs)\n')


#Outputs
tosub.write(f'output      = dev/null\n')

if op2:
    #tosub.write(f'output      = ./log/{op1}_{op2}_{model}_limits.$(ClusterId).$(ProcId).out\n')
    tosub.write(f'error       = ./log/{op1}_{op2}_{model}_limits.$(ClusterId).$(ProcId).err\n')
    #tosub.write(f'log         = ./log/{op1}_{op2}_{model}_limits.$(ClusterId).log\n')
else:
    #tosub.write(f'output      = ./log/{op1}_{model}_limits.$(ClusterId).$(ProcId).out\n')
    tosub.write(f'error       = ./log/{op1}_{model}_limits.$(ClusterId).$(ProcId).err\n')
    #tosub.write(f'log         = ./log/{op1}_{model}_limits.$(ClusterId).log\n')

tosub.write(f'log         = dev/null\n')



tosub.write('+JobFlavour = "microcentury"\n')
tosub.write('MY.WantOS = "el7"\n')
tosub.write('RequestCpus = 8\n')

if op2:
    tosub.write(f'queue myargs from utils/to_submit_{op1}_{op2}.txt\n')
else:
    tosub.write(f'queue myargs from utils/to_submit_{op1}.txt\n')

tosub.close()



if op2:
    out = open(f'./utils/to_submit_{op1}_{op2}.txt','w')
else:
    out = open(f'./utils/to_submit_{op1}.txt','w')

for i in range(njobs):
    pta = i * ppj
    ptb = (i+1) * ppj - 1

    if op2:
        out.write(f'{workspace}\t{op1}\t{rng1}\t{op2}\t{rng2}\t{pts}\t{pta}\t{ptb}\t{pothops}\t{frz_ops}\n')
    else:
        out.write(f'{workspace}\t{op1}\t{rng1}\t{pts}\t{pta}\t{ptb}\t{pothops}\t{frz_ops}\n')


out.close()
