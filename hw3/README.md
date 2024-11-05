## 1. Клонирование репозитория
Склонируйте репозиторий с исходным кодом:
```bash
git clone https://github.com/teqnot/config-management.git
```

Перейдите в директорию проекта:
```bash
cd config-management/hw3
```

## 2. Установка зависимостей и запуск
Выполните:
```bash
go mod init <samplename>
```

Запуск:
```bash
go run ./main.go <input XML file> <output file>
```
Default case:
```bash
go run ./main.go example1.xml output.txt
```

## 3. Структура проекта
```bash
main.go     # Парсинг XML файла, создание файла на конфигурационном языке
```

## 4. Запуск тестов
```bash
go test
```