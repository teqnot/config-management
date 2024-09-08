#!/bin/bash

if [ "$#" -ne 2 ]; then
	echo "Использование: $0 /путь/к/каталогу <расширение>."
	exit 1
fi

directory="$1"
extension="$2"

if [ ! -d "$directory" ]; then
	echo "Ошибка: указанный каталог '$directory' не существует."
	exit 1
fi

shopt -s nullglob
files=("$directory"/*."$extension")

if [ ${#files[@]} -eq 0 ]; then
	echo "Ошибка: в указанном каталоге '$directory' нет файлов с расширением .'$extension'."
	exit 1
fi

archive_name="${directory%/}.tar"

tar -cvf "$archive_name" -C "$directory" ./*."$extension"

echo "Архив '$archive_name' успешно создан."
