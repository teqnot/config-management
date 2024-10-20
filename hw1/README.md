## 1. Клонирование репозитория
Склонируйте репозиторий с исходным кодом:
```bash
git clone https://github.com/teqnot/config-management.git
```

Перейдите в директорию проекта:
```
cd config-management/hw1
```

## 2. Установка зависимостей и запуск
Создайте виртуальное окружение:
> Windows
```bash
python -m venv venv
venv\Scripts\Activate
```
> Linux
```bash
python -m venv venv
source venv/bin/activate
```

Запуск:
```bash
python main.py --username USERNAME --hostname HOSTNAME --zip_path ZIP_PATH --init_script INIT_SCRIPT
```
Default case:
```bash
python main.py --username USERNAME --hostname HOSTNAME --zip_path vfs.zip --init_script startup.bash
```

## 3. Структура проекта
Проект содержит следующие файлы:
```bash
commands.py     # Обработка текстового ввода команд
filesystem.py   # Реализация функций команд, файловой системы и записи логов
gui.py          # Реализация GUI
main.py         # Изначальный запуск и настройка эмулятора
shell.py        # Обработка работы команд
startup.bash    # Скрипт изначальной проверки команд
tests.py        # Реализация тестов команд
vfs.zip         # Default файловая система
```

## 4. Запуск тестов
```bash
python tests.py
```
