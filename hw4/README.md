## 1. Клонирование репозитория
Склонируйте репозиторий с исходным кодом:
```bash
git clone https://github.com/teqnot/config-management.git
```

Перейдите в директорию проекта:
```bash
cd config-management/hw4
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
1. Запуск ассемблера
```bash
python assembler.py <input_file> <output_bin_file> <output_log_file>
```

Default case:
```bash
python assembler.py sample.txt output.bin log.yaml
```

2. Запуск интерпретатора
```bash
python interpreter.py <binary_file> <result_file>
```

Default case:
```bash
python interpreter.py output.bin result.yaml
```

## 3. Структура проекта
```bash
assembler.py    # Сборка бинарного файла и логов по исходному коду
interpreter.py  # Интерпретация бинарного файла в контексте памяти и регистров
```