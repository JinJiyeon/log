#!/bin/bash

cat /dev/null > /test/0601_setuid.log

for perm in $(find / -type f -perm -4000 -print)
do
  owner="$(ls -l $perm | awk '{print $3}')"

  # 소유자가 root(0) 라면
  if [ ! -z $owner ]
  then
    echo "setuid 권한을 포함하고 root 소유인 파일 : $perm"
    echo "setuid 권한을 포함하고 root 소유인 파일 : $perm" >> /test/0601_setuid.log
  fi
done
  exit