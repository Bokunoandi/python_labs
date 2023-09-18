from googletrans import Translator, LANGUAGES

def TransLate(text: str, src: str, dest: str) -> str:
    translator = Translator()
    try:
        translated = translator.translate(text, src=src, dest=dest)
        return translated.text
    except Exception as e:
        return str(e)

def LangDetect(text: str, set: str = "all") -> str:
    translator = Translator()
    try:
        detected = translator.detect(text)
        if set == "lang":
            return detected.lang
        elif set == "confidence":
            return str(detected.confidence)
        else:
            return f"Language: {detected.lang}, Confidence: {detected.confidence}"
    except Exception as e:
        return str(e)

def CodeLang(lang: str) -> str:
    lang = lang.lower()
    if lang in LANGUAGES:
        return LANGUAGES[lang]
    elif lang in LANGUAGES.values():
        return next(key for key, value in LANGUAGES.items() if value == lang)
    else:
        return "Language not found"

def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        if out == "file":
            with open("language_list.txt", "w", encoding="utf-8") as file:
                for code, language in LANGUAGES.items():
                    translation = TransLate(text, 'auto', code) if text else ''
                    file.write(f"Code: {code}, Language: {language}, Translation: {translation}\n")
        else:
            for code, language in LANGUAGES.items():
                translation = TransLate(text, 'auto', code) if text else ''
                print(f"Code: {code}, Language: {language}, Translation: {translation}")
        return "Ok"
    except Exception as e:
        return str(e)


print(TransLate("Hello", "en", "fr"))
print(LangDetect("Мене звати Андрій"))
print(CodeLang("es"))
print(LanguageList("file", "Hello"))
