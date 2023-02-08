# nuisances
# name of samples here must match keys in samples.py    

try:
    mc = [skey for skey in samples if skey != 'DATA' and not skey.startswith('Fake')]
except NameError:
    mc = []

try:
    signal = [skey for skey in samples if skey.startswith('AZH')]
except NameError:
    signal = []

try:
    fitcuts = [cut for cut in cuts if 'SR' in cut or 'CR' in cut]
except NameError:
    fitcuts = []

#### Luminosity

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2017',
    'type': 'lnN',
    'samples': dict((skey, '1.020') for skey in mc),
    'cuts' : fitcuts
}

nuisances['lumi_Correlated'] = {
    'name': 'lumi_correlated',
    'type': 'lnN',
    'samples': dict((skey, '1.009') for skey in mc),
    'cuts' : fitcuts
}

nuisances['lumi_1718'] = {
    'name': 'lumi_13TeV_1718',
    'type': 'lnN',
    'samples': dict((skey, '1.006') for skey in mc),
    'cuts' : fitcuts
}


#### Theoretical Systematics

# Scale
from LatinoAnalysis.Tools.HiggsXSection  import *
HiggsXS = HiggsXSection()

nuisances['QCDscale_ttH']  = {
  'name'  : 'QCDscale_ttH', 
  'samples'  : {
    'ttH_hww': HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ttH','125.09','scale','sm'),                  
  },
  'type'  : 'lnN',
  'cuts' : fitcuts
}

variations = ['Alt$(LHEScaleWeight[0],1)', 'Alt$(LHEScaleWeight[1],1)', 'Alt$(LHEScaleWeight[3],1)', 'Alt$(LHEScaleWeight[5],1)', 'Alt$(LHEScaleWeight[7],1)', 'Alt$(LHEScaleWeight[8],1)']

nuisances['QCDscale_V'] = {
    'name': 'QCDscale_V',
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {'ttV': variations},
    'AsLnN': '0',
    'cuts' : fitcuts
}

nuisances['QCDscale_VVV'] = {
    'name': 'QCDscale_VVV',
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {'VVV': variations},
    'AsLnN': '0',
    'cuts' : fitcuts
}

nuisances['QCDscale_VH'] = {
    'name': 'QCDscale_VH',
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': dict((skey, variations) for skey in signal),
    'AsLnN': '0',
    'cuts' : fitcuts
}

nuisances['QCDscale_VV'] = {
    'name': 'QCDscale_VV',
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {
        'Zg'      : variations,
        'ZgS'     : variations,
        'WZ'      : variations,
        'ZZ'      : variations,
    },
    'cuts' : fitcuts
}


nuisances['pdf_Higgs_ttH'] = {
               'name': 'pdf_Higgs_ttH',
               'type': 'lnN',
               'samples': {
                   'ttH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ttH','125.09','pdf','sm')
                   },
               'cuts' : fitcuts
              }

nuisances['pdf_qqbar'] = {
              'name': 'pdf_qqbar',
              'type': 'lnN',
              'samples': {
                  'Zg':  '1.04',
                  'ZgS': '1.04',
                  'WZ':  '1.04',
                  'ZZ':  '1.04',
		  'ttV': '1.04',
                  },
              'cuts' : fitcuts
              }


pdf_variations = ["LHEPdfWeight[%d]" %i for i in range(1,101)] # Float_t LHE pdf variation weights (w_var / w_nominal) for LHA IDs 320901 - 321000
nuisances['pdf_AZH']  = {
      'name'  : 'CMS_AZH_pdf_2017',
      'kind'  : 'weight_rms',
      'type'  : 'shape',
      'samples'  : dict((skey, variations) for skey in signal)
#      'scale' : nfdict["pdf_WW"] --> I should calculate my own norm factor here
}

#To be updated for v7
nuisances['PS_ISR'] = {
     'name': 'PS_ISR',
     'kind': 'weight',
     'type': 'shape',
     'samples': dict((skey, ['PSWeight[2]', 'PSWeight[0]']) for skey in mc), 
     'cuts' : fitcuts
}

#To be updated for v7
nuisances['PS_FSR'] = {
     'name': 'PS_FSR',
     'kind': 'weight',
     'type': 'shape',
     'samples': dict((skey, ['PSWeight[3]', 'PSWeight[1]']) for skey in mc), 
     'cuts' : fitcuts
}

#To be updated for v7
nuisances['PU'] = {
    'name': 'CMS_PU_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
          'WZ'      : ['0.991966*(puWeightUp/puWeight)', '1.005891*(puWeightDown/puWeight)'],
          'ZZ'      : ['0.991473*(puWeightUp/puWeight)', '1.008323*(puWeightDown/puWeight)'],
          'VVV'     : ['1.004325*(puWeightUp/puWeight)', '0.995718*(puWeightDown/puWeight)'],
          'ttV'     : ['(puWeightUp/puWeight)', '(puWeightDown/puWeight)'],
          'Zg'      : ['0.996218*(puWeightUp/puWeight)', '1.009114*(puWeightDown/puWeight)'],
          'top'     : ['0.998941*(puWeightUp/puWeight)', '1.000953*(puWeightDown/puWeight)'],
    },
    'AsLnN': '1',
    'cuts' : fitcuts
}


