#! /bin/bash
#
#$Author: ee364f04 $
#$Date: 2013-02-14 11:29:52 -0500 (Thu, 14 Feb 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Lab06/assign_undergrad_grades.bash $
#$Revision: 51929 $

f=$@
sum=0
t=$2
if (( $# != 2 ))
then
    echo "usage: assign_undergrad_grades.bash <grade file> <school>"
    exit 1
fi
if [[ ! -r $1 ]] && [[ ! -e $1 ]]
then
    echo "error: $1 is not a readable file"
    exit 2
fi
if [[ "$2" =~ ^[^a-z]+$ ]]
then
    echo "error: $2 is not a valid school abbreviation."
    exit 2
fi

IFS="/"
while read name data
do
    if [[ "$name" =~ ^[$t].*$ ]]
    then
        set $data

        for i in ${!data[*]}
        do
            sum=$(($sum + $i))
            c=$(($c + 1))
            avg=$(($sum/$c))
        done

        let=$(get_letter_grade.bash $avg)

        echo "$name $avg $let" >>sutdents.db.$t
    fi
done <$1

exit 0
