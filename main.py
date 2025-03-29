import os
import time

import redis


def get_redis_connection():
    host = os.getenv('REDIS_HOST', 'localhost')
    port = int(os.getenv('REDIS_PORT', 6379))
    db = int(os.getenv('REDIS_DB', 0))
    password = os.getenv('REDIS_PASSWORD')

    try:
        if password:
            r = redis.Redis(host=host, port=port, db=db, password=password)
        else:
            r = redis.Redis(host=host, port=port, db=db)
        r.ping()
        return r
    except redis.ConnectionError as e:
        print(f"Помилка підключення до Redis: {e}")
        return None


def save_timestamp_to_redis(r, key="dt"):
    current_time = time.time()
    r.set(key, current_time)
    return current_time


def get_timestamp_from_redis(r, key="dt"):
    current_time = r.get(key)
    if current_time:
        return float(current_time.decode("utf-8"))
    else:
        return None


if __name__ == '__main__':
    redis_connection = get_redis_connection()

    if redis_connection:
        save_time = save_timestamp_to_redis(redis_connection)
        print(f"Таймстемп {save_time} збережено в Redis.")

        read_time = get_timestamp_from_redis(redis_connection)
        print(f'Прочитано таймстемп: {read_time}')
    else:
        print("Не вдалося зберегти таймстемп в Redis.")
