import os
import copy
import inspect

# /afs/cern.ch/user/n/ntrevisa/work/latinos/unblinding/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/WH_chargeAsymmetry/UL/2016noHIPM_v9/WH3l

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # WH3l
configurations = os.path.dirname(configurations) # 2016noHIPM_v9
configurations = os.path.dirname(configurations) # UL
configurations = os.path.dirname(configurations) # WH_chargeAsymmetry
configurations = os.path.dirname(configurations) # Configurations

#aliases = {}
mc     = [skey for skey in samples if skey not in ('Fake', 'DATA', 'Dyemb')]
mc_emb = [skey for skey in samples if skey not in ('Fake', 'DATA')]

# LepCut2l__ele_mvaFall17V2Iso_WP90_tthmva_70__mu_cut_Tight_HWWW_tthmva_80
eleWP = 'mvaFall17V2Iso_WP90_SS_tthmva_70'
muWP  = 'cut_Tight80x_tthmva_80'

aliases['LepWPCut'] = {
    'expr': 'LepCut3l__ele_mvaFall17V2Iso_WP90__mu_cut_Tight80x*\
               ( ( (abs(Lepton_pdgId[0])==13 && Muon_mvaTTH[Lepton_muonIdx[0]]>0.85) || (abs(Lepton_pdgId[0])==11 && Lepton_mvaTTH_UL[0]>0.95) ) \
              && ( (abs(Lepton_pdgId[1])==13 && Muon_mvaTTH[Lepton_muonIdx[1]]>0.85) || (abs(Lepton_pdgId[1])==11 && Lepton_mvaTTH_UL[1]>0.95) ) \
              && ( (abs(Lepton_pdgId[2])==13 && Muon_mvaTTH[Lepton_muonIdx[2]]>0.85) || (abs(Lepton_pdgId[2])==11 && Lepton_mvaTTH_UL[2]>0.95) ) )',
    'samples': mc +  ['DATA']
}
#'expr': 'LepCut2l__ele_mvaFall17V2Iso_WP90__mu_cut_Tight_HWWW*\
#         ( (abs(Lepton_pdgId[0])==11 || Muon_mvaTTH[Lepton_muonIdx[0]]>0.85) && (abs(Lepton_pdgId[1])==11 || Muon_mvaTTH[Lepton_muonIdx[1]]>0.85) \
#        && (abs(Lepton_pdgId[0])==13 || Lepton_mvaTTH_UL[0]>0.95)            && (abs(Lepton_pdgId[1])==13 || Lepton_mvaTTH_UL[1]>0.95) )',

aliases['LepWPSF'] = {
    'expr': 'LepSF3l__ele_'+eleWP+'__mu_'+muWP,
    'samples': mc
}

# Fake leptons transfer factor
aliases['fakeW'] = {
    'linesToAdd' : ['.L %s/WH_chargeAsymmetry/UL/macros/fake_rate_reader.C+' % configurations],
    'class'      : 'fake_rate_reader',
    'args'       : ('2016_noHIPM', '95', '85', 0.95, 0.85, 'nominal', 3),
    'samples'    : ['Fake']
}
# aliases['fakeW'] = {
#     'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP,
#     'samples': ['Fake']
# }

# # And variations - already divided by central values in formulas !
# aliases['fakeWEleUp'] = {
#     'linesToAdd' : ['.L %s/WH_chargeAsymmetry/UL/macros/fake_rate_reader.C+' % configurations],
#     'class'      : 'fake_rate_reader',
#     'args'       : ('2017', '95', '85', 0.95, 0.85, 'EleUp', 3),
#     'samples'    : ['Fake']
# }

# aliases['fakeWEleDown'] = {
#     'linesToAdd' : ['.L %s/WH_chargeAsymmetry/UL/macros/fake_rate_reader.C+' % configurations],
#     'class'      : 'fake_rate_reader',
#     'args'       : ('2017', '95', '85', 0.95, 0.85, 'EleDown', 3),
#     'samples'    : ['Fake']
# }

