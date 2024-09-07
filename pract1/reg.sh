#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "Используйте: $0 имя команды."
	exit 1
fi

command_name="$1"
command_path="./$command_name"

if [ ! -f "$command_path" ]; then
	echo "Ошибка: файл '$command_path' не найден."
	exit 1
fi

sudo chmod +x "$command_name"
sudo cp "$command_path" /usr/local/bin/

if [ $? -ne 0 ]; then
	echo "Ошибка: не удалось скопировать файл."
	exit 1
fi

sudo chmod 775 /usr/local/bin/"$command_name"

if [ $? -ne 0 ]; then
	echo "Ошибка: не удалось установить права для '$command_name'."
	exit 1
fi

echo "Команда '$command_name' успешно зарегестрирована."