nuisances['PU_AZH'] = {
     'name': 'PU_AZH',
     'kind': 'weight',
     'type': 'shape',
     'samples': dict((skey, ['(puWeightUp/puWeight)', '(puWeightDown/puWeight)']) for skey in signal),
     'AsLnN': '1', 
     'cuts' : fitcuts
}


### PU ID SF uncertainty
puid_syst = ['Jet_PUIDSF_up/Jet_PUIDSF', 'Jet_PUIDSF_down/Jet_PUIDSF']

nuisances['jetPUID'] = {
    'name': 'CMS_PUID_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, puid_syst) for skey in mc)
}

nuisances['UE']  = {
                'name'  : 'UE',
                'skipCMS' : 1,
                'type'  : 'lnN',
                'samples'  : dict((skey, puid_syst) for skey in mc), 
                'cuts' : fitcuts
}


#### Top

apply_on = {
    'top': [
        '(topGenPt * antitopGenPt <= 0.) * 1.0816 + (topGenPt * antitopGenPt > 0.)',
        '(topGenPt * antitopGenPt <= 0.) * 0.9184 + (topGenPt * antitopGenPt > 0.)'
    ]
}

nuisances['singleTopToTTbar'] = {
    'name': 'singleTopToTTbar',
    'skipCMS': 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': apply_on,
    'cuts' : fitcuts
}

nuisances['TopPtRew'] = {
    'name': 'CMS_topPtRew',   # Theory uncertainty
    'kind': 'weight',
    'type': 'shape',
    'samples': {'top': ["1.", "1./Top_pTrw"]},
    'symmetrize': True,
    'cuts' : fitcuts
}

#### FAKES

fakeW_EleUp       = '( fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3lElUp       / fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3l )'
fakeW_EleDown     = '( fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3lElDown     / fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3l )'
fakeW_MuUp        = '( fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3lMuUp       / fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3l )'
fakeW_MuDown      = '( fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3lMuDown     / fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3l )'
fakeW_statEleUp   = '( fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3lstatElUp   / fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3l )'
fakeW_statEleDown = '( fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3lstatElDown / fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3l )'
fakeW_statMuUp    = '( fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3lstatMuUp   / fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3l )'
fakeW_statMuDown  = '( fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3lstatMuDown / fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_3l )'

nuisances['fake_syst_e']  = {
               'name'  : 'CMS_fake_syst_e',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake_e' : '1.30',
                             },
               'cuts' : fitcuts
}

nuisances['fake_syst_m']  = {
               'name'  : 'CMS_fake_syst_m',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake_m' : '1.30',
                             },
               'cuts' : fitcuts
}

nuisances['fake_ele']  = {
                'name'  : 'CMS_fake_e_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'     : [ fakeW_EleUp , fakeW_EleDown ],
                             },
                'cuts' : fitcuts
}

nuisances['fake_ele_stat']  = {
                'name'  : 'CMS_fake_stat_e_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'      : [ fakeW_statEleUp , fakeW_statEleDown ],
                             },
                'cuts' : fitcuts
}

nuisances['fake_mu']  = {
                'name'  : 'CMS_fake_m_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'     : [ fakeW_MuUp , fakeW_MuDown ],
                             },
                'cuts' : fitcuts
}

nuisances['fake_mu_stat']  = {
                'name'  : 'CMS_fake_stat_m_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'     : [ fakeW_statMuUp , fakeW_statMuDown ],
                             },
                'cuts' : fitcuts
}

##### B-tagger

for shift in [ 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2017'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
        'cuts' : fitcuts
    }

#### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_3l_u)/(TriggerEffWeight_3l))*(TriggerEffWeight_3l>0.02) + (TriggerEffWeight_3l<=0.02)', '(TriggerEffWeight_3l_d)/(TriggerEffWeight_3l)']

nuisances['trigg']  = {
                'name'  : 'CMS_eff_hwwtrigger_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, trig_syst) for skey in mc),
                'cuts' : fitcuts
}

#### Prefiring

prefire_syst = ['PrefireWeight_Up/PrefireWeight', 'PrefireWeight_Down/PrefireWeight']

nuisances['prefire'] = {
    'name': 'CMS_eff_prefiring_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples'  : dict((skey, prefire_syst) for skey in mc),
    'cuts' : fitcuts
}

##### Electron Efficiency and energy scale

id_syst_ele = ['SFweightEleUp', 'SFweightEleDown'] #defined in aliases

nuisances['eff_e']  = {
                'name'  : 'CMS_eff_e_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, id_syst_ele) for skey in mc),
                'cuts' : fitcuts
}
##WIP for UL
#nuisances['electronpt']  = {
#                'name'  : 'CMS_scale_e_2017',
#                'kind'  : 'suffix',
#                'type'  : 'shape',
#                'mapUp' : 'ElepTup',
#                'mapDown' : 'ElepTdo',
#                'samples'  : dict((skey, ['1', '1']) for skey in mc),
#                'folderUp'   : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__ElepTup_suffix', 
#                'folderDown' : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__ElepTdo_suffix', 
#                'AsLnN' : '1',
#                'cuts' : fitcuts
#}

