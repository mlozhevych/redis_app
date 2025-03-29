# Redis Timestamp App

Цей проєкт зберігає поточний таймстемп у Redis, використовуючи Python.

## Вимоги

* Python 3.6+
* Redis (встановлений та запущений локально або віддалено)

## Встановлення

1.  Клонуйте репозиторій:

    ```bash
    git clone https://github.com/mlozhevych/redis_app.git
    cd redis_app
    ```
2.  Створіть віртуальне оточення (рекомендовано):

    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Linux/macOS
    venv\Scripts\activate  # Для Windows
    ```
3.  Встановіть необхідні пакети:

    ```bash
    pip install -r requirements.txt
    ```
4. Створіть або відредагуйте `.env` файл з параметрами з'єднання з Redis:

    ```
    REDIS_HOST=localhost
    REDIS_PORT=6379
    REDIS_DB=0
    ```
   Або встановлення через командний рядок (приклад для Linux/macOS):

    ```bash
    export REDIS_HOST=ваш_хост
    export REDIS_PORT=ваш_порт
    export REDIS_DB=ваш_db
    export REDIS_PASSWORD=ваш_пароль
    ```
   
## Запуск

```bash
python main.py
```

Скрипт:

- Зчитує конфігурацію з `.env`
- Підключається до Redis
- Зберігає поточний таймстемп під ключем `current_time`
- Виводить таймстемп у консоль