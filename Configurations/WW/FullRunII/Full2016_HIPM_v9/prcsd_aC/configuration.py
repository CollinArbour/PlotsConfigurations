# Configuration file to produce initial root files -- has both merged and binned ggH samples

treeName = 'Events'

backs = '../../../../../../../../../../eos/public/prcsd_aC'

era = '2016_HIPM_v9_aC'
tag = 'WW2016_HIPM_v9_aC'

# used by mkShape to define output directory for root files
outputDir = '{}/rootFile/{}'.format(backs,era)

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts.py' 

# file with list of samples
#samplesFile = 'samples.py'
samplesFile = 'indv_samples.py'

# file with list of samples
plotFile = 'plot.py' 

# luminosity to normalize to (in 1/fb)
lumi = 19.52

# used by mkPlot to define output directory for plots
outputDirPlots = '{}/plots/{}'.format(backs,era)

# used by mkDatacards to define output directory for datacards
outputDirDatacard = '{}/datacards/{}'.format(backs,era)

# structure file for datacard
structureFile = 'structure.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'
