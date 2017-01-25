#!/usr/bin/env python

from sys import argv
import commands
import time
import re
import os
import string
from os import listdir
from os.path import isfile, join

import FWCore.ParameterSet.Config as cms

import sys
sys.path.append('./')

# options are "run_tree_skimmer" "run_histos"
run = argv[1]

################################################################################

def submit(sample, first, last, postfix):
    print "Running: submit.py "+run
    scriptName = 'job_'+sample+'_'+str(first)+'_'+str(last)+'.sh'
    jobName    = 'job_'+sample+'_'+str(first)+'_'+str(last)
    outName = ""
    if run=="run_histos":
        if first>=0:
            outName = sample+'_'+str(first)+'_'+str(last)
        else:
            outName = sample
    if run=="run_tree_skimmer":
        outName = "tree_"+str(postfix)
    f = open(scriptName,'w')
    f.write('#!/bin/bash\n\n')
    f.write('cd  /afs/cern.ch/work/d/degrutto/private/VHbb_2016/CMSSW_8_0_11/src/SkimNtuple\n')
#    f.write('cd /mnt/t3nfs01/data01/shome/bianchi/TTH-76X-heppy/CMSSW/src/TTH/MEIntegratorStandalone/test/macros\n')                                                                                
 #   f.write('source /swshare/psit3/etc/profile.d/cms_ui_env.sh\n')                                                                                                                                  
    f.write('source /cvmfs/cms.cern.ch/cmsset_default.sh\n')
    f.write('eval `scramv1 runtime -sh`\n')
    f.write('\n')

    f.write('export X509_USER_PROXY=/afs/cern.ch/work/d/degrutto/private/VHbb_2016/CMSSW_8_0_11/src/SkimNtuple/x509up_u24426\n')
#    f.write('eosmount /afs/cern.ch/work/d/degrutto/private/Xbbanalysis/CMSSW_7_6_3_patch2/src/Hbb/test/eos/')

    f.write('\n')    
    f.write('python '+run+'.py '+sample+' '+str(first)+' '+str(last)+' '+str(postfix)+'\n')

#    if run=="run_tree_skimmer":
#        f.write('mkdir '+sample+'\n')
#        f.write('mv /scratch/$USER/'+sample+'/'+outName+'.root ./'+sample+'/'+'\n')    
#    else:
#        f.write('mv /scratch/$USER/'+outName+'.root ./'+'\n')    

    f.close()
    os.system('chmod +x '+scriptName)
             
#    submitToQueue = 'bsub -q 8nh -G CMS_CERN01_YODA -J testXbb -u pippo123'+jobName+' '+scriptName
    
    submitToQueue =  'bsub -q 8nh -G CMS_CERN01_YODA -J '+jobName+' -u pippo123 <'+scriptName              
    print submitToQueue
    os.system(submitToQueue)
    time.sleep( 1.0 )

    print "@@@@@ END JOB @@@@@@@@@@@@@@@"


##########################################

