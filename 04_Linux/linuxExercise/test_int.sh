#!/bin/sh

x=10; y=20

test $x -eq $y; echo $?

test $x -ne $y; echo $?

[ $x -eq $y ]; echo $?

[ $x -ne $y ]; echo $?

[ $x -gt $y ]; echo $?

[ $x -lt $y ]; echo $?

[ $x -ge $y ]; echo $?

[ $x -le $y ]; echo $?

