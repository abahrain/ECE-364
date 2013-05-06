#!/bin/bash -x

gcc -ansi -Wall -pedantic -c -o tiff.o tiff.c
gcc -ansi -Wall -pedantic -c -o allocate.o allocate.c
gcc -ansi -Wall -pedantic -c -o randlib.o randlib.c
gcc -ansi -Wall -pedantic -c -o new_file.o new_file.c;
gcc -ansi -Wall -pedantic -o new_file new_file.o tiff.o allocate.o randlib.o -lm;
exit 0 
