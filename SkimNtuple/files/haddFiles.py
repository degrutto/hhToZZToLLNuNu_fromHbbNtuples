import os
file = [
"WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",
"WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",
"QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",
"QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",
"ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_t-channel_top_4f_leptonDecays_13TeV-powheg-Py8_TuneCUETP8M1__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",
"QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",
"ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-Py8_TuneCUETP8M1__spr16MAv2-premix_withHLT_80r2as_v14_ext1-v10000",
"QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",
"ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_tW_top_5f_inclusiveDecays_13TeV-powheg-Py8_TuneCUETP8M1__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v20000",
"ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-Py8_TuneCUETP8M1__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",
"QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",
"QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v30000",
"QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",
"QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",
"WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",
"WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v20000",
"ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-Py8_TuneCUETP8M1__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",
"QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",
"QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",
"QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",
"QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",
"WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",
"WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",
"ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-Py8_TuneCUETP8M1__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",
"QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",
"QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v20000",
"QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",
"QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",
"ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-Py8_TuneCUETP8M1__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",
"ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-Py8_TuneCUETP8M1__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",


#"ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8#",
#"SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016C-PromptReco-v20000",#",
#"SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016C-PromptReco-v20001#",
#"SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016G-PromptReco-v10000",#",
#"SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016G-PromptReco-v10001#",
#"SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016G-PromptReco-v10002#",
#"SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016F-PromptReco-v10000",#",
#"SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016D-PromptReco-v20000",#",
#"SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016D-PromptReco-v20001#",
#"SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016B-PromptReco-v20000",#",
#"SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016B-PromptReco-v20001#",
#"SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016B-PromptReco-v20002#",
#"SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016B-PromptReco-v20003#",
#"SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016E-PromptReco-v20000",#",
#"SingleMuonVHBB_HEPPY_V24_SingleMuon__Run2016E-PromptReco-v20001#",
#"SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016C-PromptReco-v20000",#",
#"SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016C-PromptReco-v20001#",
#"SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016B-PromptReco-v20000",#",
#"SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016B-PromptReco-v20001#",
#"SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016B-PromptReco-v20002#",
#"SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016B-PromptReco-v20003#",
#"SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016F-PromptReco-v10000",#",
#"SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016D-PromptReco-v20000",#",
#"SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016D-PromptReco-v20001#",
#"SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016G-PromptReco-v10000",#",
#"SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016G-PromptReco-v10001#",
#"SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016G-PromptReco-v10002#",
#"SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016E-PromptReco-v20000",#",
#"SingleElectronVHBB_HEPPY_V24_SingleElectron__Run2016E-PromptReco-v20001#",
#"TT_TuneCUETP8M1_13TeV-powheg-pythia8VHBB_HEPPY_V24_TT_TuneCUETP8M1_13TeV-powheg-Py8__spr16MAv2-puspr16_HLT_80r2as_v14_ext3-v10000",#",
#"TT_TuneCUETP8M1_13TeV-powheg-pythia8VHBB_HEPPY_V24_TT_TuneCUETP8M1_13TeV-powheg-Py8__spr16MAv2-puspr16_HLT_80r2as_v14_ext3-v10001#",
#"TT_TuneCUETP8M1_13TeV-powheg-pythia8VHBB_HEPPY_V24_TT_TuneCUETP8M1_13TeV-powheg-Py8__spr16MAv2-puspr16_HLT_80r2as_v14_ext3-v10002#",
#"QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"WZ_TuneCUETP8M1_13TeV-pythia8VHBB_HEPPY_V24_WZ_TuneCUETP8M1_13TeV-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",#",
#"WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",#",
#"WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",#",
#"WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_t-channel_top_4f_leptonDecays_13TeV-powheg-Py8_TuneCUETP8M1__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"DYJetsToNuNu_PtZ-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8VHBB_HEPPY_V24_DYJetsToNuNu_PtZ-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"WJetsToLNu_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8VHBB_HEPPY_V24_WJetsToLNu_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"METVHBB_HEPPY_V24_MET__Run2016E-PromptReco-v20000",#",
#"METVHBB_HEPPY_V24_MET__Run2016E-PromptReco-v20001#",
#"METVHBB_HEPPY_V24_MET__Run2016B-PromptReco-v20000",#",
#"METVHBB_HEPPY_V24_MET__Run2016B-PromptReco-v20001#",
#"METVHBB_HEPPY_V24_MET__Run2016B-PromptReco-v20003#",
#"METVHBB_HEPPY_V24_MET__Run2016F-PromptReco-v10000",#",
#"METVHBB_HEPPY_V24_MET__Run2016F-PromptReco-v10001#",
#"METVHBB_HEPPY_V24_MET__Run2016D-PromptReco-v20000",#",
#"METVHBB_HEPPY_V24_MET__Run2016D-PromptReco-v20001#",
#"METVHBB_HEPPY_V24_MET__Run2016C-PromptReco-v20000",#",
#"METVHBB_HEPPY_V24_MET__Run2016C-PromptReco-v20001#",
#"METVHBB_HEPPY_V24_MET__Run2016G-PromptReco-v10000",#",
#"METVHBB_HEPPY_V24_MET__Run2016G-PromptReco-v10001#",
#"ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-Py8_TuneCUETP8M1__spr16MAv2-premix_withHLT_80r2as_v14_ext1-v10000",#",
#"WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_HLT_80r2as_v14_ext1-v10000",#",
#"ZZ_TuneCUETP8M1_13TeV-pythia8VHBB_HEPPY_V24_ZZ_TuneCUETP8M1_13TeV-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT300to500_BGenFilter_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"ZJetsToNuNu_HT-400To600_13TeV-madgraphVHBB_HEPPY_V24_ZJetsToNuNu_HT-400To600_13TeV-madgraph__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",#",
#"ZJetsToNuNu_HT-400To600_13TeV-madgraphVHBB_HEPPY_V24_ZJetsToNuNu_HT-400To600_13TeV-madgraph__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",#",
#"ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_tW_top_5f_inclusiveDecays_13TeV-powheg-Py8_TuneCUETP8M1__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v20000",#",
#"DYJetsToNuNu_BGenFilter_Zpt-40toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_DYJetsToNuNu_BGenFilter_Zpt-40toInf_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v20000",#",
#"ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8VHBB_HEPPY_V24_ZH_HToBB_ZToNuNu_M125_13TeV_powheg_Py8__spr16MAv2-puspr16_HLT_80r2as_v14_ext1-v10000",#",
#"WW_TuneCUETP8M1_13TeV-pythia8VHBB_HEPPY_V24_WW_TuneCUETP8M1_13TeV-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"ZJetsToNuNu_HT-100To200_13TeV-madgraphVHBB_HEPPY_V24_ZJetsToNuNu_HT-100To200_13TeV-madgraph__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",#",
#"ZJetsToNuNu_HT-100To200_13TeV-madgraphVHBB_HEPPY_V24_ZJetsToNuNu_HT-100To200_13TeV-madgraph__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8VHBB_HEPPY_V24_WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-Py8__spr16MAv2-puspr16_HLT_80r2as_v14_ext1-v10000",#",
#"ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-Py8_TuneCUETP8M1__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"ZJetsToNuNu_HT-200To400_13TeV-madgraphVHBB_HEPPY_V24_ZJetsToNuNu_HT-200To400_13TeV-madgraph__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"ZJetsToNuNu_HT-200To400_13TeV-madgraphVHBB_HEPPY_V24_ZJetsToNuNu_HT-200To400_13TeV-madgraph__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",#",
#"ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8_CUETP8M1DownVHBB_HEPPY_V24_ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_Py8_CUETP8M1Down__spr16MAv2-puspr16_HLT_80r2as_v14-v10000",#",
#"QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",#",
#"QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v30000",#",
#"WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8VHBB_HEPPY_V24_WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"DYJetsToNuNu_PtZ-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8VHBB_HEPPY_V24_DYJetsToNuNu_PtZ-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8VHBB_HEPPY_V24_WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"WplusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8VHBB_HEPPY_V24_WplusH_HToBB_WToLNu_M125_13TeV_powheg_Py8__spr16MAv2-puspr16_HLT_80r2as_v14-v10000",#",
#"QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",#",
#"QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8VHBB_HEPPY_V24_WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_Py8__spr16MAv2-puspr16_HLT_80r2as_v14-v10000",#",
#"WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",#",
#"WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v20000",#",
#"ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-Py8_TuneCUETP8M1__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",#",
#"DYJetsToNuNu_PtZ-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8VHBB_HEPPY_V24_DYJetsToNuNu_PtZ-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"WJetsToLNu_BGenFilter_Wpt-40toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_BGenFilter_Wpt-40toInf_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",#",
#"QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",#",
#"WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-Py8_TuneCUETP8M1__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8VHBB_HEPPY_V24_ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_Py8__spr16MAv2-puspr16_HLT_80r2as_v14-v10000",#",
#"ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8VHBB_HEPPY_V24_ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_Py8__spr16MAv2-puspr16_HLT_80r2as_v14-v10000",#",
#"ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8VHBB_HEPPY_V24_ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_Py8__spr16MAv2-puspr16_HLT_80r2as_v14_ext1-v10000",#",
#"ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8VHBB_HEPPY_V24_ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_Py8__spr16MAv2-puspr16_HLT_80r2as_v14_ext2-v10000",#",
#"ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_herwigppVHBB_HEPPY_V24_ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_herwigpp__spr16MAv2-puspr16_HLT_80r2as_v14-v10000",#",
#"QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",#",
#"QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v20000",#",
#"WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",#",
#"WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"WminusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8VHBB_HEPPY_V24_WminusH_HToBB_WToLNu_M125_13TeV_powheg_Py8__spr16MAv2-puspr16_HLT_80r2as_v14-v10000",#",
#"QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",#",
#"QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"WJetsToLNu_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8VHBB_HEPPY_V24_WJetsToLNu_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8VHBB_HEPPY_V24_WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"ZJetsToNuNu_HT-1200To2500_13TeV-madgraphVHBB_HEPPY_V24_ZJetsToNuNu_HT-1200To2500_13TeV-madgraph__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"ZJetsToNuNu_HT-1200To2500_13TeV-madgraphVHBB_HEPPY_V24_ZJetsToNuNu_HT-1200To2500_13TeV-madgraph__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",#",
#"DYJetsToNuNu_PtZ-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8VHBB_HEPPY_V24_DYJetsToNuNu_PtZ-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"ZJetsToNuNu_HT-600To800_13TeV-madgraphVHBB_HEPPY_V24_ZJetsToNuNu_HT-600To800_13TeV-madgraph__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8_CUETP8M1UpVHBB_HEPPY_V24_ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_Py8_CUETP8M1Up__spr16MAv2-puspr16_HLT_80r2as_v14-v10000",#",
#"ZJetsToNuNu_HT-800To1200_13TeV-madgraphVHBB_HEPPY_V24_ZJetsToNuNu_HT-800To1200_13TeV-madgraph__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v30000",#",
#"ZJetsToNuNu_HT-2500ToInf_13TeV-madgraphVHBB_HEPPY_V24_ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"WBJetsToLNu_Wpt-40toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WBJetsToLNu_Wpt-40toInf_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"ggZH_HToBB_ZToNuNu_M125_13TeV_amcatnlo_pythia8VHBB_HEPPY_V24_ggZH_HToBB_ZToNuNu_M125_13TeV_amcatnlo_Py8__spr16MAv2-puspr16_HLT_80r2as_v14-v10000",#",
#"WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v30000",#",
#"WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8VHBB_HEPPY_V24_WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-Py8__spr16MAv2-puspr16_80r2as_2016_MAv2_v0_ext1-v10000",#",
#"ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-Py8_TuneCUETP8M1__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",
#"ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1VHBB_HEPPY_V24_ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-Py8_TuneCUETP8M1__spr16MAv2-puspr16_80r2as_2016_MAv2_v0-v10000",#",


]

for f in file:
   print f
   name = f+'.root'
   os.system("hadd  -f %s %s/tree*.root"%(name,f))


