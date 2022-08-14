#!/bin/bash

# longest-word: find longest string in a file

while [[ -n "$1" ]]; do 		# size가 0보다 크다
	if [[ -r "$1" ]]; then		# 읽기가 가능하다
		max_word=
		max_len=0
		set -x
		for i in $(strings "$1"); do
			len="$(echo -n "$i" | wc -c)" # wc : word count
			if (( len > max_len )); then
				max_len="$len"
				max_word="$i"
			fi
		done
		set +x
		echo "$1: '$max_word' ($max_len characters)"
	fi
	shift
done
