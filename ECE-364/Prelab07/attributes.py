#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-02-17 16:11:17 -0500 (Sun, 17 Feb 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab07/attributes.py $
#$Revision: 52017 $

import sys
import os

n=sys.argv[1:]

if len(sys.argv) !=2:
    print " Usage: ./attributes.py"
    sys.exit(1)

if os.access(n[0], os.R_OK):
    print "%s esixts" % (n[0],)
else:
    print "%s does not exist" % (n[0])
    sys.exit(1)

if os.path.isdir(n[0]):
    print "%s is a directory" % (n[0],)
else:
    print "%s is not a directory" % (n[0],)

if os.path.isfile(n[0]):
    print "%s is an ordinary file" % (n[0],)
else:
    print "%s is not an ordinary file" % (n[0],)

if os.access(n[0],os.R_OK):
    print "%s is readable" % (n[0],)
else:
    print "%s is not readable" % (n[0],)

if os.access(n[0],os.W_OK):
    print "%s is writable" % (n[0],)
else:
    print "%s is not writable" % (n[0],)

if os.access(n[0], os.X_OK):
    print "%s is executable" % (n[0],)
else:
    print "%s is not executable" % (n[0],)

sys.exit(0)
