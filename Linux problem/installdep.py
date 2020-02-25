import subprocess
import sys
import json

#load Json file from File name passed as command line argument
with open(str(sys.argv[1])) as f:
  dep = json.load(f)
failed_pkgs = []
for item in dep["Dependencies"].items():
      out = subprocess.run("pip install " + str(item[0]) + "==" + str(item[1]), shell=True)
      if(out.returncode!=0):
            #error
            # check_returncode()
            failed_pkgs.append(item)
      else:
            continue


if(len(failed_pkgs) == 0):
      print("Success!")
else:
      print("Failed to install following packages...")
      for pkg in failed_pkgs:
            print(pkg)