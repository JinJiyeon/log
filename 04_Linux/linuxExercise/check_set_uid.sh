#!/bin/bash

file=~/test/set_uid.log
cat /dev/null > $file

for filename in $(sudo find / -type f -perm -4000 2> /dev/null)
do
	user="$(ls -l $filename | awk '{print $3'})"
	
	if [ -s $perm ]; then
		echo "$user의 SetUID 설정이 있는 파일: $filename" | tee -a $file
	fi
done
exit
