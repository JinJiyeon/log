#!/bin/sh

echo \$_: $_
echo \$*: $*
echo \$@: $@
echo \$#: $#
echo \$\$: $$
echo \$0: $0
echo "\$1: $1, \$2: $2, \$3: $3"
echo \$_: $_

set $(date) 

echo \$_: $_
echo \$*: $*
echo \$@: $@
echo \$#: $#
echo \$\$: $$
echo \$0: $0
echo \$1: $1, \$2: $2, \$3: $3
echo \$_: $_

