#! /bin/bash
#
#$Author: ee364f04 $
#$Date: 2013-01-17 11:25:32 -0500 (Thu, 17 Jan 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Lab02/summarize_expr.bash $
#$Revision: 48413 $

Files=$@

if (($# < 2))
then
    echo "usage: summarize_expr.bash $File"
    exit 1
fi

collect_expr.bash $Files

cut -d' ' -f1,7,8 $1

exit 0
