import random
import string

def generate_unique_email():
    name = "test_user"
    cohort = "1999"
    suffix = ''.join(random.choices(string.digits, k=3))
    domain = "yandex.ru"
    return f"{name}_{cohort}_{suffix}@{domain}"