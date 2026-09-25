Лабораторная работа 1. Консольный набор утилит.
Python-пакет `toolkit` с CLI на Typer: калькулятор арифметических выражений и конвертер единиц измерения.

Требования:
 - Python 3.10 или выше
 - Terminal
   
Установка:

    cd lab_01
    python -m venv .venv
    
  Windows PowerShell:
  
    .venv\Scripts\Activate.ps1
    
  Linux/macOS:
  
    source .venv/bin/activate

    python -m pip install --upgrade pip
    python -m pip install -e .
    python -m pip install pytest ruff
   
Быстрый старт:

    python -m toolkit calc "2 + 2 * 2"
    python -m toolkit convert 1 --from m --to cm
    python -m toolkit --help

Калькулятор:

    python -m toolkit calc "EXPRESSION"

Конвертер:

    python -m toolkit convert VALUE --from UNIT --to UNIT

Структура проекта:

lab_01/
├── pyproject.toml
├── README.md
├── src/
│   └── toolkit/
│       ├── __init__.py
│       ├── __main__.py
│       ├── tokenization.py
│       ├── validation.py
│       ├── calculation.py
│       ├── converter.py
│       └── errors.py
└── tests/
    ├── test_calculator.py
    ├── test_converter.py
    └── test_cli.py

Тесты:

  python -m pytest
  
  python -m pytest tests/test_calculator.py
  
  python -m pytest tests/test_converter.py
  
  python -m pytest tests/test_cli.py
