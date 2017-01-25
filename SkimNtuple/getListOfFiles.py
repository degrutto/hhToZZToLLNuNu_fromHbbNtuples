import  os
import subprocess

#files = str(subprocess.check_output("xrdfs t3se01.psi.ch ls /store/user/perrozzi/VHBBHeppyV23", shell=True))
files = str(subprocess.check_output("xrdfs stormgf1.pi.infn.it ls  /store/user/arizzi/VHBBHeppyV24/", shell=True)) 
for file in files.split("\n"):
#  print file
  if 'arizzi' in file:
#    level1 = str(subprocess.check_output("xrdfs t3se01.psi.ch ls %s" %file , shell=True))
    level1 = str(subprocess.check_output("xrdfs  stormgf1.pi.infn.it ls %s" %file , shell=True))
#  print level1 
    for l1 in level1.split("\n"):  
      level2 = str(subprocess.check_output("xrdfs  stormgf1.pi.infn.it ls %s" %l1 , shell=True))
      if '1609' in  level2:
        for l2 in level2.split("\n"):
          level3 = str(subprocess.check_output("xrdfs stormgf1.pi.infn.it ls %s" %l2 , shell=True))
          if 'arizzi' in level3:
            print level3
