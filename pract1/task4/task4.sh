#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "Используйте: $0 имя_файла"
	exit 1
fi

file="$1"

grep -oE '\b[a-zA-Z_][a-zA-Z0-9_]*\b' "$file" | sort -u