# aliases['fakeWMuUp'] = {
#     'linesToAdd' : ['.L %s/WH_chargeAsymmetry/UL/macros/fake_rate_reader.C+' % configurations],
#     'class'      : 'fake_rate_reader',
#     'args'       : ('2017', '95', '85', 0.95, 0.85, 'MuUp', 3),
#     'samples'    : ['Fake']
# }

# aliases['fakeWMuDown'] = {
#     'linesToAdd' : ['.L %s/WH_chargeAsymmetry/UL/macros/fake_rate_reader.C+' % configurations],
#     'class'      : 'fake_rate_reader',
#     'args'       : ('2017', '95', '85', 0.95, 0.85, 'MuDown', 3),
#     'samples'    : ['Fake']
# }


# aliases['fakeWStatEleUp'] = {
#     'linesToAdd' : ['.L %s/WH_chargeAsymmetry/UL/macros/fake_rate_reader.C+' % configurations],
#     'class'      : 'fake_rate_reader',
#     'args'       : ('2017', '95', '85', 0.95, 0.85, 'StatEleUp', 3),
#     'samples'    : ['Fake']
# }

# aliases['fakeWStatEleDown'] = {
#     'linesToAdd' : ['.L %s/WH_chargeAsymmetry/UL/macros/fake_rate_reader.C+' % configurations],
#     'class'      : 'fake_rate_reader',
#     'args'       : ('2017', '95', '85', 0.95, 0.85, 'StatEleDown', 3),
#     'samples'    : ['Fake']
# }

# aliases['fakeWStatMuUp'] = {
#     'linesToAdd' : ['.L %s/WH_chargeAsymmetry/UL/macros/fake_rate_reader.C+' % configurations],
#     'class'      : 'fake_rate_reader',
#     'args'       : ('2017', '95', '85', 0.95, 0.85, 'StatMuUp', 3),
#     'samples'    : ['Fake']
# }

# aliases['fakeWStatMuDown'] = {
#     'linesToAdd' : ['.L %s/WH_chargeAsymmetry/UL/macros/fake_rate_reader.C+' % configurations],
#     'class'      : 'fake_rate_reader',
#     'args'       : ('2017', '95', '85', 0.95, 0.85, 'StatMuDown', 3),
#     'samples'    : ['Fake']
# }
# # # And variations - already divided by central values in formulas !
# # aliases['fakeWEleUp'] = {
# #     'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleUp',
# #     'samples': ['Fake']
# # }
# # aliases['fakeWEleDown'] = {
# #     'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleDown',
# #     'samples': ['Fake']
# # }
# # aliases['fakeWMuUp'] = {
# #     'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuUp',
# #     'samples': ['Fake']
# # }
# # aliases['fakeWMuDown'] = {
# #     'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuDown',
# #     'samples': ['Fake']
# # }
# # aliases['fakeWStatEleUp'] = {
# #     'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleUp',
# #     'samples': ['Fake']
# # }
# # aliases['fakeWStatEleDown'] = {
# #     'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleDown',
# #     'samples': ['Fake']
# # }
# # aliases['fakeWStatMuUp'] = {
# #     'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuUp',
# #     'samples': ['Fake']
# # }
# # aliases['fakeWStatMuDown'] = {
# #     'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuDown',
# #     'samples': ['Fake']
# # }

# No jet with pt > 30 GeV
aliases['zeroJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) < 30.'
}

aliases['oneJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) > 30.'
}

aliases['multiJet'] = {
    'expr': 'Alt$(CleanJet_pt[1], 0) > 30.'
}

###########################################################################################
# b tagging WPs: https://twiki.cern.ch/twiki/bin/view/CMS/BtagRecommendation106XUL16postVFP
###########################################################################################

# DeepB = DeepCSV
bWP_loose_deepB  = '0.1918'
bWP_medium_deepB = '0.5847' 
bWP_tight_deepB  = '0.8767'

# DeepFlavB = DeepJet
bWP_loose_deepFlavB  = '0.0480'
bWP_medium_deepFlavB = '0.2489'
bWP_tight_deepFlavB  = '0.6377'

