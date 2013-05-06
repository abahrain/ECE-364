#! /bin/bash
#
#$Author: ee364f04 $
#$Date: 2013-01-17 00:03:16 -0500 (Thu, 17 Jan 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab02/check_file.bash $
#$Revision: 48316 $

FILENAME=$@

if [[ -e $FILENAME ]]
then
    echo "$FILENAME exists"
else
    echo "$FILENAME does not exist"
fi

if [[ -d $FILENAME ]]
then
    echo "$FILENAME is a directory"
else
    echo "$FILENAME is not a directory"
fi

if [[ -f $FILENAME ]]
then
    echo "$FILENAME is an ordinary file"
else
    echo "$FILENAME is not an ordinary file"
fi

if [[ -r $FILENAME ]]
then
    echo "$FILENAME is readable"
else
    echo "$FILENAME is not readable"
fi

if [[ -w $FILENAME ]]
then
    echo "$FILENAME is writable"
else
    echo "$FILENAME is not writable"
fi

if [[ -x $FILENAME ]]
then
    echo "$FILENAME is executable"
else
    echo "$FILENAME is not executable"
fi

exit 0
