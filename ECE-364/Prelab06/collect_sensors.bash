#! /bin/bash
#
#$Author: ee364f04 $
#$Date: 2013-02-14 01:33:00 -0500 (Thu, 14 Feb 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab06/collect_sensors.bash $
#$Revision: 51882 $

f=$@
min=0
max=0
sum=0
avg=0
c=0

if (( $# != 1 ))
then
    echo "Usage: collect_sensors.bash <filename>"
    exit 1
elif [[ ! -r $1 ]]
then
    echo "Error: $1 is not a readable file"
    exit 1
fi

while read test extra
do
    test=${test%%-*}
    if [[ "$test" =~ ^("FL"|"NJ")T(7[0-8][7-9]|7[1-7][0-9]|78[1-7])$ ]]
    then
        y=1
    fi
done <$1
if (( y!=1))
then
    echo "no data"
    exit 3
fi

IFS=':,'
while read sensor value
do
    test=${sensor%%-*}
        if [[ "$test" =~ ^("FL"|"NJ")T(7[0-8][7-9]|7[1-7][0-9]|78[1-7])$ ]]
        then
            set $value

            for n in $value
            do
                sum=$(($sum + $n))
                c=$(($c+1))
                avg=$(($sum/$c))

                if (($n < min))
                then
                    min=$n
                elif (($n > max))
                then
                    max=$n
                fi
            done
        fi
done <$1

echo "min=$min, max=$max, sum=$sum, avg=$avg"
exit 0
