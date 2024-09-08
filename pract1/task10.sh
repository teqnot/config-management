#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "Использование: $0 /путь/к/каталогу."
	exit 1
fi

directory="$1"

if [ ! -d "$directory" ]; then
	echo: "Ошибка: указанный каталог '$directory' не существует."
	exit 1
fi

find "$directory" -type f -name "*.txt" -empty -exec basename {} \;
