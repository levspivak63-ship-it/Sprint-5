import random

def generate_email():
    """Генерирует email в формате test123@ya.ru"""
    return f"test{random.randint(100, 999)}@ya.ru"