###### Muon Efficiency and energy scale

id_syst_mu = ['SFweightMuUp', 'SFweightMuDown']  #defined in aliases

nuisances['eff_m']  = {
                'name'  : 'CMS_eff_m_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, id_syst_mu) for skey in mc),
                'cuts' : fitcuts
}

#nuisances['muonpt']  = {
#                'name'  : 'CMS_scale_m_2017',
#                'kind'  : 'suffix',
#                'type'  : 'shape',
#                'mapUp' : 'MupTup',
#                'mapDown' : 'MupTdo',
#                'samples'  : dict((skey, ['1', '1']) for skey in mc),
#                'folderUp'   : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__MupTup_suffix', 
#                'folderDown' : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__MupTdo_suffix', 
#                'AsLnN' : '1',
#                'cuts' : fitcuts
#}

####### Jet energy scale

#jes_systs = ['JESAbsolute','JESAbsolute_2017','JESBBEC1','JESBBEC1_2017','JESEC2','JESEC2_2017','JESFlavorQCD','JESHF','JESHF_2017','JESRelativeBal','JESRelativeSample_2017']
#folderup = ""
#folderdo = ""

#for js in jes_systs:
#  if 'Absolute' in js:
#    folderup =  treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__JESAbsoluteup_suffix' 
#    folderdo = treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__JESAbsolutedo_suffix' 
#  elif 'BBEC1' in js:
#    folderup = treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__JESBBEC1up_suffix'
#    folderdo = treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__JESBBEC1do_suffix'
#  elif 'EC2' in js:
#    folderup = treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__JESEC2up_suffix'
#    folderdo =  treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__JESEC2do_suffix'
#  elif 'HF' in js:
#    folderup = treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__JESHFup_suffix'
#    folderdo = treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__JESHFdo_suffix'
#  elif 'Relative' in js:
#    folderup = treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__JESRelativeup_suffix'
#    folderdo = treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__JESRelativedo_suffix'
#  elif 'FlavorQCD' in js:
#    folderup = treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__JESFlavorQCDup_suffix'
#    folderdo = treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__JESFlavorQCDdo_suffix'
#
#  nuisances[js] = {
#                'name': 'CMS_scale_'+js,
#                'kind': 'suffix',
#                'type': 'shape',
#                'mapUp': js+'up',
#                'mapDown': js+'do',
#                'samples': dict((skey, ['1', '1']) for skey in mc),
#                'samples': {'ttV': ['1','1'], 'VVV': ['1','1'], 'ZH_hww': ['1','1'], 'ggZH_hww': ['1','1'], 'WH_hww': ['1','1'], 'ttH_hww': ['1','1'], 'ZH_htt': ['1','1'], 'WH_htt': ['1','1']},
#		'folderUp': folderup,
#	        'folderDown': folderdo,	
#                'folderUp'   : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__JESup_suffix', 
#                'folderDown' : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__JESdo_suffix', 
#                'AsLnN': '1',
#                'cuts' : fitcuts
#  }

##### Jet energy resolution
#nuisances['JER'] = {
#    'name' : 'CMS_res_j_2017',
#    'kind': 'suffix',
#    'type': 'shape',
#    'mapUp': 'JERup',
#    'mapDown': 'JERdo',
#    'samples': dict((skey, ['1', '1']) for skey in mc),
#    'folderUp': treeBaseDir+'Summer20UL17_106x_nAODv9_Full2017v9/MCl1loose2017v9__MCCorr2017v9NoJERInHorn__l2tightOR2017v9__JERup_suffix',
#    'folderDown': treeBaseDir+'Summer20UL17_106x_nAODv9_Full2017v9/MCl1loose2017v9__MCCorr2017v9NoJERInHorn__l2tightOR2017v9__JERdo_suffix',
#    'AsLnN': '1'
#}
##### MET energy scale

#nuisances['met']  = {
#                'name'  : 'CMS_scale_met_2017',
#                'kind'  : 'suffix',
#                'type'  : 'shape',
#                'mapUp' : 'METup',
#                'mapDown' : 'METdo',
#                'samples'  : dict((skey, ['1', '1']) for skey in mc),
#                'folderUp'   : treeBaseDir+'Summer20UL17_106x_nAODv9_Full2017v9/MCl1loose2017v9__MCCorr2017v9NoJERInHorn__l2tightOR2017v9__METup_suffix', 
#                'folderDown' : treeBaseDir+'Summer20UL17_106x_nAODv9_Full2017v9/MCl1loose2017v9__MCCorr2017v9NoJERInHorn__l2tightOR2017v9__METdo_suffix', 
#                'AsLnN' : '1',
#                'cuts' : fitcuts
#}

# Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat']  = {
              'type'  : 'auto',
              'maxPoiss'  : '10',
              'includeSignal'  : '1',
              #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
              #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
              'samples' : {},
              'cuts' : fitcuts
             }

for n in nuisances.values():
    n['skipCMS'] = 1