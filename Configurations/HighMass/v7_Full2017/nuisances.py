import math
import copy
# nuisances
HiggsXS = HiggsXSection()

# name of samples here must match keys in samples.py 

################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity

mc_emb = [skey for skey in samples if skey != 'DATA' and not skey.startswith('Fake') and skey != 'DYveto']
mc = [skey for skey in mc_emb if skey != 'DYemb']
mc_noDYHM = [skey for skey in mc if ('DY' not in skey or EMorEEorMM=="em") and 'GGH' not in skey and 'QQH' not in skey] # Using recoil corrected DY in SF final state -> nuisances in different directory. Same for HM because friend trees broke after adding another postprocessing step
mc_HM = [skey for skey in mc if 'GGH' in skey or 'QQH' in skey]

# Combined:
#nuisances['lumi'] = {
#    'name': 'lumi_13TeV_2017',
#    'type': 'lnN',
#    'samples': dict((skey, '1.023') for skey in mc if skey not in ['WW', 'top', 'DY'])
#}

# Old:
#nuisances['lumi_Uncorrelated'] = {
#    'name': 'lumi_13TeV_2017',
#    'type': 'lnN',
#    'samples': dict((skey, '1.02') for skey in mc if skey not in ['WW', 'WW2J', 'WWewk', 'top', 'DY'])
#}
#
#nuisances['lumi_XY'] = {
#    'name': 'lumi_13TeV_XY',
#    'type': 'lnN',
#    'samples': dict((skey, '1.008') for skey in mc if skey not in ['WW', 'WW2J', 'WWewk', 'top', 'DY'])
#}
#
#nuisances['lumi_LS'] = {
#    'name': 'lumi_13TeV_LS',
#    'type': 'lnN',
#    'samples': dict((skey, '1.003') for skey in mc if skey not in ['WW', 'WW2J', 'WWewk', 'top', 'DY'])
#}
#
#nuisances['lumi_BBD'] = {
#    'name': 'lumi_13TeV_BBD',
#    'type': 'lnN',
#    'samples': dict((skey, '1.004') for skey in mc if skey not in ['WW', 'WW2J', 'WWewk', 'top', 'DY'])
#}
#
#nuisances['lumi_DB'] = {
#    'name': 'lumi_13TeV_DB',
#    'type': 'lnN',
#    'samples': dict((skey, '1.005') for skey in mc if skey not in ['WW', 'WW2J', 'WWewk', 'top', 'DY'])
#}
#
#nuisances['lumi_BCC'] = {
#    'name': 'lumi_13TeV_BCC',
#    'type': 'lnN',
#    'samples': dict((skey, '1.003') for skey in mc if skey not in ['WW', 'WW2J', 'WWewk', 'top', 'DY'])
#}
#
#nuisances['lumi_GS'] = {
#    'name': 'lumi_13TeV_GS',
#    'type': 'lnN',
#    'samples': dict((skey, '1.001') for skey in mc if skey not in ['WW', 'WW2J', 'WWewk', 'top', 'DY'])
#}

# New:
nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2017',
    'type': 'lnN',
    'samples': dict((skey, '1.020') for skey in mc if skey not in ['WW', 'WW2J', 'WWewk', 'top', 'DY'])
}

nuisances['lumi_Correlated'] = {
    'name': 'lumi_13TeV_correlated',
    'type': 'lnN',
    'samples': dict((skey, '1.009') for skey in mc if skey not in ['WW', 'WW2J', 'WWewk', 'top', 'DY'])
}

nuisances['lumi_1718'] = {
    'name': 'lumi_13TeV_1718',
    'type': 'lnN',
    'samples': dict((skey, '1.006') for skey in mc if skey not in ['WW', 'WW2J', 'WWewk', 'top', 'DY'])
}

#### FAKES

#if Nlep == '2' :
# already divided by central values in formulas !
fakeW_EleUp       = fakeW+'_EleUp'
fakeW_EleDown     = fakeW+'_EleDown'
fakeW_MuUp        = fakeW+'_MuUp'
fakeW_MuDown      = fakeW+'_MuDown'
fakeW_statEleUp   = fakeW+'_statEleUp'
fakeW_statEleDown = fakeW+'_statEleDown'
fakeW_statMuUp    = fakeW+'_statMuUp'
fakeW_statMuDown  = fakeW+'_statMuDown'


nuisances['fake_syst_em']  = {
               'name'  : 'CMS_fake_syst_em',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake_em' : '1.30',
                             },
               }
nuisances['fake_syst_me']  = {
               'name'  : 'CMS_fake_syst_me',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake_me' : '1.30',
                             },
               }
nuisances['fake_syst_of']  = {
               'name'  : 'CMS_fake_syst_of',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake_of' : '1.30',
                             },
               }
nuisances['fake_syst_ee']  = {
               'name'  : 'CMS_fake_syst_ee',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake_ee' : '1.30',
                             },
               }
nuisances['fake_syst_mm']  = {
               'name'  : 'CMS_fake_syst_mm',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake_mm' : '1.30',
                             },
               }

nuisances['fake_ele']  = {
                'name'  : 'CMS_fake_e_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake_em'     : [ fakeW_EleUp , fakeW_EleDown ],
                              'Fake_me'     : [ fakeW_EleUp , fakeW_EleDown ],
                              'Fake_of'     : [ fakeW_EleUp , fakeW_EleDown ],
                              'Fake_ee'     : [ fakeW_EleUp , fakeW_EleDown ],
                             },
}

nuisances['fake_ele_stat']  = {
                'name'  : 'CMS_fake_stat_e_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake_em'      : [ fakeW_statEleUp , fakeW_statEleDown ],
                              'Fake_me'      : [ fakeW_statEleUp , fakeW_statEleDown ],
                              'Fake_of'      : [ fakeW_statEleUp , fakeW_statEleDown ],
                              'Fake_ee'      : [ fakeW_statEleUp , fakeW_statEleDown ],
                             },
}

nuisances['fake_mu']  = {
                'name'  : 'CMS_fake_m_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake_em'     : [ fakeW_MuUp , fakeW_MuDown ],
                              'Fake_me'     : [ fakeW_MuUp , fakeW_MuDown ],
                              'Fake_of'     : [ fakeW_MuUp , fakeW_MuDown ],
                              'Fake_mm'     : [ fakeW_MuUp , fakeW_MuDown ],
                             },
}


nuisances['fake_mu_stat']  = {
                'name'  : 'CMS_fake_stat_m_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake_em'     : [ fakeW_statMuUp , fakeW_statMuDown ],
                              'Fake_me'     : [ fakeW_statMuUp , fakeW_statMuDown ],
                              'Fake_of'     : [ fakeW_statMuUp , fakeW_statMuDown ],
                              'Fake_mm'     : [ fakeW_statMuUp , fakeW_statMuDown ],
                             },
}

##### B-tagger
nuisances['btag_jes']  = {
                'name'  : 'CMS_btag_jes',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, ['(btagSFjesup/btagSF)', '(btagSFjesdown/btagSF)']) for skey in mc),
}

nuisances['btag_lf']  = {
                'name'  : 'CMS_btag_lf',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, ['(btagSFlfup/btagSF)', '(btagSFlfdown/btagSF)']) for skey in mc),
}

nuisances['btag_hf']  = {
                'name'  : 'CMS_btag_hf',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, ['(btagSFhfup/btagSF)', '(btagSFhfdown/btagSF)']) for skey in mc),
}

nuisances['btag_hfstats1']  = {
                'name'  : 'CMS_btag_hfstats1_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, ['(btagSFhfstats1up/btagSF)', '(btagSFhfstats1down/btagSF)']) for skey in mc),
}

nuisances['btag_hfstats2']  = {
                'name'  : 'CMS_btag_hfstats2_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, ['(btagSFhfstats2up/btagSF)', '(btagSFhfstats2down/btagSF)']) for skey in mc),
}

nuisances['btag_lfstats1']  = {
                'name'  : 'CMS_btag_lfstats1_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, ['(btagSFlfstats1up/btagSF)', '(btagSFlfstats1down/btagSF)']) for skey in mc),
}

nuisances['btag_lfstats2']  = {
                'name'  : 'CMS_btag_lfstats2_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, ['(btagSFlfstats2up/btagSF)', '(btagSFlfstats2down/btagSF)']) for skey in mc),
}

nuisances['btag_cferr1']  = {
                'name'  : 'CMS_btag_cferr1',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, ['(btagSFcferr1up/btagSF)', '(btagSFcferr1down/btagSF)']) for skey in mc),
}

nuisances['btag_cferr2']  = {
                'name'  : 'CMS_btag_cferr2',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, ['(btagSFcferr2up/btagSF)', '(btagSFcferr2down/btagSF)']) for skey in mc),
}


##### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)'] # TODO Cut at 0.02?

nuisances['trigg']  = {
                'name'  : 'CMS_eff_hwwtrigger_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, trig_syst) for skey in mc_emb),
}

##### Electron Efficiency and energy scale

nuisances['eff_e']  = {
                'name'  : 'CMS_eff_e_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, ['LepSF2l__ele_'+eleWP+'__Up' , 'LepSF2l__ele_'+eleWP+'__Do']) for skey in mc_emb), 
}

nuisances['electronpt']  = {
                'name'  : 'CMS_scale_e_2017',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp'  : 'ElepTup',
                'mapDown'  : 'ElepTdo',
                'samples': dict((skey, ['1', '1']) for skey in mc_noDYHM),
                'folderUp'   : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__ElepTup_suffix',
                'folderDown' : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__ElepTdo_suffix',
}
nuisances['electronpt_HM']  = {
                'name'  : 'CMS_scale_e_2017',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp'  : 'ElepTup',
                'mapDown'  : 'ElepTdo',
                'samples': dict((skey, ['1', '1']) for skey in mc_HM),
                'folderUp'   : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__BWReweight__ElepTup_suffix',
                'folderDown' : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__BWReweight__ElepTdo_suffix',
}

