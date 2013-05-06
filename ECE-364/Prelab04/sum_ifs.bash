#! /bin/bash
#
#$Author: ee364f04 $
#$Date: 2013-01-30 19:59:56 -0500 (Wed, 30 Jan 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab04/sum_ifs.bash $
#$Revision: 49589 $

F=$@
sum=0
d=0

if (($# != 1))
then
    echo "Usage: sum_ifs.bash <filename>"
    exit 1
elif [[ ! -e $1 ]] && [[ ! -r $1 ]]
then
    echo "Error: $1 is not readable"
    exit 1
fi

IFS=':'
while read -a line
do
    d=$[$d+1]
    set $line
    for n in $line
    do
        n=${n##.}
        sum=$[$sum+$n]
    done
    echo "Sum of line $d is $sum"
    sum=0
done < $1
exit 0
