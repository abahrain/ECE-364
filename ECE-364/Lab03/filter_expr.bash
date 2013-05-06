#! /bin/bash
#
#$Author: ee364f04 $
#$Date: 2013-01-24 11:02:54 -0500 (Thu, 24 Jan 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Lab03/filter_expr.bash $
#$Revision: 48877 $

File=$@
t=$3
b=$2
g=0

if (($# != 3))
then
    echo "usage: filter_expr.bash $1 $2 $3"
    exit 1
elif [[ ! -e $1 ]] || [[ ! -r $1 ]]
then
    echo "error: $1 is not readable"
    exit 1
elif (($3 < $2))
then
    echo "error: min was greater than max"
    exit 2
fi


while read line number
do
    set $number

    for N in $number
    do
        if (($N > $b)) && (($N < $t))
        then
            g=1
        fi
    done
    if (($g==1))
    then
        printf "$line "
    fi

    for N in $number
    do
        
        if (($N > $b)) && (($N < $t))
        then
            printf "$N "
        fi
    done

    if (($g==1))
    then
        printf "\n"
    fi
    g=0

done < $1

exit 0
