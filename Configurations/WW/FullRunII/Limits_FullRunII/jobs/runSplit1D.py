#!/usr/bin/env python3

import os

mops = ['cW','cHDD','cHWB']
#mops = ['cW','cHDD','cHWB','cHl3','cHq3','cll1']

wkspcs = ['2017_combOps_model']
#wkspcs = ['2016_HIPM_allOps_model','2016_noHIPM_allOps_model','2017_allOps_model','2018_allOps_model','allOps_model']
#wkspcs = ['allOps_model']

pts = 2000
ppj = 20
mode='float'
#wkspc = '2016_noHIPM_allOps_model'

for i in range(len(mops)):
    op1 = mops[i]

    print('\n==================================================================')
    print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
    print('==================================================================\n')
    print(f'  OPERATOR: {op1}\n\n\n')

    for j in range(len(wkspcs)):
        wkspc = wkspcs[j]

        print('\n------------------------------------------------------------------')
        print(f'  WORKSPACE: {wkspc}\n\n\n')

        print(f'utils/split.py -mdl {mode} -w {wkspc} -op1 {op1} -pts {pts} -ppj {ppj}')
        os.system(f'utils/split.py -mdl {mode} -w {wkspc} -op1 {op1} -pts {pts} -ppj {ppj}')
        print('\n')

        print(f'condor_submit {op1}_1D_sendCMDs.sub')
        os.system(f'condor_submit {op1}_1D_sendCMDs.sub')

        print('\n\n\n')
