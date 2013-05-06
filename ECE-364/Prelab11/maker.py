#! /usr/bin/env python2.6
#
#$Author$
#$Date$
#$HeadURL$
#$Revision$

import sys

sourcefile = 'output.txt'
txt_file = open(sourcefile)
source_content = txt_file.read()
for i in range(1,6):
    filenum = str(i)
    destinationfile='output_'+filenum+'.txt'
    target = open (destinationfile, 'w') ## a will append, w will over-write 
    target.write(source_content)
    #print "we have added those text to the file"
    target.close()

sys.exit(0)
