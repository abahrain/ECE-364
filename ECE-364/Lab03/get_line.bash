#! /bin/bash
#
#$Author: ee364f04 $
#$Date: 2013-01-24 11:04:11 -0500 (Thu, 24 Jan 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Lab03/get_line.bash $
#$Revision: 48878 $

File=$@
t=0

if (($# != 2))
then
    echo "usage: get_line.bash $1 $2"
    exit 1
elif (($1 <= 0))
then
    echo "error: line number must be greater than zero"
    exit 2
fi

while read line
do
    if (($t == $(($1-1))))
    then
        echo $line
        exit 0
    fi
    t=$(($t+1))
done < $2

echo "error: $2 is shorter than $1 line(s)."
exit 2


