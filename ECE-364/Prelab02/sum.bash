#! /bin/bash
#
#$Author: ee364f04 $
#$Date: 2013-01-17 00:05:00 -0500 (Thu, 17 Jan 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab02/sum.bash $
#$Revision: 48319 $

I=$@ #input
X=0

while (($# !=0))
do
    ((X=X+I))
    echo "$X"
    shift
done

exit 0