# Actual algo and WP definition. BE CONSISTENT!!
bAlgo = 'DeepB' # ['DeepB','DeepFlavB']
bWP   = bWP_loose_deepB
bSF   = 'deepcsv' # ['deepcsv','deepjet']

# b veto
aliases['bVeto'] = {
    'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btag{}[CleanJet_jetIdx] > {}) == 0'.format(bAlgo, bWP)
}

aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_{}_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))'.format(bSF),
    'samples': mc
}

# At least one b-tagged jet
aliases['bReq'] = {
    'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btag{}[CleanJet_jetIdx] > {}) >= 1'.format(bAlgo, bWP)
}

aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_{}_shape[CleanJet_jetIdx]+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))'.format(bSF),
    'samples': mc
}

# Top control region
aliases['topcr'] = {
    'expr': 'mtw2>30 && mll>50 && ((zeroJet && !bVeto) || bReq)'
}

# WW control region
aliases['wwcr'] = {
    'expr': 'mth>60 && mtw2>30 && mll>100 && bVeto'
}

# Overall b tag SF
aliases['btagSF'] = {
    'expr': '(bVeto || (topcr && zeroJet))*bVetoSF + (topcr && !zeroJet)*bReqSF',
    'samples': mc
}

for shift in ['jes', 'lf', 'hf', 'lfstats1', 'lfstats2', 'hfstats1', 'hfstats2', 'cferr1', 'cferr2']:
    for targ in ['bVeto', 'bReq']:
        alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_{}_shape'.format(bSF), 'btagSF_{}_shape_up_{}'.format(bSF, shift))

        alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_{}_shape'.format(bSF), 'btagSF_{}_shape_down_{}'.format(bSF, shift))

    aliases['btagSF%sup' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
        'samples': mc
    }

    aliases['btagSF%sdown' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
        'samples': mc
    }

####################################################################################
# End of b tagging pippone
####################################################################################


aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 4',
    'samples': 'WgS'
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass < 0 || Gen_ZGstar_mass > 4',
    'samples': 'WZ'
}

# aliases['embedtotal'] = {
#     'expr': 'embed_total_mva16',  # wrt. eleWP
#     'samples': 'Dyemb'
# }


# gen-matching to prompt only (GenLepMatch3l matches to *any* gen lepton)
aliases['PromptGenLepMatch3l'] = {
    'expr': 'Alt$(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1]*Lepton_promptgenmatched[2], 0)',
    'samples': mc
}

# # PostProcessing did not create (anti)topGenPt for ST samples with _ext1
# lastcopy = (1 << 13)

# aliases['isTTbar'] = {
#     'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 2' % lastcopy,
#     'samples': ['top']
# }

# aliases['isSingleTop'] = {
#     'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 1' % lastcopy,
#     'samples': ['top']
# }

aliases['Top_pTrw'] = {
    'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPt) - 0.000134*topGenPt + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPt) - 0.000134*antitopGenPt + 0.973))) + (topGenPt * antitopGenPt <= 0.)',
    'samples': ['top']
}


# aliases['topGenPtOTF'] = {
#     'expr': 'Sum$((GenPart_pdgId == 6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
#     'samples': ['top']
# }

# aliases['antitopGenPtOTF'] = {
#     'expr': 'Sum$((GenPart_pdgId == -6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
#     'samples': ['top']
# }



##### DY Z pT reweighting
aliases['nCleanGenJet'] = {
    'linesToAdd': ['.L %s/src/PlotsConfigurations/Configurations/Differential/ngenjet.cc+' % os.getenv('CMSSW_BASE')],
    'class': 'CountGenJet',
    'samples': mc
}

# aliases['getGenZpt_OTF'] = {
#     'linesToAdd':['.L %s/src/PlotsConfigurations/Configurations/patches/getGenZpt.cc+' % os.getenv('CMSSW_BASE')],
#     'class': 'getGenZpt',
#     'samples': ['DY']
# }
# handle = open('%s/src/PlotsConfigurations/Configurations/patches/DYrew30.py' % os.getenv('CMSSW_BASE'),'r')
# exec(handle)
# handle.close()
# aliases['DY_NLO_pTllrw'] = {
#     'expr': '('+DYrew['2016']['NLO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
#     'samples': ['DY']
# }
# aliases['DY_LO_pTllrw'] = {
#     'expr': '('+DYrew['2016']['LO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
#     'samples': ['DY']
# }


