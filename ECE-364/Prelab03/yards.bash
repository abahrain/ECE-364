#! /bin/bash
#
#$Author: ee364f04 $
#$Date: 2013-01-23 14:51:00 -0500 (Wed, 23 Jan 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab03/yards.bash $
#$Revision: 48775 $

File=$@
a=0
sum=0
M=0
d=0
sum2=0

if (($# != 1))
then
    echo "Usage: yards.bash <filename>"
     exit 0
elif [[ ! -e $File ]] && [[ ! -r $File ]]
then
     echo "Error: $File is not readable"
     exit 0
fi

while read name yards
do
    set $yards

    for N in $yards
    do
       sum=$(($sum + $N))
       sum2=$(($sum*$sum))
       d=$(($d+1))
       a=$(($sum/$d))
    done 
    
    if (($a > $M))
    then
        M=$a
    fi
    
    for i in $yards
    do  
        var=$(($var+$(($(($i-$a))*$(($i-$a))))))
    done
    var=$(($var/$d))
    echo "$name schools averaged $a yards with a variance of $var"
    d=0
    var=0
    sum=0
done < $File
echo "The largest average yardage was $M"
exit 0
