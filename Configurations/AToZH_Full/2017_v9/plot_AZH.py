# plot configuration
# groupPlot = {}
 
# Groups of samples to improve the plots.
# If not defined, normal plots is used

groupPlot['VVV']  = {  
                  'nameHR' : 'VVV',
                  'isSignal' : 0,
                  'color': 806, # kOrange + 6
                  'samples'  : ['VVV']
              }

groupPlot['top']  = {  
                  'nameHR' : 'top',
                  'isSignal' : 0,
                  'color': 807, # kOrange + 6
                  'samples'  : ['top']
              }
groupPlot['Zg']  = {
          'nameHR' : 'Zg',
          'color': 859, # kAzure -1  
         'isSignal' : 0,
          'samples'  : ['Zg']
     }

groupPlot['ZgS']  = {
          'nameHR' : 'ZgS',
          'color': 432, # kCyan  
          'isSignal' : 0,
          'samples'  : ['ZgS']
      }


groupPlot['ZZ']  = {
         'nameHR' : "ZZ",
         'isSignal' : 0,
         'color'    : 881,   # kViolet + 1  
         'samples'  : ['ZZ']
      }

groupPlot['WZ']  = {
         'nameHR' : "WZ",
         'isSignal' : 0,
         'color'    : 400,   # Yellow
         'samples'  : ['WZ', 'WZ_had']
}
groupPlot['Fake']  = {  
                  'nameHR' : 'Non-prompt',
                  'isSignal' : 0,
                  'color': 921,    # kGray + 1
                  'samples'  : ['Fake']
              }
groupPlot['ttZ']  = {
  		   'nameHR' : 'ttZ',
		   'color': 419,    # kGreen+3
		   'isSignal' : 0,
		   'samples' : ['ttV']
}

groupPlot['ttW']  = {
  		   'nameHR' : 'ttW',
		   'color': 419,    # kGreen+3
		   'isSignal' : 0,
		   'samples' : ['TTWJets']
}
groupPlot['ttH_hww']  = {
         'nameHR' : "ttH",
         'isSignal' : 0,
         'color'    : 890,   # kViolet + 10  
         'samples'  : ['ttH_hww']
      }

groupPlot['tZq_ll']  = {
         'nameHR' : "tZq_ll",
         'isSignal' : 0,
         'color'    : 883,   # kViolet + 3  
         'samples'  : ['tZq_ll']
      }

#groupPlot['AZH_800_600'] = {
#          'nameHR' : "AZH_800_600",
#          'isSignal' : 1,
#          'color': 632,
#	  'isData'  : 0,
#}


#groupPlot['AZH_1200_1000'] = {
#          'nameHR' : "AZH_1200_1000",
#          'isSignal' : 1,
#	  'color': 632,
#          'isData'  : 0,
#}


#groupPlot['AZH_1200_850'] = {
#          'nameHR' : "AZH_1200_850",
#          'color': 632,
# 	  'isSignal' : 1,
#          'isData'  : 0,
#}
#groupPlot['AZH_500_350'] = {
#          'nameHR' : "AZH_500_350",
#          'color': 632,
# 	  'isSignal' : 1,
#          'isData'  : 0,
#}
#groupPlot['AZH_500_400'] = {
#          'nameHR' : "AZH_500_400",
#          'color': 632,
#	  'isSignal' : 1,
#          'isData'  : 0,
#}
#groupPlot['AZH_700_350'] = {
#          'nameHR' : "AZH_700_350",
#          'isSignal' : 1,
#	  'color': 632,
#          'isData'  : 0,
#}
#groupPlot['AZH_700_370'] = {
#          'nameHR' : "AZH_700_370",
#          'isSignal' : 1,
#	  'color': 632,
#          'isData'  : 0,
#}
#groupPlot['AZH_700_400'] = {
#          'nameHR' : "AZH_700_400",
#          'isSignal' : 1,
#	  'color': 632,
#          'isData'  : 0,
#}
#groupPlot['AZH_900_370'] = {
#          'nameHR' : "AZH_900_370",
#          'isSignal' : 1,
#	  'color': 632,
#          'isData'  : 0,
#}

groupPlot['AZH_900_400'] = {
          'nameHR' : "AZH_900_400",
          'isSignal' : 1,
          'color': 632,
          'samples' : ['AZH_900_400']
}

#plot['ZZTo4L']  = {
#groupPlot['AZH']  = {  
#                  'nameHR' : 'AZH',
#                  'isSignal' : 1,
##                  'isSignal' :0, # to turn the overlay off
#		  'color': 632, # kRed 
##                  'scaleMultiplicativeOverlaid' : 10.0, #Turn on for SR plots
 #                 'samples'  : ['AZH_800_600', 'AZH_1200_1000', 'AZH_1200_850', 'AZH_500_350', 'AZH_500_400', 'AZH_700_350', 'AZH_700_370', 'AZH_700_400', 'AZH_900_370', 'AZH_900_400']
