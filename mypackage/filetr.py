# filetr.py

import json
from deep_translator import GoogleTranslator

def read_config(config_file):
    # Функція для читання конфігураційного файлу у форматі JSON
    with open(config_file, "r") as file:
        config = json.load(file)
    return config

def translate_file(input_file, output_file, config_file):
    # Читаємо конфігураційний файл
    config = read_config(config_file)

    # Відкриваємо вхідний і вихідний файли
    with open(input_file, "r", encoding="utf-8") as infile, \
         open(output_file, "w", encoding="utf-8") as outfile:

        # Читаємо текст з вхідного файлу по рядках
        for line in infile:
            # Використовуємо deep_translator для перекладу рядка тексту
            translated_line = GoogleTranslator(source="auto", target=config['target_language']).translate(line.strip())
            # Записуємо переклад у вихідний файл
            outfile.write(translated_line + "\n")

if __name__ == "__main__":
    input_file = "input.txt"  # Ім'я вхідного файлу з текстом
    output_file = "output.txt"  # Ім'я вихідного файлу для зберігання перекладу
    config_file = "config.json"  # Конфігураційний файл з налаштуваннями

    translate_file(input_file, output_file, config_file)
