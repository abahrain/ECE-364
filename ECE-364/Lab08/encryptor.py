#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-02-28 11:32:43 -0500 (Thu, 28 Feb 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Lab08/encryptor.py $
#$Revision: 53703 $

import sys

n=sys.argv[1:]
out=""

if len(sys.argv) != 4:
    print "Usage: encryptor.py <input_file_name> <password> <mode>"
    sys.exit(1)
try:
    fp=open(sys.argv[1], "r")
except IOError as e:
    print "error: %s is not readable" % (sys.argv[1],)
    sys.exit (2)
if sys.argv[3] == "E":
    for line in fp:
        out=strip_invalid_characters(line)
        vign_encrypt(out,password)
else:
    print "error: invalid mode."
    sys.exit(3)

if sys.argv[3] == "D":
        for line in fp:
                    out=strip_invalid_characters(line)
                            vign_decrypt(out,password)
                        else:
                                print "error: invalid mode."
                                    sys.exit(3)

sys.exit(0)
