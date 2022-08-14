#!/bin/sh

x=1
echo x=1: $x

let x=x+2
echo x=x+2: $x

let "x = x + 3"
echo \"x = x + 3\": $x

let x+=4
echo x+=4: $x

x=2
echo x=2: $x

((x+=2))
echo \(\(x+=2\)\): $x

