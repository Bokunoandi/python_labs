# deeptr.py

from deep_translator import GoogleTranslator
from langdetect import detect

def main():
    text_to_translate = "Добрий вечір"

    # Використовуємо deep_translator для перекладу тексту
    translated_text = GoogleTranslator(source="auto", target="en").translate(text_to_translate)
    print(f"Translated Text: {translated_text}")

    # Використовуємо langdetect для визначення мови тексту
    detected_language = detect(text_to_translate)
    print(f"Detected Language: {detected_language}")

if __name__ == "__main__":
    main()