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
            return "N/A"
        else:
            return f"Language: {detected_lang}"
    except Exception as e:
        return str(e)

def CodeLang(lang: str) -> str:
    lang_dict = {
        "English": "en",
        "Spanish": "es",
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
    pass


text_to_translate = "Привіт, мене звати Петухов Андрій"
translated_text = TransLate(text_to_translate, src="auto", dest="en")
print(f"Translated Text: {translated_text}")

detected_language = LangDetect(text_to_translate, set="lang")
print(f"Detected Language: {detected_language}")

code = CodeLang("English")
print(f"Language Code: {code}")
