import  os
import subprocess

#"MET_Run2016B_0": [pisa_lfn + "/MET/VHBB_HEPPY_V23_MET__Run2016B-PromptReco-v2/160717_203439/0000/", -1 ],
with open('filesV24_all.txt', 'r') as f:
    for file in f:
        s = file.rstrip().split('/')
        if len(s)>1:
            #print '"'+s[5]+s[6]+s[8]+'": [pisa_lfn + "' + '/'.join(s[5:])+'/", -1 ],'  # for samples.py
            #print s[8]
            if s[8] == '0000':
                print '["'+s[5]+s[6]+s[8]+'", 10, 100],' # for submit.py
            if s[8] == '0001':
                print '["'+s[5]+s[6]+s[8]+'", 10, 100, 1000],' # for submit.py
            if s[8] == '0003':
                print '["'+s[5]+s[6]+s[8]+'", 10, 100, 3000],' # for submit.py
            if s[8] == '0004':
                print '["'+s[5]+s[6]+s[8]+'", 10, 100, 4000],' # for submit.py

#                ["MuonEG__Run2016G", 10, 100]     

#            print '/'.join(s[5:])
#"MET_Run2016B_0": [pisa_lfn + "/MET/VHBB_HEPPY_V23_MET__Run2016B-PromptReco-v2/160717_203439/0000/", -1 ],              
