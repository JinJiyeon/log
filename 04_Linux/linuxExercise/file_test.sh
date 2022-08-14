#!/bin/bash

if  [ -f ~/test/file ]; then
     if [ -s ~/test/file ]; then 
         echo " 파일이 0 보다 큽니다."
	 else 
		 echo " 파일이 0입니다."
     fi
fi
