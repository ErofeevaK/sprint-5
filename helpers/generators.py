import random
import string
import time

def generate_unique_email():
    timestamp = int(time.time() * 1000)
    random_num = random.randint(100000, 999999)
    return f"test_user_{timestamp}_{random_num}@yandex.ru"
