#!/bin/sh

name1=centos; name2=good

[ $name1 == [Cc]????? ]; echo $?

[[ $name1 == [Cc]????? ]]; echo $?

[[ $name1 == [Cc]????? && $name2 == g[o]{2}d ]]; echo $?