if EMorEEorMM!="em":
  nuisances['electronpt_DY']  = {
                'name'  : 'CMS_scale_e_2017',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp'  : 'ElepTup',
                'mapDown'  : 'ElepTdo',
                'samples': {
                     'DY'      : ['1', '1'],
                 },
                'folderUp'   : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__recoilDY__ElepTup_suffix',
                'folderDown' : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__recoilDY__ElepTdo_suffix',
  }

if useEmbeddedDY:
  nuisances['electronpt_emb']  = {
                  'name'  : 'CMS_scale_e_2017',
                  'kind'  : 'suffix',
                  'type'  : 'shape',
                  'mapUp'  : 'ElepTup',
                  'mapDown'  : 'ElepTdo',
                  'samples'  : {
                     'DYemb'      : ['1', '1'],
                   },
                  'folderUp'   : treeBaseDir+'Embedding2017_102X_nAODv7_Full2017v7/DATAl1loose2017v7__l2loose__l2tightOR2017v7__Embedding__EmbElepTup_suffix',
                  'folderDown' : treeBaseDir+'Embedding2017_102X_nAODv7_Full2017v7/DATAl1loose2017v7__l2loose__l2tightOR2017v7__Embedding__EmbElepTdo_suffix',
  }

##### Muon Efficiency and energy scale

nuisances['eff_m']  = {
                'name'  : 'CMS_eff_m_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, ['LepSF2l__mu_'+muWP+'__Up' , 'LepSF2l__mu_'+muWP+'__Do']) for skey in mc_emb),
}

nuisances['muonpt']  = {
                'name'  : 'CMS_scale_m_2017',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp'  : 'MupTup',
                'mapDown'  : 'MupTdo',
                'samples': dict((skey, ['1', '1']) for skey in mc_noDYHM),
                'folderUp'   : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__MupTup_suffix',
                'folderDown' : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__MupTdo_suffix',
}
nuisances['muonpt_HM']  = {
                'name'  : 'CMS_scale_m_2017',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp'  : 'MupTup',
                'mapDown'  : 'MupTdo',
                'samples': dict((skey, ['1', '1']) for skey in mc_HM),
                'folderUp'   : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__BWReweight__MupTup_suffix',
                'folderDown' : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__BWReweight__MupTdo_suffix',
}

if EMorEEorMM!="em":
  nuisances['muonpt_DY']  = {
                'name'  : 'CMS_scale_m_2017',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp'  : 'MupTup',
                'mapDown'  : 'MupTdo',
                'samples': {
                     'DY'      : ['1', '1'],
                 },
                'folderUp'   : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__recoilDY__MupTup_suffix',
                'folderDown' : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__recoilDY__MupTdo_suffix',
  }

if useEmbeddedDY:
  nuisances['muonpt_emb']  = {
                  'name'  : 'CMS_scale_m_2017',
                  'kind'  : 'suffix',
                  'type'  : 'shape',
                  'mapUp'  : 'MupTup',
                  'mapDown'  : 'MupTdo',
                  'samples'  : {
                     'DYemb'      : ['1', '1'],
                   },
                  'folderUp'   : treeBaseDir+'Embedding2017_102X_nAODv7_Full2017v7/DATAl1loose2017v7__l2loose__l2tightOR2017v7__Embedding__EmbMupTup_suffix',
                  'folderDown' : treeBaseDir+'Embedding2017_102X_nAODv7_Full2017v7/DATAl1loose2017v7__l2loose__l2tightOR2017v7__Embedding__EmbMupTdo_suffix',
  }

###### Jet energy scale

jes_systs = ['JESAbsolute', 'JESAbsolute_2017', 'JESBBEC1', 'JESBBEC1_2017', 'JESEC2', 'JESEC2_2017', 'JESFlavorQCD', 'JESHF', 'JESHF_2017', 'JESRelativeBal', 'JESRelativeSample_2017']

for js in jes_systs:
  for alpha in ['Absolute', 'BBEC1', 'EC2', 'HF', 'Relative', 'FlavorQCD']:
    if alpha in js: JesDirName = alpha
  nuisances[js]  = {
                'name'  : 'CMS_scale_'+js,
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp'  : js+'up',
                'mapDown'  : js+'do',
                'samples': dict((skey, ['1', '1']) for skey in mc_noDYHM),
                'folderUp'   : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__JES'+JesDirName+'up_suffix',
                'folderDown' : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__JES'+JesDirName+'do_suffix',
  }
  nuisances[js+'_HM']  = {
                'name'  : 'CMS_scale_'+js,
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp'  : js+'up',
                'mapDown'  : js+'do',
                'samples': dict((skey, ['1', '1']) for skey in mc_HM),
                'folderUp'   : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__BWReweight__JES'+JesDirName+'up_suffix',
                'folderDown' : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__BWReweight__JES'+JesDirName+'do_suffix',
  }
  if EMorEEorMM!="em":
    nuisances[js+'_DY']  = {
                'name'  : 'CMS_scale_'+js,
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp'  : js+'up',
                'mapDown'  : js+'do',
                'samples': {
                     'DY'      : ['1', '1'],
                 },
                'folderUp'   : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__recoilDY__JES'+JesDirName+'up_suffix',
                'folderDown' : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__recoilDY__JES'+JesDirName+'do_suffix',
    }

##### Jet energy resolution

nuisances['jer']  = {
                'name'  : 'CMS_res_j_2017',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp'  : 'JERup',
                'mapDown'  : 'JERdo',
                'samples': dict((skey, ['1', '1']) for skey in mc_noDYHM),
                'folderUp'   : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__JERup_suffix',
                'folderDown' : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__JERdo_suffix',
}
nuisances['jer_HM']  = {
                'name'  : 'CMS_res_j_2017',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp'  : 'JERup',
                'mapDown'  : 'JERdo',
                'samples': dict((skey, ['1', '1']) for skey in mc_HM),
                'folderUp'   : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__BWReweight__JERup_suffix',
                'folderDown' : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__BWReweight__JERdo_suffix',
}

if EMorEEorMM!="em":
  nuisances['jer_DY']  = {
                'name'  : 'CMS_res_j_2017',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp'  : 'JERup',
                'mapDown'  : 'JERdo',
                'samples': {
                     'DY'      : ['1', '1'],
                 },
                'folderUp'   : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__recoilDY__JERup_suffix',
                'folderDown' : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__recoilDY__JERdo_suffix',
  }

###### MET energy scale

nuisances['met']  = {
                'name'  : 'CMS_scale_met_2017',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp'  : 'METup',
                'mapDown'  : 'METdo',
                'samples': dict((skey, ['1', '1']) for skey in mc_noDYHM),
                'folderUp'   : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__METup_suffix',
                'folderDown' : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__METdo_suffix',
}
nuisances['met_HM']  = {
                'name'  : 'CMS_scale_met_2017',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp'  : 'METup',
                'mapDown'  : 'METdo',
                'samples': dict((skey, ['1', '1']) for skey in mc_HM),
                'folderUp'   : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__BWReweight__METup_suffix',
                'folderDown' : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__BWReweight__METdo_suffix',
}

if EMorEEorMM!="em":
  met_systs = ['MET', 'METResponse', 'METResolution']
  for ms in met_systs:
    ms_name = 'met' if ms=='MET' else ms
    nuisances[ms+'_DY']  = {
                'name'  : 'CMS_scale_'+ms_name+'_2017',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp'  : ms+'up',
                'mapDown'  : ms+'do',
                'samples': {
                     'DY'      : ['1', '1'],
                 },
                'folderUp'   : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__recoilDY__METup_suffix',
                'folderDown' : treeBaseDir+'Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7__recoilDY__METdo_suffix',
    }

# Prefire correction

nuisances['prefire']  = {
                'name'  : 'CMS_eff_prefiring_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, ['PrefireWeight_Up/PrefireWeight', 'PrefireWeight_Down/PrefireWeight']) for skey in mc),
}

# Di-Tau vetoing for embedding
if useEmbeddedDY: 
  nuisances['embedveto']  = {
                  'name'  : 'CMS_embed_veto_2017',
                  'kind'  : 'weight',
                  'type'  : 'shape',
                  'samples'  : {
                     'DYemb'    : ['1', '1'],
                     'DYveto'   : ['0.1', '-0.1'],
                  }
  }

##### PS
handle = open("../PSunc.py",'r')
exec(handle)
handle.close()

