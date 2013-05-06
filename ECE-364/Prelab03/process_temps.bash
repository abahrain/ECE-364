#! /bin/bash
#
#$Author: ee364f04 $
#$Date: 2013-01-23 22:31:47 -0500 (Wed, 23 Jan 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab03/process_temps.bash $
#$Revision: 48809 $

F=$@
d=0
sum=0
a=0
t=0

if (($# < 1))
then
    echo "usage: process_temps.bash $File"
    exit 1
elif [[ ! -r $1 ]]
then
    echo "Error: $1 is not a readable file."
    exit 2
fi

while read time name
do
    set $name

   if (($t>0))
   then
       for N in ${name[*]}
       do
           sum=$(($sum + $N))
           d=$(($d+1))
           a=$(($sum/$d))
       done
       echo "Average temperature for time $time was $a C."
   fi
   t=1
   sum=0
   d=0
   a=0
done <$1

exit 0
