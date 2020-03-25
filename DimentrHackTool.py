#!/data/data/com.termux/files/usr/bin/bash 

import subprocess

print ("=================")
print ("|DimentrHackTool|")
print ("=================")
print ("")
print ("")
print ("")

print("1. Fishing(VK)")
print("2. DDos-Attack")
print("3. MetaSploit(Не Работает)")
print("4. QiwiSoft")
print("5. Impulse")
print("6. instashell")
print("")

inp = input(">> ")

if inp == "1": 
  subprocess.call("git clone https://github.com/foxlitegor/fisher", shell=True)
  
if inp == "2":
  subprocess.call("git clone https://github.com/cyweb/hammer", shell=True)

if inp == "3":
  subprocess.call("", shell=True)
 
if inp == "4":
  subprocess.call("pip install SimpleQIWI", shell=True)
  subprocess.call("git clone https://github.com/SeRgEy2701/QiwiSoft.git", shell=True)
 
if inp =="5":
  subprocess.call("git clone https://github.com/LimerBoy/Impulse", shell=True)
  
if inp == "6":
   subprocess.call("pkg install tor curl openssl*", shell=True)
   subprocess.call("git clone https://github.com/thelinuxchoice/instashell", shell=True)