#!/bin/sh

rollbackToDir="/tmp/sample/"
ami=`whoami`

if ["$ami" != "root"];
then
  echo "이 스크립트는 관리자만 실행할 수 있습니다"
  exit
fi

for name in $(cat /etc/passwd | awk -F: `/^user/{print $1}`)
do
  cd /home/$name
  rm -r *
  cp -rp /$rollbackToDir /home/$name
  echo "$name의 홈디렉토리를 초기화했습니다"
  echo ""
done
  exit