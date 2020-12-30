import ROOT as R
import sys

f = R.TFile(sys.argv[1], "UPDATE")
nuisance_name = sys.argv[2]

samples = ['VBS','top','DATA','Fake','Wjets_HT','VVV','VV','VgS','Vg','DY','VBF-V']
for ir in range(1,7):
    samples.append("Wjets_HT_res_"+str(ir))
for ir in range(1,6):
    samples.append("Wjets_HT_boost_"+str(ir))


for sample_name in samples:

    #f.ls()
    for k in f.GetListOfKeys():
        #print(k)
        R.gDirectory.Cd(k.GetName())
        for z in R.gDirectory.GetListOfKeys():
            #print(z)
            print ">>> ", k.GetName(), z.GetName()
            R.gDirectory.Cd(z.GetName())
            for l in R.gDirectory.GetListOfKeys():
                if "histo_" + sample_name == l.GetName():
                    print "delete ", l.GetName()+"_"+nuisance_name+"*;*"
                    #Delete boh up and down
                    R.gDirectory.Delete(l.GetName()+"_"+nuisance_name+"*;*")
            R.gDirectory.Cd("../")

        R.gDirectory.Cd("../")

f.Write()
f.Close()
