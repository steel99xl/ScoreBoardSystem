import os
import time
os.system("cat *.txt > TABLE/TMP.table")
f = open("TABLE/TMP.table")
TMP = f.read()
t = open("TABLE/render.txt","w+")
t.write(TMP.replace('|',"   "))
t.close
f.close
time.sleep(1)
os.system("cat TABLE/logo.txt")
os.system("cat TABLE/TABLE.txt")
