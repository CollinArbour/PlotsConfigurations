# structure configuration for datacard
structure ={}

# keys here must match keys in samples.py 
for iproc in samples.keys():
    structure[iproc] = {
        'isSignal' : 1 if 'sm' in iproc or 'quad' in iproc else 0,
        'isData'   : 1 if iproc == 'DATA' else 0,
    }

for nuis in nuisances.itervalues():
  if 'cutspost' in nuis:
    nuis['cuts'] = nuis['cutspost'](nuis, cuts)

    print nuis

structure['WWewk']['removeFromCuts'] = ['ww2l2v_13TeV_top_1j', 'ww2l2v_13TeV_top_0j', 'ww2l2v_13TeV_sr_2j_B0', 'ww2l2v_13TeV_sr_1j_B0', 'ww2l2v_13TeV_top_2j', 'ww2l2v_13TeV_sr_0j_B0']	
