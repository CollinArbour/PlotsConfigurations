#!/bin/bash

op1=$1
rng1=$2
op2=$3
rng2=$4

pts=$5
pta=$6
ptb=$7

othOps=$8
frzOps=$9

term="$op1"_"$op2"
mcmssw=/afs/cern.ch/user/c/carbour/projects/aC/CMSSW_10_6_27/src
mWrkSpc=RunII_allOps_model.root

source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700
cd $mcmssw
eval `scram runtime -sh`

mbase=PlotsConfigurations/Configurations/WW/FullRunII/Limits_FullRunII/jobs
mdir=2D/"$op1"_"$op2"

mkdir -p $mbase/$mdir
cd $mbase/$mdir

if [ "$frzOps" == "FLOAT" ]; then
    combine -M MultiDimFit $mcmssw/$mbase/workspaces/$mWrkSpc --algo=grid -t -1 -m 125 --points $pts --firstPoint $pta --lastPoint $ptb -n SPLIT.POINTS.$pta.$ptb \
        --redefineSignalPOIs k_$op1,k_$op2 \
        --freezeParameters r  \
        --setParameters r=1,$othOps    --setParameterRanges k_"$op1"=-$rng1,$rng1:k_"$op2"=-$rng2,$rng2     \
        --verbose -1
else
    combine -M MultiDimFit $mcmssw/$mbase/workspaces/$mWrkSpc --algo=grid -t -1 -m 125 --points $pts --firstPoint $pta --lastPoint $ptb -n SPLIT.POINTS.$pta.$ptb \
        --redefineSignalPOIs k_$op1,k_$op2 \
        --freezeParameters r,$frzOps  \
        --setParameters r=1,$othOps    --setParameterRanges k_"$op1"=-$rng1,$rng1:k_"$op2"=-$rng2,$rng2     \
        --verbose -1
fi
