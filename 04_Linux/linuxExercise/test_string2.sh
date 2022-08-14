#!/bin/sh

x=10; y=20

[ x == y ]; echo $?

[ x = y ]; echo $?

[ x != y ]; echo $?

