import re
import sys

f = open(sys.argv[1],'r')
fileString = f.read()
f.close

finalCount={}
for word in re.split('\W+', fileString):
    finalCount[word] = finalCount.get(word,0)+1

f = open(sys.argv[2],'w')
f.write(str(finalCount))