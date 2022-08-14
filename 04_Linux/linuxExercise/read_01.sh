#!/bin/bash

# evaluate the value of an integer.

echo -n "Please enter an integer -> "
read INT

if [[ "$INT" =~ ^-?[0-9]+$ ]]; then
	if [ "$INT" -eq 0 ]; then
		echo "INT is zero."
	else
		if [ "$INT" -lt 0 ]; then
			echo "INT is negative."
		else
			echo "INT is positive."
		fi

		if [ $((INT % 2)) -eq 0 ]; then
			echo "INT is even."
		else
			echo "INT is odd."
		fi 
	fi
else
	echo "INT is not an integer." >&2
	exit 1
fi
