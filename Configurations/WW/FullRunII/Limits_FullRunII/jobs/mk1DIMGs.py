#!/usr/bin/env python3

import os
import argparse
parser = argparse.ArgumentParser()

mops = ['cW','cHDD','cHWB']
#mops = ['cW','cHl3','cll1']
#mops = ['cW','cHDD','cHWB','cHl3','cHq3','cll1']

wkspcs = ['2017_allOps_model','2017_combOps_model']
#wkspcs = ['2016_HIPM_allOps_model','2016_noHIPM_allOps_model','2017_allOps_model','2018_allOps_model']

parser.add_argument('-mdl','--model',dest='model',default='fixed',help='float or fixed?')
parser.add_argument('-w','--wkspc',dest='workspace',default='allOps_model.root')
parser.add_argument('-n','--name',dest='name',help='Name to print')

args = parser.parse_args()

model = args.model
workspace = args.workspace
name = args.name

for i in range(len(mops)):
    op1 = mops[i]

    print('\n==================================================================')
    print('/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
    print('==================================================================\n')
    print(f'  OPERATOR: {op1}\n\n\n')

    for j in range(len(wkspcs)):
        workspace = wkspcs[j]

        print('\n------------------------------------------------------------------')
        print(f'  WORKSPACE: {workspace}\n\n\n')

        # hadd the models together
        print('H-adding')
        os.makedirs(f'./1D/{op1}/{workspace}/split_jobs')
        os.system(f'mv ./1D/{op1}/{workspace}/*.root ./1D/{op1}/{workspace}/split_jobs/')

        os.system(f'hadd ./1D/{op1}/{workspace}/{op1}.higgsCombine.MultiDimFit.mH125.root  ./1D/{op1}/{workspace}/split_jobs/*.root')

        # Make the scans
        print('Making scans')
            
        scanCMD = f'/afs/cern.ch/user/c/carbour/projects/aC/CMSSW_10_6_27/src/HiggsAnalysis/AnalyticAnomalousCoupling/scripts/mkEFTScan.py ' \
                + f'./1D/{op1}/{workspace}/{op1}.higgsCombine.MultiDimFit.mH125.root -p k_{op1} -maxNLL 5 -lumi 138 ' \
                + f'-cms -preliminary -xlabel "{op1} [TeV^{-2}]" '
        print(scanCMD)
        os.system(scanCMD)

        # Moving and renaming:
        print('Moving scan.pdf')
        os.system(f'mv scan.pdf.pdf ./1D/{op1}/{workspace}/{op1}_{model}.pdf')
        os.system(f'mv scan.pdf.png ./1D/{op1}/{workspace}/{op1}_{model}.png')
        #os.system(f'convert -define pdf:use-cropbox=true ./2D/{pair}_{model}.pdf ./2D/{pair}_scan.png')

        print('\n\n\n')
