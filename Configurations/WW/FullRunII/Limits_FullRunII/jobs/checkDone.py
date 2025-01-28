#!/usr/bin/env python3 

import os

mops = ['cW','cHDD','cHWB']
#mops = ['cW','cHDD','cHWB','cHl3','cHq3','cll1']

wkspcs = ['2017_allOps_model','2017_combOps_model']
#wkspcs = ['2016_HIPM_allOps_model','2016_noHIPM_allOps_model','2017_allOps_model','2018_allOps_model','allOps_model']
#wkspcs = ['allOps_model']

for op in mops:
    print()
    for wkspc in wkspcs:
        print(f'Operator: {op} \t Workspace: {wkspc}')
        os.system(f'find ./1D/{op}/{wkspc}/ -type f -size +5k -printf 1 | wc -c')