nuisances['PS_ISR']  = {
    'name': 'PS_ISR',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'VgS'    : ['1.0000536116408023*(nCleanGenJet==0) + 1.0100100693580492*(nCleanGenJet==1) + 0.959068359375*(nCleanGenJet==2) + 0.9117049260469496*(nCleanGenJet>=3)', '0.9999367833485968*(nCleanGenJet==0) + 0.9873682892005163*(nCleanGenJet==1) + 1.0492717737268518*(nCleanGenJet==2) + 1.1176958835210322*(nCleanGenJet>=3)'], # From WZTo3LNu_mllmin01
        'ggWW'   : ['1.040233912070831*(nCleanGenJet==0) + 0.9611236379290876*(nCleanGenJet==1) + 0.9014289294088699*(nCleanGenJet==2) + 0.864310738090035*(nCleanGenJet>=3)', '0.9510305474211223*(nCleanGenJet==0) + 1.0433432942960381*(nCleanGenJet==1) + 1.1271383507266095*(nCleanGenJet==2) + 1.1885756983901514*(nCleanGenJet>=3)'], # From GluGluToWWToENMN
        'WW'     : ['1.0005237869294796*(nCleanGenJet==0) + 1.0157425373134328*(nCleanGenJet==1) + 0.9644598124510606*(nCleanGenJet==2) + 0.9271488926223369*(nCleanGenJet>=3)', '0.9993553300024391*(nCleanGenJet==0) + 0.9806102300995024*(nCleanGenJet==1) + 1.042603303739856*(nCleanGenJet==2) + 1.0950369125887705*(nCleanGenJet>=3)'], # From WWTo2L2Nu
        'WWewk'   : ['1.000046239608802*(nCleanGenJet==0) + 1.0133437345113673*(nCleanGenJet==1) + 1.0144565712441801*(nCleanGenJet==2) + 0.9633224709814209*(nCleanGenJet>=3)', '0.9972924400977996*(nCleanGenJet==0) + 0.9796025428294364*(nCleanGenJet==1) + 0.9785038122896787*(nCleanGenJet==2) + 1.043894692205412*(nCleanGenJet>=3)'], # From WpWmJJ_EWK_noTop
        'qqWWqq'   : ['1.031198192*(nCleanGenJet==0) + 1.029396447*(nCleanGenJet==1) + 1.008244787*(nCleanGenJet==2) + 0.958054424*(nCleanGenJet>=3)', '0.962541517*(nCleanGenJet==0) + 0.964149647*(nCleanGenJet==1) + 0.988864503*(nCleanGenJet==2) + 1.052819668*(nCleanGenJet>=3)'], # From WpWmJJ_QCD_noTop_ext1
        'WW2J'   : ['1.031198192*(nCleanGenJet==0) + 1.029396447*(nCleanGenJet==1) + 1.008244787*(nCleanGenJet==2) + 0.958054424*(nCleanGenJet>=3)', '0.962541517*(nCleanGenJet==0) + 0.964149647*(nCleanGenJet==1) + 0.988864503*(nCleanGenJet==2) + 1.052819668*(nCleanGenJet>=3)'], # From WpWmJJ_QCD_noTop_ext1
        'top'    : ['1.0020618369910668*(nCleanGenJet==0) + 1.0063081530771556*(nCleanGenJet==1) + 1.0094298425968304*(nCleanGenJet==2) + 0.9854207999040726*(nCleanGenJet>=3)', '0.9974340279269026*(nCleanGenJet==0) + 0.9920634820709106*(nCleanGenJet==1) + 0.988226385054923*(nCleanGenJet==2) + 1.017968568319235*(nCleanGenJet>=3)'], # From TTTo2L2Nu
        'DY'     : ['0.9998177685645392*(nCleanGenJet==0) + 1.0080838149428026*(nCleanGenJet==1) + 1.0057948912950987*(nCleanGenJet==2) + 0.9721358221196619*(nCleanGenJet>=3)', '1.0003244155266309*(nCleanGenJet==0) + 0.9897992135367016*(nCleanGenJet==1) + 0.9928782069009531*(nCleanGenJet==2) + 1.0348902921423981*(nCleanGenJet>=3)'], # From DYJetsToTT_MuEle_M-50
        'VVV'    : ['1.0270826786253018*(nCleanGenJet==0) + 1.0198703447307862*(nCleanGenJet==1) + 1.0109191915514344*(nCleanGenJet==2) + 0.9838184220287978*(nCleanGenJet>=3)', '0.9661665482954546*(nCleanGenJet==0) + 0.9751744967838527*(nCleanGenJet==1) + 0.9859624782745712*(nCleanGenJet==2) + 1.0202995039288625*(nCleanGenJet>=3)'], # From WWW
        'VZ'    : ['1.0005649495173758*(nCleanGenJet==0) + 1.0126108996187784*(nCleanGenJet==1) + 0.9655814439488959*(nCleanGenJet==2) + 0.9231853653899337*(nCleanGenJet>=3)', '0.9992093891493296*(nCleanGenJet==0) + 0.9843983411237471*(nCleanGenJet==1) + 1.0409271492937164*(nCleanGenJet==2) + 1.1001990664321764*(nCleanGenJet>=3)'], # From ZZTo2L2Nu_ext1
        'Vg'    : ['1.0039055667905552*(nCleanGenJet==0) + 1.0059752448648116*(nCleanGenJet==1) + 0.9926179336643974*(nCleanGenJet==2) + 0.9524471129275528*(nCleanGenJet>=3)', '0.9949355050284215*(nCleanGenJet==0) + 0.9926938538727195*(nCleanGenJet==1) + 1.0093671414600691*(nCleanGenJet==2) + 1.060578524662196*(nCleanGenJet>=3)'], # From Zg
        'ggH_hww': ['1.0007510488273352*(nCleanGenJet==0) + 1.0152476349471342*(nCleanGenJet==1) + 0.9645590929269297*(nCleanGenJet==2) + 0.9189171704206691*(nCleanGenJet>=3)', '0.9989909143752528*(nCleanGenJet==0) + 0.9814978813068076*(nCleanGenJet==1) + 1.0416554335980368*(nCleanGenJet==2) + 1.1060543963750413*(nCleanGenJet>=3)'], # From GluGluHToWWTo2L2NuPowheg_M125
        'qqH_hww': ['1.0008858084852863*(nCleanGenJet==0) + 1.001293920824975*(nCleanGenJet==1) + 1.0013304143711548*(nCleanGenJet==2) + 0.9875473532521144*(nCleanGenJet>=3)', '0.9987483211480337*(nCleanGenJet==0) + 0.9982952329209852*(nCleanGenJet==1) + 0.9983076740658964*(nCleanGenJet==2) + 1.016023412328836*(nCleanGenJet>=3)'], # From VBFHToWWTo2L2Nu_M125
        'WH_hww' : ['1.0006979353025824*(nCleanGenJet==0) + 1.0014529360558138*(nCleanGenJet==1) + 1.0007920644457673*(nCleanGenJet==2) + 0.996814275350521*(nCleanGenJet>=3)', '0.9990367459746422*(nCleanGenJet==0) + 0.9980712824836634*(nCleanGenJet==1) + 0.9989875513096169*(nCleanGenJet==2) + 1.0039628146069568*(nCleanGenJet>=3)'], # From HWplusJ_HToWW_M125
        'ZH_hww' : ['1.0008198940532742*(nCleanGenJet==0) + 1.001574300159756*(nCleanGenJet==1) + 1.0014892423703352*(nCleanGenJet==2) + 0.9982835923429388*(nCleanGenJet>=3)', '0.9991322211949244*(nCleanGenJet==0) + 0.9979828392772856*(nCleanGenJet==1) + 0.9980190791034156*(nCleanGenJet==2) + 1.0021025907582017*(nCleanGenJet>=3)'], # From HZJ_HToWW_M125
        'ggH_htt' : ['1.0009206232135992*(nCleanGenJet==0) + 1.0169049400184142*(nCleanGenJet==1) + 0.9651882268657965*(nCleanGenJet==2) + 0.9207705642435241*(nCleanGenJet>=3)', '0.9987561139828172*(nCleanGenJet==0) + 0.9794201864664572*(nCleanGenJet==1) + 1.0412120487156962*(nCleanGenJet==2) + 1.1029538166275263*(nCleanGenJet>=3)'], # From GluGluHToTauTau_M125
        'qqH_htt' : ['1.0015936666002356*(nCleanGenJet==0) + 1.0009069467125817*(nCleanGenJet==1) + 1.0013415884915544*(nCleanGenJet==2) + 0.9899575000578329*(nCleanGenJet>=3)', '0.9977688532207473*(nCleanGenJet==0) + 0.9987106379579664*(nCleanGenJet==1) + 0.9982730482948471*(nCleanGenJet==2) + 1.0129212222112982*(nCleanGenJet>=3)'], # From VBFHToTauTau_M125
        'ZH_htt' : ['1.0011046590284958*(nCleanGenJet==0) + 1.0009827081230018*(nCleanGenJet==1) + 1.0014051098703878*(nCleanGenJet==2) + 0.9922466090234346*(nCleanGenJet>=3)', '0.9985385006421232*(nCleanGenJet==0) + 0.9987921714622244*(nCleanGenJet==1) + 0.9980838293358115*(nCleanGenJet==2) + 1.009751444450435*(nCleanGenJet>=3)'], # From HZJ_HToTauTau_M125
        'WH_htt' : ['1.000668369771863*(nCleanGenJet==0) + 1.0016815623453736*(nCleanGenJet==1) + 1.0013707389683542*(nCleanGenJet==2) + 0.9915138785231363*(nCleanGenJet>=3)', '0.9991668459690679*(nCleanGenJet==0) + 0.9978760956386513*(nCleanGenJet==1) + 0.9981171739879867*(nCleanGenJet==2) + 1.0105488300114145*(nCleanGenJet>=3)'], # From HWplusJ_HToTauTau_M125
    },
}
# PS Weight exist only for WW and ggWW (also ggH400,750; VBF250,400,750), and also some Top samples but no all
for alpha in ["WW", "ggWW"]:
  nuisances['PS_ISR']['samples'].update({alpha: ['Alt$(PSWeight[2], 1.0)', 'Alt$(PSWeight[0], 1.0)']}) # Alt$ needed to check for presence of weight later in SBI
for model in models:
  model_name = '_'+model.replace(".","")
  for m in massggh:
    PSup = PSunc['GGF'+m]['ISRup']
    PSdn = PSunc['GGF'+m]['ISRdn']
    PSstring = [str(PSup['0j'])+'*(nCleanGenJet==0) + '+str(PSup['1j'])+'*(nCleanGenJet==1) + '+str(PSup['2j'])+'*(nCleanGenJet==2) + '+str(PSup['3j'])+'*(nCleanGenJet>=3)', str(PSdn['0j'])+'*(nCleanGenJet==0) + '+str(PSdn['1j'])+'*(nCleanGenJet==1) + '+str(PSdn['2j'])+'*(nCleanGenJet==2) + '+str(PSdn['3j'])+'*(nCleanGenJet>=3)']
    nuisances['PS_ISR']['samples'].update({'GGH_'+m+model_name: PSstring})
    nuisances['PS_ISR']['samples'].update({'GGHINT_'+m+model_name: PSstring}) # Here and in the following: Don't put nuisances here for SBI; they're added automatically in a later step!
  for m in massvbf:
    PSup = PSunc['VBF'+m]['ISRup']
    PSdn = PSunc['VBF'+m]['ISRdn']
    PSstring = [str(PSup['0j'])+'*(nCleanGenJet==0) + '+str(PSup['1j'])+'*(nCleanGenJet==1) + '+str(PSup['2j'])+'*(nCleanGenJet==2) + '+str(PSup['3j'])+'*(nCleanGenJet>=3)', str(PSdn['0j'])+'*(nCleanGenJet==0) + '+str(PSdn['1j'])+'*(nCleanGenJet==1) + '+str(PSdn['2j'])+'*(nCleanGenJet==2) + '+str(PSdn['3j'])+'*(nCleanGenJet>=3)']
    nuisances['PS_ISR']['samples'].update({'QQH_'+m+model_name: PSstring})
    nuisances['PS_ISR']['samples'].update({'QQHINT_'+m+model_name: PSstring})

