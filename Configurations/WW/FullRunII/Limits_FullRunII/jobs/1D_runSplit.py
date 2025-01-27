#!/usr/bin/env python3

import os

mops = ['cW','cHDD','cHWB','cHl3','cHq3','cll1']

pts = 2000
ppj = 20
mode='float'

for i in range(len(mops)):
    op1 = mops[i]

    print(f'utils/split.py -mdl {mode} -op1 {op1} -pts {pts} -ppj {ppj}')
    os.system(f'utils/split.py -mdl {mode} -op1 {op1} -pts {pts} -ppj {ppj}')
    print('\n')

    print(f'condor_submit {op1}_1D_sendCMDs.sub')
    os.system(f'condor_submit {op1}_1D_sendCMDs.sub')

    print('\n\n\n')
