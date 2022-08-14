#!/bin/sh

ami=`whoami`

if [ "$ami" != "root" ];
then
  echo "이 스크립트는 관리자만 실행할 수 있습니다"
  exit
fi

echo "인수로 받은 name : $1 인 계정을 일시정지합니다"
echo ""

killall -s HUP -u $1
sleep 1
killall -s KILL -u $1

chmod 000 /home/$1
echo "$1을 일시정지 했습니다"
exit

