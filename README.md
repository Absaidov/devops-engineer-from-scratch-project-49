# Проект Игры разума

### Hexlet tests and linter status:
[![Actions Status](https://github.com/Absaidov/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Absaidov/devops-engineer-from-scratch-project-49/actions)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Absaidov_devops-engineer-from-scratch-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Absaidov_devops-engineer-from-scratch-project-49)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Absaidov_devops-engineer-from-scratch-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Absaidov_devops-engineer-from-scratch-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Absaidov_devops-engineer-from-scratch-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=Absaidov_devops-engineer-from-scratch-project-49)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=Absaidov_devops-engineer-from-scratch-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=Absaidov_devops-engineer-from-scratch-project-49)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Absaidov_devops-engineer-from-scratch-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=Absaidov_devops-engineer-from-scratch-project-49)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Absaidov_devops-engineer-from-scratch-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=Absaidov_devops-engineer-from-scratch-project-49)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Absaidov_devops-engineer-from-scratch-project-49&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=Absaidov_devops-engineer-from-scratch-project-49)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=Absaidov_devops-engineer-from-scratch-project-49&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=Absaidov_devops-engineer-from-scratch-project-49)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Absaidov_devops-engineer-from-scratch-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Absaidov_devops-engineer-from-scratch-project-49)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Absaidov_devops-engineer-from-scratch-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=Absaidov_devops-engineer-from-scratch-project-49)

## Использованные библиотеки
- prompt (предоставляет функции, которые запрашивают ввод строки string() , числа integer() , пароли secret() , электронную почту email())
- random (используется для генерации псевдослучайных чисел и выполнения операций со случайностью, таких как выбор случайного элемента из последовательности, перемешивание списков и генерация случайных чисел в заданном диапазоне)


## 📂 Структура репозитория:
    ── brain_games
    │   ├── __init__.py 
    │   ├── brain_games.py
    │   ├── games
    │   │   ├── __init__.py
    │   │   ├── brain_calc.py
    │   │   ├── brain_even.py
    │   │   ├── brain_gcd.py
    │   │   ├── brain_prime.py
    │   │   └── brain_progression.py
    │   ├── scripts
    │   │   ├── __init__.py
    │   │   ├── brain-calc.py
    │   │   ├── brain_even.py
    │   │   ├── brain_gcd.py
    │   │   ├── brain_prime.py
    │   │   ├── brain_progression.py
    │   │   ├── cli.py
    │   │   └── start_engine.py
    │   └── utils.py
    ├── pyproject.toml
    ├── ruff.toml
    └── uv.lock

## Установка Python

Перед тем как начать, убедитесь, что:

- Вы используете операционную систему, удобную для разработки (например Ubuntu,
  MacOS). Владельцам Windows рекомендую настроить Windows Subsystem for
  Linux (WSL). О том, как это сделать написано тут
  [гайд](https://ru.hexlet.io/blog/posts/ubuntu-linux-in-windows/).

## Установлен ли у Вас Python. Проверить это можно, выполнив команду:
```bash
python3 -V
```

## Если не установлен можно установить используя менеджер пакетов

### MacOS (если установлен Homebrew)

```bash
brew install python3
```

### Ubuntu Linux

```bash
sudo apt install python3
```
## Теперь когда Python установлен устанавливаем утилиту uv
## MacOS и Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Клонируем репозиторий локально
```bash
git clone git@github.com:Absaidov/devops-engineer-from-scratch-project-49.git
```

## Переходим в директорию
```bash
cd devops-engineer-from-scratch-project-49
```

## Собираем наш билд
```bash
make build
```

## Игра: «Проверка на чётность»
```sh
brain-even
```
## Игра: «Калькулятор»
```bash
brain-calc
```
## Игра «НОД»
```bash
brain-gcd
```
## Игра «Арифметическая прогрессия»
```bash
brain-progression
```
## Игра «Простое ли число?»
```bash
brain-prime
```

# Смотрим asciinema моего проекта

[![asciicast](https://asciinema.org/a/Gx1mBZmtlUTljlI1YvZLvlrCa.svg)](https://asciinema.org/a/Gx1mBZmtlUTljlI1YvZLvlrCa)