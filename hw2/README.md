## 1. Клонирование репозитория
Склонируйте репозиторий с исходным кодом:
```bash
git clone https://github.com/teqnot/config-management.git
```

Перейдите в директорию проекта:
```bash
cd config-management/hw2
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

Установите graphviz для визуализациия зависимостей:
> Windows
- [graphviz-12.1.2 (.EXE)](https://gitlab.com/api/v4/projects/4207231/packages/generic/graphviz-releases/12.1.2/windows_10_cmake_Release_graphviz-install-12.1.2-win64.exe) 

> Linux
```bash
# Debian, Ubuntu
sudo apt install graphviz

# Fedora Project, Rocky Linux, Redhat Enterprise Linux, or CentOS
sudo dnf install graphviz 
```

Запуск:
```bash
python main.py --graphviz-path GRAPHVIZ_PATH --package-name PACKAGE_NAME --output-file OUTPUT_FILE [--max-depth MAX_DEPTH]
```
Default case:
```bash
python main.py --graphviz-path GRAPHVIZ_PATH --package-name azure-core --output-file out.dot
```

Создание визуальной схемы зависимостей:
```bash
dot -Tpng out.dot -o samplename.png
```

## 3. Структура проекта
```bash
main.py     # Парсинг зависимостей, создание .dot файла
```

## 4. Запуск тестов
```bash
python tests.py
```