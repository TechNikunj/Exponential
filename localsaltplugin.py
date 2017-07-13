#!/user/bin/python

import os, sys
import time

written = "test"
cmd = 'echo "test" >> testtry.txt'
os.system(cmd)
print "target file written"

print "\nAllowing Salt to revert changes . . . \n\n"
time.sleep(2)

print "checking file"
fh = open ( 'testtry.txt',"rw" )
linelist=fh.readlines()


linelist[-1] = linelist[-1].strip('\n')

#print linelist[-1]
#print written

booltest = linelist[-1] == written

if booltest:
	print 'File modification not reverted, salt not running'
else:
	print 'File modification reverted, salt is running'

fh.close()
