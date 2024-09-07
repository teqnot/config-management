#!/bin/bash

check_comment() {
	local file=$1
	local ext=${file##*.}

	echo "Проверка: $file с расширением: .$ext"
	
	case $ext in
		c)
			if head -n 1 "$file" | grep -q '^\s*//' || head -n 1 "$file" | grep -q '^\s*/\*'; then
				echo "$file: Есть комментарий."
			else
				echo "$file: Нет комментария."
			fi
			;;
		js)
			if head -n 1 "$file" | grep -q '^\s*//'; then
				echo "$file: Есть комментарий."
			else
				echo "$file: Нет комментария."
			fi
			;;
		py)
			if head -n 1 "$file" | grep -q '^\s*#'; then
				echo "$file: Есть комментарий."
			else
				echo "$file: Нет комментария."
			fi
			;;
		*)
			echo "$file: Неподдерживаемый формат."
			;;
	esac
}


if [[ $# -ne 1 ]]; then
	echo "Использование: $0 <имя_файла>."
	exit 1
fi

if [[ -f $1 ]]; then
	check_comment "$1"
else
	echo "Файл $file не найден."
	exit 1
fi
