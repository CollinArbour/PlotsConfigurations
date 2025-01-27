#!/usr/bin/env python3

import os
import argparse
parser = argparse.ArgumentParser()

mops = ['cW','cHDD','cHWB','cHl3','cHq3','cll1']

parser.add_argument('-mdl','--model',dest='model',default='fixed',help='float or fixed?')
parser.add_argument('-n','--name',dest='name',help='Name to print')

args = parser.parse_args()

model = args.model
name = args.name

for i in range(len(mops)-1):
    op1 = mops[i]

    for j in range(i+1,len(mops)):
        op2 = mops[j]

        if f'{op1}_{op2}' != 'cW_cHDD' and f'{op1}_{op2}' != 'cHWB_cHl3':
            continue

        pair = f'{op1}_{op2}'
        print(pair)

        # hadd the models together
        print('H-adding')
        os.system(f'hadd ./2D/{pair}.higgsCombine.MultiDimFit.mH125.root  ./2D/{pair}/*.root')

        # Make the scans
        print('Making scans')
        
        scanCMD = f'/afs/cern.ch/user/c/carbour/projects/aC/CMSSW_10_6_27/src/HiggsAnalysis/AnalyticAnomalousCoupling/scripts/mkEFTScan.py ' \
                + f'./2D/{pair}.higgsCombine.MultiDimFit.mH125.root -p k_{op1} k_{op2} -maxNLL 10 -lumi 59.83 ' \
                + f'-cms -preliminary -xlabel "{op1} [TeV^{-2}]" -ylabel "{op2} [TeV^{-2}]" '
        print(scanCMD)
        os.system(scanCMD)

        # Moving and renaming:
        print('Moving scan.pdf')
        os.system(f'mv scan.pdf.pdf ./2D/{pair}_{model}.pdf')
        os.system(f'mv scan.pdf.png ./2D/{pair}_{model}.png')
        #os.system(f'convert -define pdf:use-cropbox=true ./2D/{pair}_{model}.pdf ./2D/{pair}_scan.png')

        print('\n\n\n')
