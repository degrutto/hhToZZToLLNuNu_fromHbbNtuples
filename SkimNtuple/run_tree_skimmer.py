from sys import argv
argv.append( '-b-' )
import ROOT
ROOT.gROOT.SetBatch(True)
argv.remove( '-b-' )
from ROOT import TLorentzVector
import math
import os

import sys
sys.path.append('./')
#sys.path.append('../python/')
from samples import *

samples = samples_V24

sample_to_process = samples[argv[1]]
print "\nProcessing sample", argv[1]

is_empty = True
processed = 0
processedP = 0
processedN = 0

chain = ROOT.TChain("tree")
for ff in xrange(int(argv[2]),int(argv[3])+1):
  fname = sample_to_process[0]+"tree_"+str(ff)+".root"
  fi = ROOT.TFile.Open(fname)
  if fi==None or fi.IsZombie():
    continue
  is_empty = False
  chain.AddFile(fname)  
  processed += fi.Get("CountWeighted").GetBinContent(1)
  processedP += fi.Get("CountPosWeight").GetBinContent(1)
  processedN += fi.Get("CountNegWeight").GetBinContent(1)
  fi.Close()
  print "Adding file n.", ff, ": total processed events:", processed

if is_empty:
  print "Return because no files could be opened"
  exit(1)

h_count = ROOT.TH1F("CountWeighted", "CountWeighted", 1, 0, 2)
h_count.Fill(1, processed)

h_countPos = ROOT.TH1F("CountPosWeight", "CountPosWeight", 1, 0, 2)
h_countPos.Fill(1, processedP)

h_countNeg = ROOT.TH1F("CountNegWeight", "CountNegWeight", 1, 0, 2)
h_countNeg.Fill(1, processedN)



os.system('mkdir /afs/cern.ch/work/d/degrutto/private/VHbb_2016/CMSSW_8_0_11/src/SkimNtuple/files/'+argv[1])
f = ROOT.TFile("/afs/cern.ch/work/d/degrutto/private/VHbb_2016/CMSSW_8_0_11/src/SkimNtuple/files/"+argv[1]+"/tree_"+argv[4]+".root", "RECREATE")


chain.SetBranchStatus("*", True)
chain.SetBranchStatus("HLT_*")
chain.SetBranchStatus("Jet_*", True)
chain.SetBranchStatus("met*", True)
#chain.SetBranchStatus("mht*", True)
chain.SetBranchStatus("sel*", True)
chain.SetBranchStatus("V*", True)
chain.SetBranchStatus("v*", True)
chain.SetBranchStatus("gen*", True)
chain.SetBranchStatus("gen*", True)
chain.SetBranchStatus("pu*", True) ### check

#cut_string = "(HLT_BIT_HLT_DoubleJetsC100_DoubleBTagCSV0p85_DoublePFJetsC160_v | HLT_BIT_HLT_DoubleJetsC100_DoubleBTagCSV0p9_DoublePFJetsC100MaxDeta1p6_v) & (TMath::Abs(Jet_eta[hJCidx[0]]-Jet_eta[hJCidx[1]])<1.6 & Jet_pt[hJCidx[0]]>200 & Jet_pt[hJCidx[1]]>200 & TMath::Abs(Jet_eta[hJCidx[0]])<2.4 & TMath::Abs(Jet_eta[hJCidx[1]])<2.4)"
#cut_string = "(HLT_BIT_HLT_DoubleJetsC100_DoubleBTagCSV0p85_DoublePFJetsC160_v | HLT_BIT_HLT_DoubleJetsC100_DoubleBTagCSV0p9_DoublePFJetsC100MaxDeta1p6_v) & (TMath::Abs(Jet_eta[hJCidx[0]]-Jet_eta[hJCidx[1]])<2.0 & Jet_pt[hJCidx[0]]>150 & Jet_pt[hJCidx[1]]>150 & TMath::Abs(Jet_eta[hJCidx[0]])<2.4 & TMath::Abs(Jet_eta[hJCidx[1]])<2.4)"
#cut_string = "min(mhtJet30,met_pt)>100 && json && Sum$(vLeptons_pt>30)>=1 && (Vtype==2 || Vtype==3)"
#cut_string = "json && (Vtype>=2) && met_pt>170 && H_pt>170 && min(Jet_btagCSV[hJidx[0]], Jet_btagCSV[hJidx[1]])>0.46"
#cut_string = "V_pt>100 && json && vLeptons_pt[0]>30 && (Vtype==2 || Vtype==3)"
cut_string = "V_mass>50 && json && (Vtype==0 || Vtype==1)"

print "Cut string: ", cut_string
print "Copying tree with ", chain.GetEntries(), " entries..."
tree = chain.CopyTree(cut_string, "")
print "Copied ", tree.GetEntries(), " entries satisfying the cut condition"

print "Writing to file..."
f.cd()
tree.Write("", ROOT.TObject.kOverwrite)
h_count.Write("", ROOT.TObject.kOverwrite)
h_countPos.Write("", ROOT.TObject.kOverwrite)
h_countNeg.Write("", ROOT.TObject.kOverwrite)
f.Close()
print "Done!"
