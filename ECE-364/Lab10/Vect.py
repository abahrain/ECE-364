#! /usr/bin/env python

import sys
import os
import math
import Vectors

Vec_a=[1,2,3]
Vec_b=[4,5,6]
Vec_c=[7,8,9,10]
Vec_d=[11,12,13,14]

V_a=Vectors.Vector3D(Vec_a)
V_b=Vectors.Vector3D(Vec_b)
V_c=Vectors.Vector(Vec_c)
V_d=Vectors.Vector(Vec_d)


V_e=V_c.add(V_d)
V_f=V_c.sub(V_d)
V_g=V_c.dot(V_d)
V_h=V_c.scale(7)
V_i=V_c.extend(V_d)
V_j=V_c.distance(V_d)

print V_e
print V_f
print V_g
print V_h
print V_i
print V_j

V_z=V_a.add(V_b)

print V_z