# [name, files_per_sample, njobs, offset [OPTIONAL]]
for sample in [

    # run_tree_skimmer:

#    ["MET_Run2016B_0",10, 100],
#    ["MET_Run2016B_1",10, 100,1000],
#    ["MET_Run2016B_2",10, 100,2000],
#    ["MET_Run2016C",10, 100],
#    ["MET_Run2016D",10, 100],
#     ["MuonEG__Run2016F", 10, 100],
#     ["MuonEG__Run2016G", 10, 100]

#["ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8" , 10, 100],


#["SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016C-PromptReco-v20000", 10, 100],
#["SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016C-PromptReco-v20001", 10, 100, 1000],
#["SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016G-PromptReco-v10000", 10, 100],
#["SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016G-PromptReco-v10001", 10, 100, 1000],
#["SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016G-PromptReco-v10002", 10, 100, 2000],
#["SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016F-PromptReco-v10000", 10, 100],
#["SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016D-PromptReco-v20000", 10, 100],
#["SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016D-PromptReco-v20001", 10, 100, 1000],
#["SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016B-PromptReco-v20000", 10, 100],
#["SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016B-PromptReco-v20001", 10, 100, 1000],
#["SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016B-PromptReco-v20002", 10, 100, 2000],
#["SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016B-PromptReco-v20003", 10, 100, 3000],
#["SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016E-PromptReco-v20000", 10, 100],
#["SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016E-PromptReco-v20001", 10, 100, 1000],
#["SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016C-PromptReco-v20000", 10, 100],
#["SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016C-PromptReco-v20001", 10, 100, 1000],
#["SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016B-PromptReco-v20000", 10, 100],
#["SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016B-PromptReco-v20001", 10, 100, 1000],
#["SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016B-PromptReco-v20002", 10, 100, 2000],
#["SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016B-PromptReco-v20003", 10, 100, 3000],
#["SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016F-PromptReco-v10000", 10, 100],
#["SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016D-PromptReco-v20000", 10, 100],
#["SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016D-PromptReco-v20001", 10, 100, 1000],
#["SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016G-PromptReco-v10000", 10, 100],
#["SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016G-PromptReco-v10001", 10, 100, 1000],
#["SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016G-PromptReco-v10002", 10, 100, 2000],
#["SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016E-PromptReco-v20000", 10, 100],
#["SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016E-PromptReco-v20001", 10, 100, 1000],
["TT_TuneCUETP8M1_13TeV-powheg-pythia8VHBB_HEPPY_V24_TT_TuneCUETP8M1_13TeV-powheg-Py8__spr16MAv2-puspr16_HLT_80r2as_v14_ext3-v10000", 10, 100],
["TT_TuneCUETP8M1_13TeV-powheg-pythia8VHBB_HEPPY_V24_TT_TuneCUETP8M1_13TeV-powheg-Py8__spr16MAv2-puspr16_HLT_80r2as_v14_ext3-v10001", 10, 100, 1000],
["TT_TuneCUETP8M1_13TeV-powheg-pythia8VHBB_HEPPY_V24_TT_TuneCUETP8M1_13TeV-powheg-Py8__spr16MAv2-puspr16_HLT_80r2as_v14_ext3-v10002", 10, 100, 2000],

#["QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["WZ_TuneCUETP8M1_13TeV-pythia8VHBB_HEPPY_V24_WZ_TuneCUETP8M1_13TeV-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],

#["QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000", 10, 100],
#["WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000", 10, 100],
#["WJetsToLNu_HT-600To800TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000", 10, 100],
#["WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_t-channel_top_4f_leptonDecays_13TeV-powheg-Py8_TuneCUETP8M1__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["DYJetsToNuNu_PtZ-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8VHBB_HEPPY_V24_DYJetsToNuNu_PtZ-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["WJetsToLNu_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8VHBB_HEPPY_V24_WJetsToLNu_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],

#["METVHBB_HEPPY_V24_MET__Run2016E-PromptReco-v20000", 10, 100],
#["METVHBB_HEPPY_V24_MET__Run2016E-PromptReco-v20001", 10, 100, 1000],
#["METVHBB_HEPPY_V24_MET__Run2016B-PromptReco-v20000", 10, 100],
#["METVHBB_HEPPY_V24_MET__Run2016B-PromptReco-v20001", 10, 100, 1000],
#["METVHBB_HEPPY_V24_MET__Run2016B-PromptReco-v20003", 10, 100, 3000],
#["METVHBB_HEPPY_V24_MET__Run2016F-PromptReco-v10000", 10, 100],
#["METVHBB_HEPPY_V24_MET__Run2016F-PromptReco-v10001", 10, 100, 1000],
#["METVHBB_HEPPY_V24_MET__Run2016D-PromptReco-v20000", 10, 100],
#["METVHBB_HEPPY_V24_MET__Run2016D-PromptReco-v20001", 10, 100, 1000],
#["METVHBB_HEPPY_V24_MET__Run2016C-PromptReco-v20000", 10, 100],
#["METVHBB_HEPPY_V24_MET__Run2016C-PromptReco-v20001", 10, 100, 1000],
#["METVHBB_HEPPY_V24_MET__Run2016G-PromptReco-v10000", 10, 100],
#["METVHBB_HEPPY_V24_MET__Run2016G-PromptReco-v10001", 10, 100, 1000],
#["ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-Py8_TuneCUETP8M1__spr16MAv2-premix_withHLT_80r2as_v14_ext1-v10000", 10, 100],
#["WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_HLT_80r2as_v14_ext1-v10000", 10, 100],
#["ZZ_TuneCUETP8M1_13TeV-pythia8VHBB_HEPPY_V24_ZZ_TuneCUETP8M1_13TeV-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["ZJetsToNuNu_HT-400To600_13TeV-madgraphVHBB_HEPPY_V24_ZJetsToNuNu_HT-400To600_13TeV-madgraph__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000", 10, 100],
#["ZJetsToNuNu_HT-400To600_13TeV-madgraphVHBB_HEPPY_V24_ZJetsToNuNu_HT-400To600_13TeV-madgraph__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000", 10, 100],
#["ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_tW_top_5f_inclusiveDecays_13TeV-powheg-Py8_TuneCUETP8M1__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v20000", 10, 100],
#["DYJetsToNuNu_BGenFilter_Zpt-40toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_DYJetsToNuNu_BGenFilter_Zpt-40toInf_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v20000", 10, 100],
#["ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8VHBB_HEPPY_V24_ZH_HToBB_ZToNuNu_M125_13TeV_powheg_Py8__spr16MAv2-puspr16_HLT_80r2as_v14_ext1-v10000", 10, 100],
#["WW_TuneCUETP8M1_13TeV-pythia8VHBB_HEPPY_V24_WW_TuneCUETP8M1_13TeV-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["ZJetsToNuNu_HT-100To200_13TeV-madgraphVHBB_HEPPY_V24_ZJetsToNuNu_HT-100To200_13TeV-madgraph__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000", 10, 100],
#["ZJetsToNuNu_HT-100To200_13TeV-madgraphVHBB_HEPPY_V24_ZJetsToNuNu_HT-100To200_13TeV-madgraph__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8VHBB_HEPPY_V24_WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-Py8__spr16MAv2-puspr16_HLT_80r2as_v14_ext1-v10000", 10, 100],
#["ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-Py8_TuneCUETP8M1__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["ZJetsToNuNu_HT-200To400_13TeV-madgraphVHBB_HEPPY_V24_ZJetsToNuNu_HT-200To400_13TeV-madgraph__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["ZJetsToNuNu_HT-200To400_13TeV-madgraphVHBB_HEPPY_V24_ZJetsToNuNu_HT-200To400_13TeV-madgraph__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000", 10, 100],
#["ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8_CUETP8M1DownVHBB_HEPPY_V24_ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_Py8_CUETP8M1Down__spr16MAv2-puspr16_HLT_80r2as_v14-v10000", 10, 100],
#["QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000", 10, 100],
#["QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v30000", 10, 100],
#["WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8VHBB_HEPPY_V24_WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["DYJetsToNuNu_PtZ-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8VHBB_HEPPY_V24_DYJetsToNuNu_PtZ-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8VHBB_HEPPY_V24_WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["WplusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8VHBB_HEPPY_V24_WplusH_HToBB_WToLNu_M125_13TeV_powheg_Py8__spr16MAv2-puspr16_HLT_80r2as_v14-v10000", 10, 100],
#["QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000", 10, 100],
#["QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8VHBB_HEPPY_V24_WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_Py8__spr16MAv2-puspr16_HLT_80r2as_v14-v10000", 10, 100],
#["WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000", 10, 100],
#["WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v20000", 10, 100],
#["ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-Py8_TuneCUETP8M1__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000", 10, 100],
#["DYJetsToNuNu_PtZ-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8VHBB_HEPPY_V24_DYJetsToNuNu_PtZ-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["WJetsToLNu_BGenFilter_Wpt-40toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_BGenFilter_Wpt-40toInf_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000", 10, 100],
#["QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000", 10, 100],
#["WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-Py8_TuneCUETP8M1__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8VHBB_HEPPY_V24_ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_Py8__spr16MAv2-puspr16_HLT_80r2as_v14-v10000", 10, 100],
#["ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8VHBB_HEPPY_V24_ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_Py8__spr16MAv2-puspr16_HLT_80r2as_v14-v10000", 10, 100],
#["ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8VHBB_HEPPY_V24_ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_Py8__spr16MAv2-puspr16_HLT_80r2as_v14_ext1-v10000", 10, 100],
#["ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8VHBB_HEPPY_V24_ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_Py8__spr16MAv2-puspr16_HLT_80r2as_v14_ext2-v10000", 10, 100],
#["ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_herwigppVHBB_HEPPY_V24_ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_herwigpp__spr16MAv2-puspr16_HLT_80r2as_v14-v10000", 10, 100],
#["QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000", 10, 100],
#["QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v20000", 10, 100],
#["WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000", 10, 100],
#["WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["WminusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8VHBB_HEPPY_V24_WminusH_HToBB_WToLNu_M125_13TeV_powheg_Py8__spr16MAv2-puspr16_HLT_80r2as_v14-v10000", 10, 100],
#["QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000", 10, 100],
#["QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["WJetsToLNu_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8VHBB_HEPPY_V24_WJetsToLNu_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8VHBB_HEPPY_V24_WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["ZJetsToNuNu_HT-1200To2500_13TeV-madgraphVHBB_HEPPY_V24_ZJetsToNuNu_HT-1200To2500_13TeV-madgraph__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["ZJetsToNuNu_HT-1200To2500_13TeV-madgraphVHBB_HEPPY_V24_ZJetsToNuNu_HT-1200To2500_13TeV-madgraph__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000", 10, 100],
#["DYJetsToNuNu_PtZ-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8VHBB_HEPPY_V24_DYJetsToNuNu_PtZ-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["ZJetsToNuNu_HT-600To800_13TeV-madgraphVHBB_HEPPY_V24_ZJetsToNuNu_HT-600To800_13TeV-madgraph__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8_CUETP8M1UpVHBB_HEPPY_V24_ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_Py8_CUETP8M1Up__spr16MAv2-puspr16_HLT_80r2as_v14-v10000", 10, 100],
#["ZJetsToNuNu_HT-800To1200_13TeV-madgraphVHBB_HEPPY_V24_ZJetsToNuNu_HT-800To1200_13TeV-madgraph__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v30000", 10, 100],
#["ZJetsToNuNu_HT-2500ToInf_13TeV-madgraphVHBB_HEPPY_V24_ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["WBJetsToLNu_Wpt-40toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WBJetsToLNu_Wpt-40toInf_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["ggZH_HToBB_ZToNuNu_M125_13TeV_amcatnlo_pythia8VHBB_HEPPY_V24_ggZH_HToBB_ZToNuNu_M125_13TeV_amcatnlo_Py8__spr16MAv2-puspr16_HLT_80r2as_v14-v10000", 10, 100],

#["WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v30000", 10, 100],

#["WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000", 10, 100],
#["ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-Py8_TuneCUETP8M1__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],
#["ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-Py8_TuneCUETP8M1__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000", 10, 100],


    ]:
    for it in xrange(sample[2]):
        postfix = it+1
        first = it*sample[1]+1 + (sample[3] if len(sample)>3 else 0)
        last = (it+1)*sample[1] + (sample[3] if len(sample)>3 else 0)
        print sample[0],sample[1], last, postfix
        submit(sample[0], first if sample[1]>=0 else -1, last, postfix)
        #exit(1)


