#! /bin/bash
#
#$Author: ee364f04 $
#$Date: 2013-01-17 00:04:14 -0500 (Thu, 17 Jan 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab02/line_num.bash $
#$Revision: 48318 $

File=$@
a=1

if (($# != 1))
then
    echo "Invalid entry"
    exit 0
elif [[ ! -e $File ]] && [[ ! -r $File ]]
then
    echo "Cannot read $File"
    exit 0
fi

while read line
do
    echo "$a: $line"
    ((a=a+1))
done < $File

exit 0
