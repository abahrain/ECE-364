#! /bin/bash
#
#$Author: ee364f04 $
#$Date: 2013-01-16 23:57:44 -0500 (Wed, 16 Jan 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab02/sensor_sum.sh $
#$Revision: 48314 $

File=$@
sum=0

if (($# != 1))
then
    echo "usage: $File sensor_sum.sh"
    exit 0
elif [[ ! -e $File ]] && [[ ! -r $File ]]
then
    echo "$File is not a readable file!"
    exit 0
fi

while read line sum1 sum2 sum3
do
    sum=$(($sum1+$sum2+$sum3))
    echo $line |cut -d'.' -f1| head -c2
    echo " $sum"
done < $File

exit 0

