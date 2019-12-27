#gadgetmiser's idempotent splitter

import os, sys
from pathlib import Path
from shutil import move

import pdb


wd = os.getcwd()
dirs = os.listdir()
lastitemindex = len(dirs) - 1


drive = wd.split(':')[0]
results = ':\\c64Romset_output\\'
filesperfolder = 255
letterstodisplay = 15

firstfn_2l = dirs[0][:letterstodisplay].split("(")[0].strip().upper()[:4]
lastfn_2l = dirs[:filesperfolder - 1][-1][:letterstodisplay].split("(")[0].strip().upper()[:4]

firsttarget = (firstfn_2l + " to " + lastfn_2l).strip()
os.mkdir(drive + results)
os.mkdir(drive + results + firsttarget)
log_output = open(drive + results + "log_output.txt","w+")


tally = 0
counter = 0
target = firsttarget

#pdb.set_trace()

for folder in dirs:
    tally += 1

    if counter == filesperfolder:
            p1 = folder[:letterstodisplay].split("(")[0].upper().strip()[:4]
            folderpos = dirs.index(folder)
            try:
                p2 =  dirs[folderpos + filesperfolder - 1][:letterstodisplay].split("(")[0].upper().strip()[:4]
            except IndexError:
                p2 =  dirs[lastitemindex][:letterstodisplay].split("(")[0].upper().strip()[:4]
            newdir = (p1 + " to " + p2).strip()
            print(str(tally) + " files processed ... making new dir called: " + newdir)
            target = newdir
            counter = 0
    newfname = folder.split("(")[0].strip()
    move(folder, drive + results + target + "\\" + newfname)
    print("Moved " + folder + " to " + drive + results + target + " as " + newfname)
    log_output.write("\n" + "Moved " + folder + " to: ** " + target + " **" + " as " + newfname)
    counter += 1
    
print(str(tally) + ' files processed ... ALL DONE')
log_output.write("\n" + str(tally) + " files processed.")
log_output.close()