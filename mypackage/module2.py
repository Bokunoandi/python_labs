from deep_translator import GoogleTranslator
from langdetect import detect

def TransLate(text: str, src: str, dest: str) -> str:
    try:
        translated = GoogleTranslator(source=src, target=dest).translate(text)
        return translated
    except Exception as e:
        return str(e)

def LangDetect(text: str, set: str = "all") -> str:
    try:
        detected_lang = detect(text)
        if set == "lang":
            return detected_lang
        elif set == "confidence":
            # deep_translator не надає коефіцієнт довіри для визначення мови
            return "N/A"
        else:
            return f"Language: {detected_lang}"
    except Exception as e:
        return str(e)

def CodeLang(lang: str) -> str:
    # Ви можете створити власний словник кодів мов для deep_translator,
    # якщо такий словник не надається бібліотекою
    lang_dict = {
        "English": "en",
        "Spanish": "es",
        # Додайте інші мови тут
    }
    if lang in lang_dict:
        return lang_dict[lang]
    elif lang in lang_dict.values():
        for name, code in lang_dict.items():
            if code == lang:
                return name
    else:
        return "Language not found"

def LanguageList(out: str = "screen", text: str = None) -> str:
    # Реалізуйте цю функцію, використовуючи deep_translator,
    # для отримання списку підтримуваних мов і їх кодів.
    # Ви можете також використовувати langdetect для перекладу тексту,
    # як показано у попередньому прикладі.
    pass

# Приклад використання функцій
text_to_translate = "Добрий день"
translated_text = TransLate(text_to_translate, src="auto", dest="en")
print(f"Translated Text: {translated_text}")

detected_language = LangDetect(text_to_translate, set="lang")
print(f"Detected Language: {detected_language}")

code = CodeLang("English")
print(f"Language Code: {code}")
