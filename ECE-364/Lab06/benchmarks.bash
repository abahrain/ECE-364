#! /bin/bash
#
#$Author: ee364f04 $
#$Date: 2013-02-14 11:17:47 -0500 (Thu, 14 Feb 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Lab06/benchmarks.bash $
#$Revision: 51908 $

f=$@

if (( $# < 2))
then
    echo "usage: benchmarks.bash <delim> <name1> <name2> ... [nameN]"
    exit 1
fi

for i in $2 $3 $4 $5 $6
do
    algorithm.py $i 1

    if (( $? !=0 ))
    then
        echo "warning: skipping bad algorithm $i" >&2
    else
        algorithm.py $i 10 >run[0]
        algorithm.py $i 100 >run[1]
        algorithm.py $i 250 >run[2]
        algorithm.py $i 500 >run[3]
        algorithm.py $i 1000 >run[4]
        algorithm.py $i 1500 >run[5]

        echo "$i $1 ${run[0]} $1 ${run[1]} $1 ${run[2]} $1 ${run[3]} $1 ${run[4]} $1 ${run[5]}" >&1 
    fi
done

exit 0
