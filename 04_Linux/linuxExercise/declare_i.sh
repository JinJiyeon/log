#!/bin/sh

declare -i num

num=hello
echo num=hello: $num

num=10+20
echo num=10+20: $num

num="10 + 20"
echo num=\"10 + 20\": $num

num=10*20
echo num=10*20: $num

num=3.14
echo num=3.14: $num


