#!c:/usr/bin/python.exe -u

# Rev1.5: Adds multiple file selection functionality to tkinter, i.e. highlight many files at once
#           for selection
 
# Import all needed modules
import tkinter
from tkinter import *
import tkFileDialog, tkMessageBox
import subprocess, re
import gzip

# Setup the Tk environment
root = Tk()
# Hide the Tk screen since it isn't used
root.withdraw()

# Open the path for the temp file so it can be written
hndl = open('tmpjmpfile.txt', 'w')
tmpfilepath = hndl.name

# This method creates the data header from either a txt file or a gzip file
def parseheader(filename):
    if filename.endswith('.gz'):
        datahndl = gzip.open(filename, 'r')
    else:
        datahndl = open(filename, 'rt')
    counter = 0
    for eachline in datahndl:
        if counter > 0:
            break
        splitline = eachline.strip().split(',')
        try:
            splitline[1]
            if 'Chamber' in splitline[1]:
                splitline[0] = "Time"
                hndl.write('Date-time, ' + ','.join(splitline) + '\n')
                counter += 1
        except IndexError:
            pass
    datahndl.close()


# This method reads and writes all the data to the temp file from a txt file or a gzip file
def parsedata(filename):
    if filename.endswith('.gz'):
        datahndl = gzip.open(filename, 'r')
    else:
        datahndl = open(filename, 'rt')
    for eachline in datahndl:
        splitline = eachline.strip().split(',')
        if 'Log' in splitline[0]:
            date=re.search("\d*/\d*",splitline[0])
            date=date.group()
        try:
            splitline[1]
            if splitline[1].isdigit() and splitline[0]!='':
                hndl.write(date +'-'+ splitline[0] + ',' + ','.join(splitline) + '\n')
        except IndexError:
            pass
    datahndl.close()

# This method takes the temp data file from C:\util\tmp\ and opens it in JMP
def jmpopen(tmpfilepath):
	jmpfile = tmpfilepath
	jmppath = r'C:\Program Files\SAS\JMPPRO\11\jmp.exe'
	subprocess.call("%s %s" % (jmppath, jmpfile))
    
# This iterates over all the above methods in order to open and combine files
def main():
    counter=0
    # Obtain filnames from user via tkinter dialog box
    filelist = tkFileDialog.askopenfilenames(parent=root,initialdir="/Desktop",title='Please select files')
    #filelist = tkFileDialog.askopenfilenames(title='Please select files')
    #print type(filelist)    
    filelist = filelist.encode('ascii', 'ignore')
    #print filelist
    #print type(filelist)
    filelist = filelist.strip().split()
    filelist.reverse()
    #print filelist
    try:
        filelist[0]
    except:
        sys.exit(1)
    for filename in filelist:
        if counter == 0:
            parseheader(filename)
            parsedata(filename)
            counter+= 1
        else:
            parsedata(filename)
            counter += 1

# Run the main method which calls all other methods with logic
main()

# Close the temp file that parsed data was written to
hndl.close()

# Open temp data file in JMP
jmpopen(tmpfilepath)



