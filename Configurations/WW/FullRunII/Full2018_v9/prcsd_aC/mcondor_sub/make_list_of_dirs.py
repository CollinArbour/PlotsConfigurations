#/usr/bin/env python3

import os
import shutil
import glob

# make list from subdirs within working dir 

## USER INPUTS WORKING DIRECTORY HERE; keep wildcard to probe subdirectories of working directory   
#for f in glob.glob('/afs/cern.ch/work/t/tcarnaha/HWW2022/jobs/mkShapes__offshell2018_v9_ggH__ALL/*/*.sh', recursive=True): ##keep the wildcards in the path
for f in glob.glob('/afs/cern.ch/user/c/carbour/jobs/mkShapes__WW2018_v9_aC__ALL/*/*.sh', recursive=True): ##keep the wildcards in the path
    os.system('echo ' + f + ' >> dirs.txt') ## keeps entire pathway + prints into dirs.txt

    #g = os.path.split(f)[1] ## keeps subdir only
    #os.system('echo ' + g + ' >> dirs.txt')

    
