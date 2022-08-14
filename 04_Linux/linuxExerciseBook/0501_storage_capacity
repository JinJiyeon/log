#!/bin/sh

SETSIZW=10

EXMB=`expr $SETSIZE * 1024 * 1024`

for name in $(cut -d: -f1,3 /etc/passwd | awk -F: '$2 > 2499 {print $1}')
do
  echo "사용자 : $name 의 $SETSIZE를 초과한 파일과 용량"
  find /usr/tmp/home  -user $name  -type f  -ls | awk "\$7 > $EXMB" | awk '{print $11, $7}'
  echo ""
done
exit