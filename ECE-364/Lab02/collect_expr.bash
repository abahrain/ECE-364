#! /bin/bash
#
#$Author: ee364f04 $
#$Date: 2013-01-17 11:05:35 -0500 (Thu, 17 Jan 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Lab02/collect_expr.bash $
#$Revision: 48395 $
Output=$1
File=$@
a=0
sum=0

if (($# < 2))
then
    echo "usage: collect_expr.bash $File"
    exit 1
elif [[ -e $1 ]]
then
    echo "$Output already exists."
    exit 2
fi

touch $1
shift

while [[ -e $1 ]]
do
    if [[ ! -r $1 ]]
    then
        echo "error: $(($#-1)) is not a readable file."
        exit 2
    fi

    while read name d1 d2 d3 d4 d5
    do
        sum=$(($d1+$d2+$d3+$d4+$d5))
        a=$(($sum/5))
        echo "$name $d1 $d2 $d3 $d4 $d5 $sum $a" >> $Output
    done < $1
    shift
done

exit 0
