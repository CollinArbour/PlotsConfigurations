#!/bin/bash

op1=$1
rng1=$2

pts=$3
pta=$4
ptb=$5

othOps=$6
frzOps=$7

term=$op1
mcmssw=/afs/cern.ch/user/c/carbour/projects/aC/CMSSW_10_6_27/src

source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700
cd $mcmssw
eval `scram runtime -sh`

mbase=PlotsConfigurations/Configurations/WW/FullRunII/Limits_FullRunII/jobs
mdir=1D/$op1

mkdir -p $mbase/$mdir
cd $mbase/$mdir

if [ "$frzOps" == "FLOAT" ]; then
    combine -M MultiDimFit $mcmssw/$mbase/workspaces/allOps.root --algo=grid -t -1 -m 125 --points $pts --firstPoint $pta --lastPoint $ptb -n SPLIT.POINTS.$pta.$ptb \
        --redefineSignalPOIs k_$op1 \
        --freezeParameters r  \
        --setParameters r=1,$othOps    --setParameterRanges k_"$op1"=-$rng1,$rng1     \
        --verbose -1
else
    combine -M MultiDimFit $mcmssw/$mbase/workspaces/allOps.root --algo=grid -t -1 -m 125 --points $pts --firstPoint $pta --lastPoint $ptb -n SPLIT.POINTS.$pta.$ptb \
        --redefineSignalPOIs k_$op1 \
        --freezeParameters r,$frzOps  \
        --setParameters r=1,$othOps    --setParameterRanges k_"$op1"=-$rng1,$rng1     \
        --verbose -1
fi
