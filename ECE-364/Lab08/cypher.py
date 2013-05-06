#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-02-28 11:10:21 -0500 (Thu, 28 Feb 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Lab08/cypher.py $
#$Revision: 53683 $

import sys
d="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 "
A={}
C={}
c=0
for i in d:
    B={c:i}
    D={i:c}
    A.update(B)
    C.update(D)
    c+=1

def strip_invalid_characters(s):
    out=[]
    outst=""
    for i in s:
        if i.isspace() or i.isupper() or i.islower() or i.isdigit():
            out.append(i)
    for i in out:
        outst+=i

    return outst

def is_valid_password(s):
    for i in s:
        if not i.isspace() or i.isupper() or i.islower() or i.isdigit():
            return False

def vign_encrypt(message, password):
    out=""
    if is_valid_password(password):
        raise ValueError()

    p=len(password)

    for i in range(len(message)):
        e=C[message[i]]+C[password[i%p]]
        e=e%63
        out+=A[e]

    return out



def vign_decrypt(message, password):
    out=""
    if is_valid_password(password):
        raise ValueError()
    
    p=len(password)
    
    for i in range(len(message)):
        e=C[message[i]]-C[password[i%p]]
        e=e%63
        out+=A[e]
    
    return out

