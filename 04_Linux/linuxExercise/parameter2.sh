#!/bin/sh

set "홍 길동" 이순신 강감찬

echo \$*
for i in $*
do
  echo $i
done

echo \"\$*\"
for i in "$*"
do
  echo $i
done

echo \$@
for i in $@
do
  echo $i
done

echo \"\$@\"
for i in "$@"
do
  echo $i
done