# Jet bins
# using Alt$(CleanJet_pt[n], 0) instead of Sum$(CleanJet_pt >= 30) because jet pt ordering is not strictly followed in JES-varied samples

# aliases['SFweight2lAlt'] = {
#     'expr'   : 'puWeight*TriggerSFWeight_2l*Lepton_RecoSF[0]*Lepton_RecoSF[1]*EMTFbug_veto',
#     'samples': mc
# }

# data/MC scale factors
aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight3l', 'LepWPCut', 'LepWPSF','PrefireWeight','Jet_PUIDSF_loose', 'btagSF']),
    'samples': mc
}

# # variations
# aliases['SFweightEleUp'] = {
#     'expr': 'LepSF2l__ele_'+eleWP+'__Up',
#     'samples': mc_emb
# }
# aliases['SFweightEleDown'] = {
#     'expr': 'LepSF2l__ele_'+eleWP+'__Do',
#     'samples': mc_emb
# }
# aliases['SFweightMuUp'] = {
#     'expr': 'LepSF2l__mu_'+muWP+'__Up',
#     'samples': mc_emb
# }
# aliases['SFweightMuDown'] = {
#     'expr': 'LepSF2l__mu_'+muWP+'__Do',
#     'samples': mc_emb
# }

# # In WpWmJJ_EWK events, partons [0] and [1] are always the decay products of the first W
# aliases['lhe_mW1'] = {
#     'expr': 'TMath::Sqrt(2. * LHEPart_pt[0] * LHEPart_pt[1] * (TMath::CosH(LHEPart_eta[0] - LHEPart_eta[1]) - TMath::Cos(LHEPart_phi[0] - LHEPart_phi[1])))',
#     'samples': ['WWewk']
# }

# # and [2] [3] are the second W
# aliases['lhe_mW2'] = {
#     'expr': 'TMath::Sqrt(2. * LHEPart_pt[2] * LHEPart_pt[3] * (TMath::CosH(LHEPart_eta[2] - LHEPart_eta[3]) - TMath::Cos(LHEPart_phi[2] - LHEPart_phi[3])))',
#     'samples': ['WWewk']
# }

# ### BDT on-the-fly
# aliases['BDT_SS_v7'] = {
#     'class': 'BDT_v7_noCorrelatedVariables',
#     'linesToAdd' : ['.L %s/WH_chargeAsymmetry/WHSS/Full2018_v7/macros/BDT_v7_noCorrelatedVariables.C+' % configurations],
# }

# ########################
# ### Charge misid SFs ###
# ########################

# aliases['ttHMVA_SF_flip_2l'] = {
#     'linesToAdd': ['.L %s/macros/flipper.C+' % configurations],
#     'class': 'flipper',
#     'args' : ('2018', 2, 'Total_SF', 'false'),
#     'samples': ['DY','WW','top']
# }

# aliases['ttHMVA_SF_err_flip_2l'] = {
#     'linesToAdd': ['.L %s/macros/flipper.C+' % configurations],
#     'class': 'flipper',
#     'args' : ('2018', 2, 'Total_SF_err', 'false'),
#     'samples': ['DY','WW','top']
# }

# ##################################
# ### Charge misid probabilities ###
# ##################################

# aliases['ttHMVA_eff_flip_2l'] = {
#     'linesToAdd': ['.L %s/macros/flipper_eff.C+' % configurations],
#     'class': 'flipper_eff',
#     'args' : ('2018', 2, 'Total_SF'),
#     'samples': ['DY_OS']
# }

# aliases['ttHMVA_eff_err_flip_2l'] = {
#     'linesToAdd': ['.L %s/macros/flipper_eff.C+' % configurations],
#     'class': 'flipper_eff',
#     'args' : ('2018', 2, 'Total_SF_err'),
#     'samples': ['DY_OS']
# }

## WH3l variables

