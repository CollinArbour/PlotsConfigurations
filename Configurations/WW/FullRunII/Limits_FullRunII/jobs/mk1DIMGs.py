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

for i in range(len(mops)):
    op1 = mops[i]

    # hadd the models together
#    print('H-adding')
#    os.system(f'hadd ./1D/{op1}.higgsCombine.MultiDimFit.mH125.root  ./1D/{op1}/*.root')

    # Make the scans
    print('Making scans')
        
    scanCMD = f'/afs/cern.ch/user/c/carbour/projects/aC/CMSSW_10_6_27/src/HiggsAnalysis/AnalyticAnomalousCoupling/scripts/mkEFTScan.py ' \
            + f'./1D/{op1}/{op1}.higgsCombine.MultiDimFit.mH125.root -p k_{op1} -maxNLL 5 -lumi 138 ' \
            + f'-cms -preliminary -xlabel "{op1} [TeV^{-2}]" '
    print(scanCMD)
    os.system(scanCMD)

    # Moving and renaming:
    print('Moving scan.pdf')
    os.system(f'mv scan.pdf.pdf ./1D/{op1}/{op1}_{model}.pdf')
    os.system(f'mv scan.pdf.png ./1D/{op1}/{op1}_{model}.png')
    #os.system(f'convert -define pdf:use-cropbox=true ./2D/{pair}_{model}.pdf ./2D/{pair}_scan.png')

    print('\n\n\n')
