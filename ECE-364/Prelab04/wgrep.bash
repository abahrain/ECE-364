#! /bin/bash
#
#$Author: ee364f04 $
#$Date: 2013-01-31 00:02:23 -0500 (Thu, 31 Jan 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab04/wgrep.bash $
#$Revision: 49610 $

F=$@
d=0

if (($# != 2))
then
    echo "Usage: wgrep.bash $1 $2"
    exit 1
elif [[ ! -e $2 ]] && [[ ! -r $2 ]]
then
    echo "Error: $1 is not readable"
    exit 1
fi

while read line
do
    d=$[$d+1]
    if $1 =~ $line
    then
        head -l{$d-1} $line
        echo $line
        cut -l{d+1} $line
    fi
done < $2

exit 0
