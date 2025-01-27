#!/usr/bin/env python3

import os

mops = ['cW','cHDD','cHWB','cHl3','cHq3','cll1']

pts = 2000
ppj = 4
mode='fixed'

for i in range(len(mops)-1):
    op1 = mops[i]

    for j in range(i+1,len(mops)):
        op2 = mops[j]

        #print(f'{op1}_{op2}') 

        print(f'utils/split.py -mdl {mode} -op1 {op1} -op2 {op2} -pts {pts} -ppj {ppj}')
        os.system(f'utils/split.py -mdl {mode} -op1 {op1} -op2 {op2} -pts {pts} -ppj {ppj}')
        print('\n')

        print(f'condor_submit {op1}_{op2}_sendCMDs.sub')
        os.system(f'condor_submit {op1}_{op2}_sendCMDs.sub')

        print('\n\n\n')
