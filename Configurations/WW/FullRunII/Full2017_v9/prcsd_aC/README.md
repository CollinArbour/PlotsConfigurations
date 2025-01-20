# Procedure for obtaining limits:

## Create Workspace:
```
text2workspace.py datacard_combined.txt -P HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFTNegative:analiticAnomalousCouplingEFTNegative  -o allOps_model.root  --PO eftOperators=cHDD,cHWB,cHl3,cHq3,cW,cll1
```

## Example command for obtaining 1D limits:
(250 points seems to works ok when troubleshooting)
```
combine -M MultiDimFit allOps_model.root  --algo=grid --points 2000  -m 125   -t -1     \
    --redefineSignalPOIs k_cW \
    --freezeParameters r  \
    --setParameters r=1,k_cHDD=0,k_cHWB=0,k_cHl3=0,k_cHq3=0,k_cll1=0    --setParameterRanges k_cW=-2,2     \
    --verbose -1
```

# Nuisances updated

## Theoretical Nuisances:
1. ['QCDscale\_WW']
2. ['PDFscale\_VV']
3. ['PS\_ISR'] / ['PS\_FSR']
4. ['UE']
5. ['PU']

## Statistical:
1. Swithced to AutoMCStats for all statistical uncertaintes
    - Set uncertainty to 0 for all EFT templates in `structure.py`
        - Not set to 0 for ['sm'] template