nuisances['PS_FSR']  = {
    'name': 'PS_FSR',
    'kind': 'weight',
    'type': 'shape',
    'samples': { 
        'VgS'    : ['0.9976593177227735*(nCleanGenJet==0) + 1.0016125187585532*(nCleanGenJet==1) + 1.0049344618055556*(nCleanGenJet==2) + 1.0195631514301164*(nCleanGenJet>=3)', '1.0026951855766457*(nCleanGenJet==0) + 1.0008132148661049*(nCleanGenJet==1) + 1.003949291087963*(nCleanGenJet==2) + 0.9708160910230832*(nCleanGenJet>=3)'],
        'ggWW'   : ['0.9910563426395067*(nCleanGenJet==0) + 1.0069894351287263*(nCleanGenJet==1) + 1.016616376034912*(nCleanGenJet==2) + 1.015902717074592*(nCleanGenJet>=3)', '1.0147395976461193*(nCleanGenJet==0) + 0.9860219489006646*(nCleanGenJet==1) + 0.9694680606617647*(nCleanGenJet==2) + 0.9489845115821678*(nCleanGenJet>=3)'],
        'WW'     : ['0.995462478372054*(nCleanGenJet==0) + 1.0052129975124378*(nCleanGenJet==1) + 1.008836750560578*(nCleanGenJet==2) + 0.9984120564941189*(nCleanGenJet>=3)', '1.008927720738437*(nCleanGenJet==0) + 0.995163868159204*(nCleanGenJet==1) + 0.9911024228315418*(nCleanGenJet==2) + 0.9763787172658678*(nCleanGenJet>=3)'],
        'WWewk'   : ['0.9919173789731052*(nCleanGenJet==0) + 0.994273375713824*(nCleanGenJet==1) + 1.0009783801226202*(nCleanGenJet==2) + 1.0046943184676753*(nCleanGenJet>=3)', '1.0081780733496333*(nCleanGenJet==0) + 1.0052172826204072*(nCleanGenJet==1) + 0.9984786981975752*(nCleanGenJet==2) + 0.9881601609947174*(nCleanGenJet>=3)'],
        'qqWWqq'   : ['0.976538004*(nCleanGenJet==0) + 0.993524816*(nCleanGenJet==1) + 1.006678783*(nCleanGenJet==2) + 1.009760965*(nCleanGenJet>=3)', '1.035661107*(nCleanGenJet==0) + 1.007585153*(nCleanGenJet==1) + 0.989764669*(nCleanGenJet==2) + 0.98276492*(nCleanGenJet>=3)'],
        'WW2J'   : ['0.976538004*(nCleanGenJet==0) + 0.993524816*(nCleanGenJet==1) + 1.006678783*(nCleanGenJet==2) + 1.009760965*(nCleanGenJet>=3)', '1.035661107*(nCleanGenJet==0) + 1.007585153*(nCleanGenJet==1) + 0.989764669*(nCleanGenJet==2) + 0.98276492*(nCleanGenJet>=3)'],
        'top'    : ['0.9910899786333963*(nCleanGenJet==0) + 0.9990635702054794*(nCleanGenJet==1) + 1.002141744200183*(nCleanGenJet==2) + 1.0129742776372779*(nCleanGenJet>=3)', '1.0068843378231833*(nCleanGenJet==0) + 0.998988498438759*(nCleanGenJet==1) + 0.9952696584115224*(nCleanGenJet==2) + 0.9790955840673237*(nCleanGenJet>=3)'],
        'DY'     : ['0.9958763409773141*(nCleanGenJet==0) + 1.0041335498093422*(nCleanGenJet==1) + 1.0163363150953029*(nCleanGenJet==2) + 1.0296733670670226*(nCleanGenJet>=3)', '1.0066775262249232*(nCleanGenJet==0) + 0.9945601465681602*(nCleanGenJet==1) + 0.9662459619335311*(nCleanGenJet==2) + 0.9479423453563661*(nCleanGenJet>=3)'],
        'VVV'    : ['0.9809047855490748*(nCleanGenJet==0) + 0.9823641498350338*(nCleanGenJet==1) + 0.9976414629808243*(nCleanGenJet==2) + 1.0077953569413387*(nCleanGenJet>=3)', '1.035388723727876*(nCleanGenJet==0) + 1.0347339790465233*(nCleanGenJet==1) + 1.0017058788771533*(nCleanGenJet==2) + 0.9829344116371653*(nCleanGenJet>=3)'],
        'VZ'    : ['0.9969613063607379*(nCleanGenJet==0) + 1.0055822932729375*(nCleanGenJet==1) + 1.0115617769727228*(nCleanGenJet==2) + 1.003930218451846*(nCleanGenJet>=3)', '1.0044825167062181*(nCleanGenJet==0) + 0.9934087678296067*(nCleanGenJet==1) + 0.9816200440919792*(nCleanGenJet==2) + 0.9733590995315957*(nCleanGenJet>=3)'],
        'Vg'    : ['0.9981385958679493*(nCleanGenJet==0) + 1.000785005516636*(nCleanGenJet==1) + 1.0072453356787239*(nCleanGenJet==2) + 1.016190506425758*(nCleanGenJet>=3)', '1.0032725732400525*(nCleanGenJet==0) + 1.0019489593245505*(nCleanGenJet==1) + 0.986995604774182*(nCleanGenJet==2) + 0.9629840158493718*(nCleanGenJet>=3)'],
        'ggH_hww': ['0.9936588910230489*(nCleanGenJet==0) + 1.0087564198432573*(nCleanGenJet==1) + 1.014636529653396*(nCleanGenJet==2) + 1.00399261707105*(nCleanGenJet>=3)','1.0125063182369591*(nCleanGenJet==0) + 0.9846168672324244*(nCleanGenJet==1) + 0.9778204449152542*(nCleanGenJet==2) + 1.0014057292097962*(nCleanGenJet>=3)'],
        'qqH_hww': ['0.9902864012471768*(nCleanGenJet==0) + 0.9950165165635796*(nCleanGenJet==1) + 1.0024778632714528*(nCleanGenJet==2) + 1.0132965690130387*(nCleanGenJet>=3)', '1.0171041801597582*(nCleanGenJet==0) + 1.0088822239287307*(nCleanGenJet==1) + 0.9946938338710369*(nCleanGenJet==2) + 0.9782409053438381*(nCleanGenJet>=3)'],
        'WH_hww' : ['0.9864466858859676*(nCleanGenJet==0) + 0.9911412676207558*(nCleanGenJet==1) + 1.0047988929561447*(nCleanGenJet==2) + 1.0135375714689319*(nCleanGenJet>=3)', '1.022768308571873*(nCleanGenJet==0) + 1.0147067259919833*(nCleanGenJet==1) + 0.9932121652658327*(nCleanGenJet==2) + 0.9807301742549035*(nCleanGenJet>=3)'],
        'ZH_hww' : ['0.98702584755388*(nCleanGenJet==0) + 0.9881328970299905*(nCleanGenJet==1) + 1.0046199525397077*(nCleanGenJet==2) + 1.0091561054313662*(nCleanGenJet>=3)', '1.0236225630459734*(nCleanGenJet==0) + 1.0213677207764504*(nCleanGenJet==1) + 0.9933149152918336*(nCleanGenJet==2) + 0.978832627595614*(nCleanGenJet>=3)'],
        'ggH_htt' : ['0.9943019952320858*(nCleanGenJet==0) + 1.0083325858201546*(nCleanGenJet==1) + 1.0201886103441544*(nCleanGenJet==2) + 0.9998286915341232*(nCleanGenJet>=3)', '1.0109237494149799*(nCleanGenJet==0) + 0.9873094123474508*(nCleanGenJet==1) + 0.9675289700468541*(nCleanGenJet==2) + 0.99986531610269*(nCleanGenJet>=3)'],
        'qqH_htt' : ['0.9902403321260225*(nCleanGenJet==0) + 0.996767386750923*(nCleanGenJet==1) + 1.0040574219585203*(nCleanGenJet==2) + 1.0124888310238733*(nCleanGenJet>=3)', '1.0139721006126092*(nCleanGenJet==0) + 1.002858740414655*(nCleanGenJet==1) + 0.9961014338785547*(nCleanGenJet==2) + 0.978061636844175*(nCleanGenJet>=3)'],
        'ZH_htt' : ['0.9936708956610235*(nCleanGenJet==0) + 0.9954883239735823*(nCleanGenJet==1) + 1.0074327384991346*(nCleanGenJet==2) + 1.0068065233897634*(nCleanGenJet>=3)', '1.0106252599791612*(nCleanGenJet==0) + 1.0109967871866061*(nCleanGenJet==1) + 0.9941765805699787*(nCleanGenJet==2) + 0.9967875439175832*(nCleanGenJet>=3)'],
        'WH_htt' : ['0.9951849276795807*(nCleanGenJet==0) + 0.9971109709655758*(nCleanGenJet==1) + 1.0089023169085682*(nCleanGenJet==2) + 1.0177364980737993*(nCleanGenJet>=3)', '1.0080916898956942*(nCleanGenJet==0) + 1.003439195368276*(nCleanGenJet==1) + 0.9870860759068387*(nCleanGenJet==2) + 0.9778888209017473*(nCleanGenJet>=3)'],
    },
}
for alpha in ["WW", "ggWW"]:
  nuisances['PS_FSR']['samples'].update({alpha: ['Alt$(PSWeight[3], 1.0)', 'Alt$(PSWeight[1], 1.0)']}) # Alt$ needed to check for presence of weight later in SBI
