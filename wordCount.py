import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program
# checks program is called correctly
if len(sys.argv) is not 3:
    print("Correct usage: wordCountTest.py <input text file> <output file>")
    exit()

inputFname = sys.argv[1]
outputFname = sys.argv[2]
#master dictionary
master = {}
with open(inputFname, 'r') as inputFile:
    for line in inputFile:
        # get rid of newline characters, converts all characters to lowercase and gets rid of punctiation
        line = line.strip()
        line = line.lower()
        line = line.replace(',','')
        line = line.replace('.','')
        line = line.replace(':','')
        line = line.replace(';','')
        line = line.replace('"','')
        # split line on whitespace and punctuation
        words = re.split('[ \t]', line)
        #checks if the word is missing to add it, otherwise it just increments it
        for word in words: 
        	if word not in master:
        		master[word] = 1
        	else:
        		master[word] +=1
        
#writes the dictionary into a .txt file	
with open(outputFname, 'w') as f:
    for key, value in list(master.items()):
    	f.write('%s %s\n' % (key, value))
   