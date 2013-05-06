#! /bin/bash
#
#$Author: ee364f04 $
#$Date: 2013-01-23 20:08:41 -0500 (Wed, 23 Jan 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab03/run.bash $
#$Revision: 48796 $

F=$@
size=(1 2 4 8 16 32)
width=(1 2 4 8 16)
output=$2

if (($# < 2))
then
    echo "usage: run.bash $File"
    exit 1
elif [[ -e $2 ]]
then
    echo "$2 already exists."
    echo -n "Would you like to delete it? "
    read answer


    if [[ $answer = "y" ]]
    then
        rm $2
    elif [[ $answer = "n" ]]
    then
        echo -n "Enter a new filename: "
        read f
        output=$f
    fi

fi

gcc $1 -o quick_sim
touch $2
set $size
set $width

for s in ${size[*]}
do
    for w in ${width[*]}
    do
        quick_sim $s $w a > $output
        quick_sim $s $w i > $output
    done
done

exit 0

