#!/bin/sh

name=centos

test $name == centos; echo $?

test $name = centos; echo $?

test $name != centos; echo $?

[ $name == centos ]; echo $?

[ $name = centos ]; echo $?

[ $name != centos ]; echo $?

[ $name ]; echo $?

[ -z $name ]; echo $?

[ -n $name ]; echo $?