# aliases['WH3l_dphilllmet_test'] = {
#     'linesToAdd': [
#         '.L %s/src/PlotsConfigurations/Configurations/WH_chargeAsymmetry/WH3l/scripts/WH3l_patch_BDT1718.cc+' % os.getenv('CMSSW_BASE')
#     ],
#     'class': 'WH3l_patch_BDT1718',
#     'args': ("dphilllmet")
# }

# aliases['BDT_SSSF1718'] = {
#     'linesToAdd': [
#         '.L %s/src/PlotsConfigurations/Configurations/WH_chargeAsymmetry/WH3l/scripts/WH3l_patch_BDT1718.cc+' % os.getenv('CMSSW_BASE')
#     ],
#     'class': 'WH3l_patch_BDT1718',
#     'args': ("BDT_SSSF1718")
# }

# aliases['BDT_OSSF1718'] = {
#     'class': 'WH3l_patch_BDT1718',
#     'args': ("BDT_OSSF1718")
# }

# aliases['WH3l_mOSll_min_test'] = {
#     'class': 'WH3l_patch_BDT1718',
#     'args': ("mOSllmin")
# }

# aliases['WH3l_ptOSll_min_test'] = {
#     'class': 'WH3l_patch_BDT1718',
#     'args': ("ptOSllmin")
# }

# aliases['WH3l_drOSll_min_test'] = {
#     'class': 'WH3l_patch_BDT1718',
#     'args': ("drOSllmin")
# }

# aliases['WH3l_ZVeto_test'] = {
#     'class': 'WH3l_patch_BDT1718',
#     'args': ("ZVeto")
# }

# aliases['WH3l_ptlll_test'] = {
#     'class': 'WH3l_patch_BDT1718',
#     'args': ("ptlll")
# }

# aliases['WH3l_mtlmet0_test'] = {
#     'class': 'WH3l_patch_BDT1718',
#     'args': ("mtlmet0")
# }

# aliases['WH3l_mtlmet1_test'] = {
#     'class': 'WH3l_patch_BDT1718',
#     'args': ("mtlmet1")
# }

# aliases['WH3l_mtlmet2_test'] = {
#     'class': 'WH3l_patch_BDT1718',
#     'args': ("mtlmet2")
# }

# aliases['WH3l_dphilmet0_test'] = {
#     'class': 'WH3l_patch_BDT1718',
#     'args': ("dphilmet0")
# }

# aliases['WH3l_dphilmet1_test'] = {
#     'class': 'WH3l_patch_BDT1718',
#     'args': ("dphilmet1")
# }

# aliases['WH3l_dphilmet2_test'] = {
#     'class': 'WH3l_patch_BDT1718',
#     'args': ("dphilmet2")
# }

# aliases['WH3l_ptWWW_test'] = {
#     'class': 'WH3l_patch_BDT1718',
#     'args': ("ptWWW")
# }

# aliases['WH3l_mtWWW_test'] = {
#     'class': 'WH3l_patch_BDT1718',
#     'args': ("mtWWW")
# }

# aliases['WH3l_mlll_test'] = {
#     'class': 'WH3l_patch_BDT1718',
#     'args': ("mlll")
# }

# # aliases['BDT_SSSFcombin'] = {
# #     'class': 'WH3l_patch_BDT1718',
# #     'args': ("BDT_SSSFcombin")
# # }

# # aliases['BDT_OSSFcombin'] = {
# #     'class': 'WH3l_patch_BDT1718',
# #     'args': ("BDT_OSSFcombin")
# # }

# Fix METFilter_DATA definition: Flag_ecalBadCalibFilter is removed since it is not needed in 2016
aliases['METFilter_DATA_fix'] = {
    'expr' : 'Flag_goodVertices*Flag_globalSuperTightHalo2016Filter*Flag_HBHENoiseFilter*Flag_HBHENoiseIsoFilter*Flag_EcalDeadCellTriggerPrimitiveFilter*Flag_BadPFMuonFilter*Flag_BadPFMuonDzFilter*Flag_eeBadScFilter',
    'samples': ['DATA','Fake']
}