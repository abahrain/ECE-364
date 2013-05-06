#! /bin/bash

if (( $# != 1 ))
then
	exit 1
fi

if [[ ! $1 =~ ^[0-9]{1,3}$ ]]
then
	exit 2
fi

(( $1 >= 90 )) && echo "A"
(( $1 < 90 && $1 >= 80 )) && echo "B"
(( $1 < 80 && $1 >= 70 )) && echo "C"
(( $1 < 70 && $1 >= 60 )) && echo "D"
(( $1 < 60 )) && echo "F"


exit 0