for model in models:
  model_name = '_'+model.replace(".","")
  for m in massggh:
    PSup = PSunc['GGF'+m]['FSRup']
    PSdn = PSunc['GGF'+m]['FSRdn']
    PSstring = [str(PSup['0j'])+'*(nCleanGenJet==0) + '+str(PSup['1j'])+'*(nCleanGenJet==1) + '+str(PSup['2j'])+'*(nCleanGenJet==2) + '+str(PSup['3j'])+'*(nCleanGenJet>=3)', str(PSdn['0j'])+'*(nCleanGenJet==0) + '+str(PSdn['1j'])+'*(nCleanGenJet==1) + '+str(PSdn['2j'])+'*(nCleanGenJet==2) + '+str(PSdn['3j'])+'*(nCleanGenJet>=3)']
    nuisances['PS_FSR']['samples'].update({'GGH_'+m+model_name: PSstring})
    nuisances['PS_FSR']['samples'].update({'GGHINT_'+m+model_name: PSstring})
  for m in massvbf:
    PSup = PSunc['VBF'+m]['FSRup']
    PSdn = PSunc['VBF'+m]['FSRdn']
    PSstring = [str(PSup['0j'])+'*(nCleanGenJet==0) + '+str(PSup['1j'])+'*(nCleanGenJet==1) + '+str(PSup['2j'])+'*(nCleanGenJet==2) + '+str(PSup['3j'])+'*(nCleanGenJet>=3)', str(PSdn['0j'])+'*(nCleanGenJet==0) + '+str(PSdn['1j'])+'*(nCleanGenJet==1) + '+str(PSdn['2j'])+'*(nCleanGenJet==2) + '+str(PSdn['3j'])+'*(nCleanGenJet>=3)']
    nuisances['PS_FSR']['samples'].update({'QQH_'+m+model_name: PSstring})
    nuisances['PS_FSR']['samples'].update({'QQHINT_'+m+model_name: PSstring})

# Uncorrelate important backgrounds
for proc in ['DY', 'top', 'WW']:
  nuisances['PS_ISR_'+proc]  = {
    'name': 'PS_ISR_'+proc,
    'kind': 'weight',
    'type': 'shape',
    'samples': {
      proc: nuisances['PS_ISR']['samples'][proc],
    }
  }
  del nuisances['PS_ISR']['samples'][proc]

  nuisances['PS_FSR_'+proc]  = {
    'name': 'PS_FSR_'+proc,
    'kind': 'weight',
    'type': 'shape',
    'samples': {
      proc: nuisances['PS_FSR']['samples'][proc],
    }
  }
  del nuisances['PS_FSR']['samples'][proc]

##### UE
# An overall 1.5% UE uncertainty will cover all the UEup/UEdo variations
# And we don't observe any dependency of UE variations on njet
nuisances['UE']  = {
                'name'  : 'UE_CP5',
                'skipCMS' : 1,
                'type': 'lnN',
                'samples': dict((skey, '1.015') for skey in mc), 
}

##### PU
nuisances['PU']  = {
                'name'  : 'CMS_PU_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                  'DY': ['0.993259983266*(puWeightUp/puWeight)', '0.997656381501*(puWeightDown/puWeight)'],
                  'top': ['1.00331969187*(puWeightUp/puWeight)', '0.999199609528*(puWeightDown/puWeight)'],
                  'WW': ['1.0033022059*(puWeightUp/puWeight)', '0.997085330608*(puWeightDown/puWeight)'],
                  'ggH_hww': ['1.0036768006*(puWeightUp/puWeight)', '0.995996570285*(puWeightDown/puWeight)'],
                  'qqH_hww': ['1.00374694528*(puWeightUp/puWeight)', '0.995878596852*(puWeightDown/puWeight)'],
                },
                'AsLnN'      : '1'
}

handle = open("../PUunc.py",'r')
exec(handle)
handle.close()

for model in models:
  model_name = '_'+model.replace(".","")
  for m in massggh:
    PUup = PUunc['GGF'+m]['Up']
    PUdn = PUunc['GGF'+m]['Down']
    PUstring = [str(PUup)+'*(puWeightUp/puWeight)', str(PUdn)+'*(puWeightDown/puWeight)']
    nuisances['PU']['samples'].update({'GGH_'+m+model_name: PUstring})
    nuisances['PU']['samples'].update({'GGHINT_'+m+model_name: PUstring})
  for m in massvbf:
    PUup = PUunc['VBF'+m]['Up']
    PUdn = PUunc['VBF'+m]['Down']
    PUstring = [str(PUup)+'*(puWeightUp/puWeight)', str(PUdn)+'*(puWeightDown/puWeight)']
    nuisances['PU']['samples'].update({'QQH_'+m+model_name: PUstring})
    nuisances['PU']['samples'].update({'QQHINT_'+m+model_name: PUstring})


### PU ID SF uncertainty
puid_syst = ['Jet_PUIDSF_up/Jet_PUIDSF', 'Jet_PUIDSF_down/Jet_PUIDSF']

nuisances['jetPUID'] = {
    'name': 'CMS_PUID_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, puid_syst) for skey in mc)
}


# QCD scale uncertainties

nuisances['QCDscale_ggH']  = {
               'name'  : 'QCDscale_ggH', 
               'samples'  : {
                   'ggH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH','125.09','scale','sm'),
                   'ggH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH','125.09','scale','sm'),
                   },
               'type'  : 'lnN',
              }

'''
# StuartTackmann; for use when considering njet ggF categories

nuisances['QCDscale0in']  = {
               'name'  : 'QCDscale_ggH0in', 
               'kind'  : 'weight',
               'type'  : 'shape',
               'samples'  : {},
               'cuts'  : [cut for cut in cuts if "0j" in cut]
              }
for m in massggh:
  STUnc0j = 1.12469-4.78587e-05*int(m)+1.52249e-07*int(m)*int(m) - 1.0
  STweight = '('+str(STUnc0j)+'*(njet0 && !VBFcut_NEW))'
  STUncString = ['1.0 + '+STweight, '1.0 / ( 1.0 + '+STweight+' )']
  nuisances['QCDscale0in']['samples'].update({'GGH_'+m+model_name: STUncString})
  nuisances['QCDscale0in']['samples'].update({'GGHINT_'+m+model_name: STUncString})

nuisances['QCDscale1in']  = {
               'name'  : 'QCDscale_ggH1in', 
               'kind'  : 'weight',
               'type'  : 'shape',
               'samples'  : {},
               'cuts'  : [cut for cut in cuts if ("0j" in cut or "1j" in cut)]
              }
for m in massggh:
  STUnc0j = math.exp(-0.00235424-0.000573266*int(m)) - 1.0
  STUnc1j = math.exp(0.245872+1.21053e-05*int(m)+1.85399e-09*int(m)*int(m)) - 1.0
  STweight = '('+str(STUnc0j)+'*(njet0 && !VBFcut_NEW)) + ('+str(STUnc1j)+'*(njet1 && !VBFcut_NEW))'
  STUncString = ['1.0 + '+STweight, '1.0 / ( 1.0 + '+STweight+' )']
  nuisances['QCDscale1in']['samples'].update({'GGH_'+m+model_name: STUncString})
  nuisances['QCDscale1in']['samples'].update({'GGHINT_'+m+model_name: STUncString})

nuisances['QCDscale2in']  = {
               'name'  : 'QCDscale_ggH2in', 
               'kind'  : 'weight',
               'type'  : 'shape',
               'samples'  : {},
               'cuts'  : [cut for cut in cuts if ("1j" in cut or "2j" in cut)]
              }
for m in massggh:
  STUnc1j = math.exp(-0.141665-0.000186944*int(m)+2.57673e-08*int(m)*int(m)) - 1.0
  STUnc2j = math.exp(0.497326+1.47493e-05*int(m)+1.4044e-09*int(m)*int(m)+6.79881/(-0.00319659+int(m))) - 1.0
  STweight = '('+str(STUnc1j)+'*(njet1 && !VBFcut_NEW)) + ('+str(STUnc2j)+'*(njet2 && !VBFcut_NEW))'
  STUncString = ['1.0 + '+STweight, '1.0 / ( 1.0 + '+STweight+' )']
  nuisances['QCDscale2in']['samples'].update({'GGH_'+m+model_name: STUncString})
  nuisances['QCDscale2in']['samples'].update({'GGHINT_'+m+model_name: STUncString})

nuisances['QCDscale3in']  = {
               'name'  : 'QCDscale_ggH3in', 
               'kind'  : 'weight',
               'type'  : 'shape',
               'samples'  : {},
               'cuts'  : [cut for cut in cuts if ("2j" in cut or "vbf" in cut)]
              }
for m in massggh:
  STUnc2j = math.exp(-0.0629982-8.84461e-06*int(m)+1.02891e-09*int(m)*int(m)-1.14474/(-1.36611+int(m))) - 1.0
  STUncvbf = math.exp(0.435135+8.7163e-06*int(m)+1.48726e-09*int(m)*int(m)+17.2495/(46.1967+int(m))) - 1.0
  STweight = '('+str(STUnc2j)+'*(njet2 && !VBFcut_NEW)) + ('+str(STUncvbf)+'*(VBFcut_NEW))'
  STUncString = ['1.0 + '+STweight, '1.0 / ( 1.0 + '+STweight+' )']
  nuisances['QCDscale3in']['samples'].update({'GGH_'+m+model_name: STUncString})
  nuisances['QCDscale3in']['samples'].update({'GGHINT_'+m+model_name: STUncString})
'''