#              }

# Individual plots

#plot['AZH_800_600'] = {
#          'nameHR' : "AZH_800_600",
#          'isSignal' : 1,
#          'color': 632,
#	  'isData'  : 0,
#}


#plot['AZH_1200_1000'] = {
#          'nameHR' : "AZH_1200_1000",
#          'isSignal' : 1,
#	  'color': 632,
#          'isData'  : 0,
#}


#plot['AZH_1200_850'] = {
#          'nameHR' : "AZH_1200_850",
#          'color': 632,
# 	  'isSignal' : 1,
#          'isData'  : 0,
#}
#plot['AZH_500_350'] = {
#          'nameHR' : "AZH_500_350",
#          'color': 632,
# 	  'isSignal' : 1,
#          'isData'  : 0,
#}
#plot['AZH_500_400'] = {
#          'nameHR' : "AZH_500_400",
#          'color': 632,
#	  'isSignal' : 1,
#          'isData'  : 0,
#}
#plot['AZH_700_350'] = {
#          'nameHR' : "AZH_700_350",
#          'isSignal' : 1,
#	  'color': 632,
#          'isData'  : 0,
#}
#plot['AZH_700_370'] = {
#          'nameHR' : "AZH_700_370",
#          'isSignal' : 1,
#	  'color': 632,
#          'isData'  : 0,
#}
#plot['AZH_700_400'] = {
#          'nameHR' : "AZH_700_400",
#          'isSignal' : 1,
#	  'color': 632,
#          'isData'  : 0,
#}
#plot['AZH_900_370'] = {
#          'nameHR' : "AZH_900_370",
#          'isSignal' : 1,
#	  'color': 632,
#          'isData'  : 0,
#}

plot['AZH_900_400'] = {
          'nameHR' : "AZH_900_400",
          'isSignal' : 1,
	  'color': 632,
          'isData'  : 0,
}

#plot['ZZ']  = {
#         'nameHR' : "ZZ",
#         'isSignal' : 0,
#         'color'    : 881,   # kViolet + 1  
#         'isData'  : 0,
#         'scale'   : 1.0
#      }



plot['WZ']  = {
    'nameHR' : 'WZ',
    'color': 858, # kAzure -2  
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
	    #'scale'    : 0.87 #1j norm
	   #'scale'    : 1.42 #2j norm
}


plot['WZ_had']  = {
    'nameHR' : 'WZ_had',
    'color': 888, # kAzure -2  
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
#	    #'scale'    : 0.87 #1j norm
#	   #'scale'    : 1.42 #2j norm
}


plot['TTWJets']  = {
    'nameHR' : 'ttW',
    'color': 899, # kAzure -2  
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
	    #'scale'    : 0.87 #1j norm
	   #'scale'    : 1.42 #2j norm
}



plot['Zg']  = {
      'nameHR' : 'Zg',
      'color': 859, # kAzure -1  
      'isSignal' : 0,
      'isData'   : 0,
      'scale'    : 1.0
  }

plot['ZgS']  = {
       'nameHR' : 'ZgS',
       'color': 859, # kAzure -1  
       'isSignal' : 0,
       'isData'   : 0,
       'scale'    : 1.0
 }


plot['ZZ']  = {
       'nameHR' : 'ZZ',
       'color': 856, # kAzure -4  
       'isSignal' : 0,
       'isData'   : 0,
       'scale'    : 1.0
}


plot['top']  = {  
                  'nameHR' : 'top',
                  'isSignal' : 0,
                  'color': 806, # kOrange + 6
                  'isData' : 0,
                   'scale' : 1.0,
              }
plot['VVV']  = { 
                  'color': 857, # kAzure -3  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['ttV']  = {
		  'color': 419,    # kGreen+3
		  'isSignal' : 0,
		  'isData'   : 0,
		  'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
}

plot['ttH_hww']  = {
		  'color': 420,    # kGreen+3
		  'isSignal' : 0,
		  'isData'   : 0,
		  'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
}

plot['tZq_ll']  = {
		  'color': 421,    # kGreen+3
		  'isSignal' : 0,
		  'isData'   : 0,
		  'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
}
plot['Fake']  = {  
                  'color': 921,    # kGray + 1
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0                  
              }

#plot['AZH'] = {
#                  'nameHR' : 'AZH',
#                  'color': 632+3, # kRed+3 
#                  'isSignal' : 1,
#                  'isData'   : 0,    
#                  'scale'    : 1
#                  }


plot['DATA']  = {
                  'nameHR' : 'Data',
                  'color': 1 ,
                  'isSignal' : 0,
                  'isData'   : 1 ,
                  'isBlind'  : 1 
                }

# additional options

legend['lumi'] = 'L = 41.5/fb'
legend['sqrt'] = '#sqrt{s} = 13 TeV'