# for combined ggF category:
for model in models:
  model_name = '_'+model.replace(".","")
  for m in massggh:
    nuisances['QCDscale_ggH']['samples'].update({'GGH_'+m+model_name: HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH',int(m),'scale','bsm')})
    nuisances['QCDscale_ggH']['samples'].update({'GGHINT_'+m+model_name: HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH',int(m),'scale','bsm')})


nuisances['QCDscale_qqH']  = {
               'name'  : 'QCDscale_qqH', 
               'samples'  : {
                   'qqH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','scale','sm'),
                   'qqH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','scale','sm'),
                   },
               'type'  : 'lnN',
              }

for model in models:
  model_name = '_'+model.replace(".","")
  for m in massvbf:
    nuisances['QCDscale_qqH']['samples'].update({'QQH_'+m+model_name: HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH',int(m),'scale','bsm')})
    nuisances['QCDscale_qqH']['samples'].update({'QQHINT_'+m+model_name: HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH',int(m),'scale','bsm')})


nuisances['QCDscale_VH']  = {
               'name'  : 'QCDscale_VH', 
               'samples'  : {
                   'WH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','scale','sm'),
                   'WH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','scale','sm'),
                   'ZH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','scale','sm'),
                   'ZH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','scale','sm'),
                   },
               'type'  : 'lnN',
              }

nuisances['QCDscale_ggH_ACCEPT']  = {
               'name'  : 'QCDscale_ggH_ACCEPT',
               'samples'  : {
                   'ggH_hww'    : '1.012',
                   'ggH_htt'    : '1.012',
                   'ggWW'       : '1.012',
                   },
               'type'  : 'lnN',
              }

for model in models:
  model_name = '_'+model.replace(".","")
  for m in massggh:
    scalegg_weight = 1.0 + (-5.53622e-02+6.73342e-05*int(m)+2.55597e+01/(int(m)-1.10009e+02))/100.0
    nuisances['QCDscale_ggH_ACCEPT']['samples'].update({'GGH_'+m+model_name: str(scalegg_weight)})
    nuisances['QCDscale_ggH_ACCEPT']['samples'].update({'GGHINT_'+m+model_name: str(scalegg_weight)})

nuisances['QCDscale_qqH_ACCEPT']  = {
               'name'  : 'QCDscale_qqH_ACCEPT',
               'samples'  : {
                   'qqH_hww'   : '1.003',
                   'qqH_htt'   : '1.003',
                   'qqWWqq'    : '1.003',
                   },
               'type'  : 'lnN',
              }

for model in models:
  model_name = '_'+model.replace(".","")
  for m in massvbf:
    scaleqq_weight = 1.0 + (4.54513e-02+3.01227e-06*int(m)+4.72447/(int(m)-9.97821e+01))/100.0
    nuisances['QCDscale_qqH_ACCEPT']['samples'].update({'QQH_'+m+model_name: str(scaleqq_weight)})
    nuisances['QCDscale_qqH_ACCEPT']['samples'].update({'QQHINT_'+m+model_name: str(scaleqq_weight)})

nuisances['QCDscale_VH_ACCEPT']  = {
               'name'  : 'QCDscale_VH_ACCEPT',
               'samples'  : {
                   'WH_hww'    : '1.010',
                   'WH_htt'    : '1.010',
                   'ZH_hww'    : '1.015',
                   'ZH_htt'    : '1.015',
                   },
               'type'  : 'lnN',
              }

# Different DY samples have different contents in the LHEScaleWeight branch!
# 2017:
#if EMorEEorMM=="em": #DYJetsToTT_MuEle_M-50
#  variations = ['LHEScaleWeight[%d]' % i for i in [0, 1, 3, 4, 6, 7]]
#else: #DYJetsToLL_M-50_ext1
#  variations = ['LHEScaleWeight[%d]' % i for i in [0, 1, 3, 5, 7, 8]]
variations = ['LHEScaleWeight[0]', 'LHEScaleWeight[1]', 'LHEScaleWeight[3]', 'LHEScaleWeight[Length$(LHEScaleWeight)-4]', 'LHEScaleWeight[Length$(LHEScaleWeight)-2]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']

# Normalize DY QCD scale -> Norm fixed by rateParam
#dynorms = {"0j": [1.0143332141114483, 0.9622267969241384, 1.0596025134712872, 0.9578457318872, 1.0375774843211096, 0.9908643255041172], "1j": [0.9940901483227454, 0.962059334214635, 1.0372868838613174, 0.9760921051451452, 1.0374644279865524, 1.0106741032623678], "2j": [0.9368854613228692, 0.9418295497969644, 0.9975194312894655, 1.0116251740594764, 1.0547144137430688, 1.0652386252175967]}
#for i,alpha in enumerate(dyvars):
#  dyvars[i] = alpha+"*((Alt$(CleanJet_pt[0], 0) < 30.)*"+str(dynorms["0j"][i])+" + (Alt$(CleanJet_pt[0], 0) >= 30.)*(Alt$(CleanJet_pt[1], 0) < 30.)*"+str(dynorms["1j"][i])+" + (Alt$(CleanJet_pt[1], 0) >= 30.)*"+str(dynorms["2j"][i])+")"

#dyvars = copy.deepcopy(variations) # For envelope
dyvars = ['LHEScaleWeight[0]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']
nuisances['QCDscale_V']  = {
                'name'  : 'QCDscale_V',
                'skipCMS' : 1,
                'kind'  : 'weight', #_envelope
                'type'  : 'shape',
                'samples'  : {
                   'DY' : dyvars,
                }
}

# Variations for all other samples are consistent.
variations = ['LHEScaleWeight[%d]' % i for i in [0, 1, 3, 5, 7, 8]]

# Normalize WW2J QCD scale -> Norm fixed by rateParam
wwvars = copy.deepcopy(variations)
#wwnorms = {"0j": [0.84383798548*0.933914610874, 0.86466427431*0.932663376857, 0.977964460303*0.999117815167, 1.03009229354*0.997491221906, 1.12456205702*1.07873927178, 1.15566989975*1.07866520474], "1j": [0.85278874621*0.921935869033, 0.883223267365*0.925374783012, 0.969327769019*0.99214009209, 1.03727097531*1.00395526094, 1.10369198376*1.08708105209, 1.14089855114*1.0953294986], "2j": [0.875280127959*0.892065330728, 0.907932347707*0.906435582251, 0.969825671359*0.978014691868, 1.03579782256*1.01735870242, 1.07835570337*1.10633174958, 1.11156964411*1.1311995478]}
#for i,alpha in enumerate(wwvars):
#  wwvars[i] = alpha+"*((Alt$(CleanJet_pt[0], 0) < 30.)*"+str(wwnorms["0j"][i])+" + (Alt$(CleanJet_pt[0], 0) >= 30.)*(Alt$(CleanJet_pt[1], 0) < 30.)*"+str(wwnorms["1j"][i])+" + (Alt$(CleanJet_pt[1], 0) >= 30.)*"+str(wwnorms["2j"][i])+")"
nuisances['QCDscale_WWJJ']  = {
                'name'  : 'QCDscale_VV',
                'skipCMS' : 1,
                'kind'  : 'weight_envelope',
                'type'  : 'shape',
                'samples'  : {
                   'qqWWqq' : variations,
                   'WW2J' : wwvars,
                }
}

nuisances['QCDscale_VV']  = {
                'name'  : 'QCDscale_VV', 
                'skipCMS' : 1,
                'kind'  : 'weight_envelope',
                'type'  : 'shape',
                'samples'  : {
                   'Vg' : variations,
                   'VZ' : variations,
                   'VgS' : variations,
                   }
}

# Normalize top QCD scale -> Norm fixed by rateParam
#topnorms = {"0j": [1.070761703863844, 1.0721982065714528, 1.0008829637654995, 1.002515087891841, 0.9270080603942781, 0.9270717138194097], "1j": [1.0846741444664376, 1.0806432359691847, 1.0079221754798773, 0.9960603215169435, 0.9198946095840594, 0.9129672863490275], "2j": [1.1209941307567444, 1.103222357530683, 1.0224795274718796, 0.9829374807746288, 0.9038880068177306, 0.8840173265167147]}
#for i,alpha in enumerate(topvars):
#  topvars[i] = alpha+"*((Alt$(CleanJet_pt[0], 0) < 30.)/"+str(topnorms["0j"][i])+" + (Alt$(CleanJet_pt[0], 0) >= 30.)*(Alt$(CleanJet_pt[1], 0) < 30.)/"+str(topnorms["1j"][i])+" + (Alt$(CleanJet_pt[1], 0) >= 30.)/"+str(topnorms["2j"][i])+")"

#topvars = copy.deepcopy(variations) # For envelope
topvars = ['LHEScaleWeight[0]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']
nuisances['QCDscale_ttbar']  = {
               'name'  : 'QCDscale_ttbar', 
                'skipCMS' : 1,
                'kind'  : 'weight', #_envelope
                'type'  : 'shape',
                'samples'  : {
                   'top' : topvars,
                   }
}

# Scale uncertainties not needed:
# WW: Special scale/resum uncertainties below
# VVV: Negligible

nuisances['QCDscale_WWewk']  = {
               'name'  : 'QCDscale_VV',
               'samples'  : {
                   'WWewk' : '1.11',
                   },
               'type'  : 'lnN'
              }

# No LHEScaleWeight entries here, not sure where 15% comes from
nuisances['QCDscale_ggVV']  = {
               'name'  : 'QCDscale_ggVV',
               'type'  : 'lnN',
               'samples'  : {
                   'ggWW' : '1.15',
                   },
              }

# PDF uncertainties
nuisances['pdf_Higgs_gg']  = {
               'name'  : 'pdf_Higgs_gg',
               'samples'  : {
                   #'ggWW'    : '1.05',    # --> no, since absorbed into k-scale factor
                   'ggH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH' ,'125.09','pdf','sm'),
                   'ggH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH' ,'125.09','pdf','sm'),
                   },
               'type'  : 'lnN',
              }
for model in models:
  model_name = '_'+model.replace(".","")
  for m in massggh:
    nuisances['pdf_Higgs_gg']['samples'].update({'GGH_'+m+model_name: HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH',int(m),'pdf','bsm')})
    nuisances['pdf_Higgs_gg']['samples'].update({'GGHINT_'+m+model_name: HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH',int(m),'pdf','bsm')})


nuisances['pdf_Higgs_qqbar']  = {
               'name'  : 'pdf_Higgs_qqbar',
               'type'  : 'lnN',
               'samples'  : {
                   'qqH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm'),
                   'qqH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm'),
                   'WH_hww'  : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH' ,'125.09','pdf','sm'),
                   'WH_htt'  : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH' ,'125.09','pdf','sm'),
                   'ZH_hww'  : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH' ,'125.09','pdf','sm'),
                   'ZH_htt'  : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH' ,'125.09','pdf','sm'),
                   },
              }
for model in models:
  model_name = '_'+model.replace(".","")
  for m in massvbf:
    nuisances['pdf_Higgs_qqbar']['samples'].update({'QQH_'+m+model_name:HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH',int(m),'pdf','bsm')})
    nuisances['pdf_Higgs_qqbar']['samples'].update({'QQHINT_'+m+model_name:HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH',int(m),'pdf','bsm')})

# PDF uncertainties not needed:
# Top, DY, WW, WW2J: Taken into account in rateParam, since these are all lnN anyway

# PDF for background: https://twiki.cern.ch/twiki/bin/view/CMS/StandardModelCrossSectionsat13TeV and https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns

# W+W-: 0.0589 / 1.2804 = 0.046001
# ZW+: 0.0064 / 0.1427 = 0.0448493
# ZW-: 0.0039 / 0.0921 = 0.0423453
# ZZ:  0.0027 / 0.0719 = 0.0375522
# DY: 14.78 / 6077.22 = 0.0024320
nuisances['pdf_gg']  = {
               'name'  : 'pdf_gg',
               'type'  : 'lnN',
               'samples'  : {
                   'ggWW'    : '1.05',
                   'WWewk'    : '1.05',
                   },
              }

nuisances['pdf_qqbar']  = {
               'name'  : 'pdf_qqbar',
               'type'  : 'lnN',
               'samples'  : {
                   'Vg'      : '1.04',
                   'VZ'      : '1.04',
                   'VgS'     : '1.04',
                   'qqWWqq'  : '1.05',
                   },
              }

for i in range(1,33):
  # LHEPdfWeight are PDF4LHC variations, while nominal is NNPDF.
  # LHEPdfWeight[i] reweights from NNPDF nominal to PDF4LHC member i
  # LHEPdfWeight[0] in particular reweights from NNPDF nominal to PDF4LHC nominal
  #pdf_variations = ["LHEPdfWeight[%d]/LHEPdfWeight[0]" %i, "1/(LHEPdfWeight[%d]/LHEPdfWeight[0])" %i ] # Float_t LHE pdf variation weights (w_var / w_nominal) for LHA IDs 91400 - 91432*
  pdf_variations = ["1.0*((abs({0})>=50) || (1.0/abs({0})>=50)) + ({0})*(abs({0})<50)*(1.0/abs({0})<50)".format('LHEPdfWeight[%d]/LHEPdfWeight[0]' %(i)), "1.0*((abs({0})>=50) || (1.0/abs({0})>=50)) + (1.0/({0}))*(abs({0})<50)*(1.0/abs({0})<50)".format('LHEPdfWeight[%d]/LHEPdfWeight[0]' %(i)) ] # There's a few events with abnormaly large weights in multiple pdfs.

  nuisances['pdf_WW_'+str(i)]  = {
    'name'  : 'pdf_WW_'+str(i)+'_2017',
    'skipCMS' : 1,
    'kind'  : 'weight',
    'type'  : 'shape',
    'samples'  : {
      'WW'   : pdf_variations,
    },
  }

  nuisances['pdf_top_'+str(i)]  = {
    'name'  : 'pdf_top_'+str(i)+'_2017',
    'skipCMS' : 1,
    'kind'  : 'weight',
    'type'  : 'shape',
    'samples'  : {
      'top'   : pdf_variations,
    },
  }

  nuisances['pdf_DY_'+str(i)]  = {
    'name'  : 'pdf_DY_'+str(i)+'_2017',
    'skipCMS' : 1,
    'kind'  : 'weight',
    'type'  : 'shape',
    'samples'  : {
      'DY'   : pdf_variations,
    },
  }


nuisances['pdf_Higgs_gg_ACCEPT']  = {
               'name'  : 'pdf_Higgs_gg_ACCEPT',
               'samples'  : {
                   'ggH_hww' : '1.006',
                   'ggH_htt' : '1.006',
                   },
               'type'  : 'lnN',
              }
for model in models:
  model_name = '_'+model.replace(".","")
  for m in massggh:
    pdfgg_weight = 1.0 + (-4.10343+1.19015e-03*int(m)-9.68156e-08*int(m)*int(m)+6.90171e+03/(int(m)+8.71935e+02)-8.94415e+05/((int(m)+4.72259e+02)*(int(m)+4.72259e+02)))/100.0
    nuisances['pdf_Higgs_gg_ACCEPT']['samples'].update({'GGH_'+m+model_name: str(pdfgg_weight)})
    nuisances['pdf_Higgs_gg_ACCEPT']['samples'].update({'GGHINT_'+m+model_name: str(pdfgg_weight)})

nuisances['pdf_Higgs_qqbar_ACCEPT']  = {
               'name'  : 'pdf_Higgs_qqbar_ACCEPT',
               'type'  : 'lnN',
               'samples'  : {
                   'qqH_hww' : '1.002',
                   'qqH_htt' : '1.002',
                   'WH_hww'  : '1.003',
                   'WH_htt'  : '1.003',
                   'ZH_hww'  : '1.002',
                   'ZH_htt'  : '1.002',
                   },
              }
for model in models:
  model_name = '_'+model.replace(".","")
  for m in massvbf:
    pdfqq_weight = 1.0 + (1.46296e-01)/100.0
    nuisances['pdf_Higgs_qqbar_ACCEPT']['samples'].update({'QQH_'+m+model_name: str(pdfqq_weight)})
    nuisances['pdf_Higgs_qqbar_ACCEPT']['samples'].update({'QQHINT_'+m+model_name: str(pdfqq_weight)})

nuisances['pdf_gg_ACCEPT']  = {
               'name'  : 'pdf_gg_ACCEPT',
               'samples'  : {
                   'ggWW'    : '1.006',
                   },
               'type'  : 'lnN',
              }

nuisances['pdf_qqbar_ACCEPT']  = {
               'name'  : 'pdf_qqbar_ACCEPT',
               'type'  : 'lnN',
               'samples'  : {
                   'qqWWqq'  : '1.001',
                   },
              }

#  - Uncertainty on SR/CR ratio

nuisances['CRSR_accept_dy'] = {
    'name': 'CMS_hww_CRSR_accept_dy',
    'type': 'lnN',
    'samples': {'DY': '1.02'},
    'cuts'  : [cut for cut in cuts if "dy" in cut]
}

nuisances['CRSR_accept_top'] = {
    'name': 'CMS_hww_CRSR_accept_top',
    'type': 'lnN',
    'samples': {'top': '1.01'},
    'cuts'  : [cut for cut in cuts if "top" in cut]
}

#  - WW shaping
nuisances['WWresum0j']  = {
                'name'  : 'CMS_hww_WWresum_0j',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
                   },
               'cuts'  : [cut for cut in cuts if "0j" in cut]
                }

nuisances['WWresum1j']  = {
                'name'  : 'CMS_hww_WWresum_1j',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
                   },
               'cuts'  : [cut for cut in cuts if "1j" in cut]
                }

nuisances['WWresum2j']  = {
                'name'  : 'CMS_hww_WWresum_2j',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
                },
               'cuts'  : [cut for cut in cuts if "2j" in cut]
                }

nuisances['WWresumggh']  = {
                'name'  : 'CMS_hww_WWresum_ggh',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
                },
               'cuts'  : [cut for cut in cuts if "ggh" in cut]
                }

nuisances['WWresumvbf']  = {
                'name'  : 'CMS_hww_WWresum_vbf',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
                },
               'cuts'  : [cut for cut in cuts if "vbf" in cut]
                }

nuisances['WWresumnotag']  = {
                'name'  : 'CMS_hww_WWresum_notag',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
                },
               'cuts'  : [cut for cut in cuts if "notag" in cut]
                }

nuisances['WWqscale0j']  = {
                'name'  : 'CMS_hww_WWqscale_0j',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
                   },
               'cuts'  : [cut for cut in cuts if "0j" in cut]
                }

nuisances['WWqscale1j']  = {
                'name'  : 'CMS_hww_WWqscale_1j',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                   'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
                   },
               'cuts'  : [cut for cut in cuts if "1j" in cut]
                }

nuisances['WWqscale2j']  = {
                'name'  : 'CMS_hww_WWqscale_2j',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
                },
                'cuts'  : [cut for cut in cuts if "2j" in cut]
                }

nuisances['WWqscaleggh']  = {
                'name'  : 'CMS_hww_WWqscale_ggh',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
                },
                'cuts'  : [cut for cut in cuts if "ggh" in cut]
                }

nuisances['WWqscalevbf']  = {
                'name'  : 'CMS_hww_WWqscale_vbf',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
                },
                'cuts'  : [cut for cut in cuts if "vbf" in cut]
                }

nuisances['WWqscalenotag']  = {
                'name'  : 'CMS_hww_WWqscale_notag',
                'skipCMS' : 1,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
                },
                'cuts'  : [cut for cut in cuts if "notag" in cut]
                }

nuisances['VgStar']  = {
               'name'  : 'CMS_hww_VgStarScale', 
               'type'  : 'lnN',
               'samples'  : {
                   'VgS_L' : '1.25',  # 0.5 / 2.0   --> k_factor = 2.0 +/- 0.5
                   },
                }
 
nuisances['VZ'] = {
               'name'  : 'CMS_hww_VZScale',
               'type'  : 'lnN',
               'samples'  : {
                   'VgS_H' : '1.16', 
                   },
                }

# Top pT reweighting uncertainty
nuisances['TopPtRew']  = {
                'name'  : 'CMS_topPtRew',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples' : {
                     'top'  : ["1.0/Top_pTrw","Top_pTrw"]
                }
         }

nuisances['singleTopToTTbar']  = {
                'name'  : 'singleTopToTTbar',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples' : {
                     'top'  : ['(topGenPt * antitopGenPt <= 0.) * 1.0816 + (topGenPt * antitopGenPt > 0.)','(topGenPt * antitopGenPt <= 0.) * 0.9184 + (topGenPt * antitopGenPt > 0.)']
                },
         }

# DY uncertainties on corrections
nuisances['DYZptRew']  = {
                'name'  : 'CMS_DY_ZPtRew_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples' : {
                     'DY'  : ["DY_NLO_pTllrw","1.0/DY_NLO_pTllrw"]
                }
         }

nuisances['DYNLORew']  = {
                'name'  : 'CMS_DY_NLORew_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples' : {
                     'DY'  : ["(DY_LOtoNLOonly)*(DY_isLO) + (1.0)*(!DY_isLO)","(1.0/DY_LOtoNLOonly)*(DY_isLO) + (1.0)*(!DY_isLO)"]
                }
         }

if EMorEEorMM!="em":
  nuisances['DYLowMll']  = {
                'name'  : 'CMS_DY_mllRew_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples' : {
                     'DY'  : ["DY_LowMll","1.0/DY_LowMll"]
                }
         }

# WW EWK NLO correction uncertainty
nuisances['EWKcorr_WW'] = {
    'name': 'CMS_hww_EWKcorr_WW',
    'skipCMS': 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'WW': ['1./ewknloW', 'ewknloW']
    }
}

# Replace lnN nuisances (from QCD and PDF only -> Other lnN nuisance are consistent across SBI) for samples contributing to SBI with shape:
oldnuisances = copy.deepcopy(nuisances)
for nuis in oldnuisances:
  if nuisances[nuis]['type'] == "lnN" and (("QCD" in nuis) or ("pdf" in nuis)):
    for samp in oldnuisances[nuis]['samples']:
      if ("GGH" in samp) or ("QQH" in samp) or (samp in ["ggWW", "ggH_hww", "qqWWqq", "qqH_hww"]):
        lnNval = nuisances[nuis]['samples'][samp]
        if "/" in lnNval:
          lnNvalUp = lnNval.split('/')[0]
          lnNvalDn = lnNval.split('/')[1]
        else:
          lnNvalUp = lnNval
          lnNvalDn = str(1.0/float(lnNval))
        if nuis+'_shape' in nuisances:
          nuisances[nuis+'_shape']['samples'].update({samp: [lnNvalUp, lnNvalDn]})
        else:
          nuisances[nuis+'_shape'] = {
                'name'  : nuisances[nuis]['name'],
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples' : { samp : [lnNvalUp, lnNvalDn] },
                }
        del nuisances[nuis]['samples'][samp]
        if nuisances[nuis]['samples'] == {}: del nuisances[nuis]

# Now create SBI nuisances
nuisancename = {}
for nuis in nuisances:
  if nuisances[nuis]['type'] == "shape":
    if nuisances[nuis]['name'] not in nuisancename: nuisancename[nuisances[nuis]['name']] = []
    nuisancename[nuisances[nuis]['name']].append(nuis)
for nuisname in nuisancename:
  allsamples = {}
  for nuis in nuisancename[nuisname]:
    allsamples.update(nuisances[nuis]['samples']) # Sometimes have 2 dict keys doing shapes for the same nuisance for different samples; combine them here
  if [samp for samp in allsamples if 'SBI' in samp] == []:
    dogg=0
    doqq=0
    for samp in allsamples:
      if ("GGH" in samp) or (samp in ["ggWW", "ggH_hww"]): dogg=1
      elif ("QQH" in samp) or (samp in ["qqWWqq", "qqH_hww"]): doqq=1
    if dogg==1:
        SM_up = '1.0'
        SM_dn = '1.0'
        WW_up = '1.0'
        WW_dn = '1.0'
        sig_up = '1.0'
        sig_dn = '1.0'
        for nuis in nuisancename[nuisname]:
          if "ggH_hww" in nuisances[nuis]['samples']: SM_up = nuisances[nuis]['samples']["ggH_hww"][0]
          if "ggH_hww" in nuisances[nuis]['samples']: SM_dn = nuisances[nuis]['samples']["ggH_hww"][1]
          if "ggWW" in nuisances[nuis]['samples']: WW_up = nuisances[nuis]['samples']["ggWW"][0]
          if "ggWW" in nuisances[nuis]['samples']: WW_dn = nuisances[nuis]['samples']["ggWW"][1]
        for model in models:
          model_name = '_'+model.replace(".","")
          for m in massggh:
            for nuis in nuisancename[nuisname]:
              if 'GGH_'+m+model_name in nuisances[nuis]['samples']: sig_up = nuisances[nuis]['samples']['GGH_'+m+model_name][0]
              if 'GGH_'+m+model_name in nuisances[nuis]['samples']: sig_dn = nuisances[nuis]['samples']['GGH_'+m+model_name][1]
            SBI_string = ['('+sig_up+')*SBI_isHM + ('+SM_up+')*SBI_isSMggh + ('+WW_up+')*SBI_isggWW',
                          '('+sig_dn+')*SBI_isHM + ('+SM_dn+')*SBI_isSMggh + ('+WW_dn+')*SBI_isggWW']
            nuisances[nuis]['samples'].update({'GGHSBI_'+m+model_name: SBI_string})
    if doqq==1:
        SM_up = '1.0'
        SM_dn = '1.0'
        WW_up = '1.0'
        WW_dn = '1.0'
        sig_up = '1.0'
        sig_dn = '1.0'
        for nuis in nuisancename[nuisname]:
          if "qqH_hww" in nuisances[nuis]['samples']: SM_up = nuisances[nuis]['samples']["qqH_hww"][0]
          if "qqH_hww" in nuisances[nuis]['samples']: SM_dn = nuisances[nuis]['samples']["qqH_hww"][1]
          if "qqWWqq" in nuisances[nuis]['samples']: WW_up = nuisances[nuis]['samples']["qqWWqq"][0]
          if "qqWWqq" in nuisances[nuis]['samples']: WW_dn = nuisances[nuis]['samples']["qqWWqq"][1]
        for model in models:
          model_name = '_'+model.replace(".","")
          for m in massvbf:
            for nuis in nuisancename[nuisname]:
              if 'QQH_'+m+model_name in nuisances[nuis]['samples']: sig_up = nuisances[nuis]['samples']['QQH_'+m+model_name][0]
              if 'QQH_'+m+model_name in nuisances[nuis]['samples']: sig_dn = nuisances[nuis]['samples']['QQH_'+m+model_name][1]
            SBI_string = ['('+sig_up+')*SBI_isHM + ('+SM_up+')*SBI_isSMVBF + ('+WW_up+')*SBI_isqqWWqq',
                          '('+sig_dn+')*SBI_isHM + ('+SM_dn+')*SBI_isSMVBF + ('+WW_dn+')*SBI_isqqWWqq']
            nuisances[nuis]['samples'].update({'QQHSBI_'+m+model_name: SBI_string})


## Use the following if you want to apply the automatic combine MC stat nuisances.
#nuisances['stat']  = {
#              'type'  : 'auto',
#              'maxPoiss'  : '10',
#              'includeSignal'  : '0',
#              #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
#              #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
#              'samples' : {}
#             }

StatSwitch = True
# Doing zeroMCError=0 now because apparently it's not well defined otherwise for this analysis (or so I've been told)
# Also remove individual bbb from background (ggWW/qqWWqq/SM HWW), I'm now absorbing their statistical uncertainty into the nuisances of other more significant backgrounds (unaffected by r), so there's nothing to correlate
if StatSwitch:
  nuisances['stat']  = {
                  # apply to the following samples: name of samples here must match keys in samples.py
                 'samples'  : {

#                     'ggWW': {
#                           'typeStat' : 'bbb',
#                           'zeroMCError' : '0',
#                           'correlate': []
#                     },
#                     'ggH_hww':{
#                           'typeStat' : 'bbb',
#                           'zeroMCError' : '0',
#                           'correlate': []
#                     },
#                     'qqWWqq': {
#                          'typeStat' : 'bbb',
#                           'zeroMCError' : '0',
#                           'correlate': []
#                     },
#                     'qqH_hww':{
#                           'typeStat' : 'bbb',
#                           'zeroMCError' : '0',
#                           'correlate': []
#                     },


                   },
                 'type'  : 'shape',
                 'cuts'  : [cut for cut in cuts if ("dy" not in cut) and ("top" not in cut)]
                }

  for model in models:
    model_name = '_'+model.replace(".","")
    for m in massggh:
      nuisances['stat']['samples']['GGH_'+m+model_name] = { 'typeStat' : 'bbb', 'zeroMCError' : '0', 'correlate': [] }
      #nuisances['stat']['samples']['ggWW']["correlate"].append('GGHSBI_'+m+model_name)
      #nuisances['stat']['samples']['ggH_hww']["correlate"].append('GGHSBI_'+m+model_name)
      nuisances['stat']['samples']['GGH_'+m+model_name]['correlate'].append('GGHSBI_'+m+model_name)

    for m in massvbf:
      nuisances['stat']['samples']['QQH_'+m+model_name] = { 'typeStat' : 'bbb', 'zeroMCError' : '0', 'correlate': [] }
      #nuisances['stat']['samples']['qqWWqq']["correlate"].append('QQHSBI_'+m+model_name)
      #nuisances['stat']['samples']['qqH_hww']["correlate"].append('QQHSBI_'+m+model_name)
      nuisances['stat']['samples']['QQH_'+m+model_name]['correlate'].append('QQHSBI_'+m+model_name)

