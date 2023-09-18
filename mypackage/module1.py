from googletrans import Translator, LANGUAGES

def TransLate(text: str, src: str, dest: str) -> str:
    """
    Функція повертає текст перекладений на задану мову, або повідомлення про помилку.
    text – текст, який необхідно перекласти;
    src – назва або код мови заданого тексту, відповідно до стандарту ISO-639,
    або значення ‘auto’;
    dest – назва або код мови на яку необхідно перевести заданий текст,
    відповідно до стандарту ISO-639
    """
    translator = Translator()
    try:
        translated = translator.translate(text, src=src, dest=dest)
        return translated.text
    except Exception as e:
        return str(e)

def LangDetect(text: str, set: str = "all") -> str:
    """
    Функція визначає мову та коефіцієнт довіри для заданого тексту,
    або повертає повідомлення про помилку.
    text – текст для якого потрібно визначити мову та коефіцієнт довіри;
    set = “lang” – функція повертає тільки мову тексту
    set = “confidence” – функція повертає тільки коефіцієнт довіри
    set = “all” (по замовченню) – функція повертає мову і коефіцієнт довіри
    """
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
    """
    Функція повертає код мови (відповідно до таблиці), якщо в параметрі lang міститься назва
    мови, або повертає назву мови, якщо в параметрі lang міститься її код,
    або повідомлення про помилку
    lang – назва або код мови
    """
    lang = lang.lower()
    if lang in LANGUAGES:
        return LANGUAGES[lang]
    elif lang in LANGUAGES.values():
        return next(key for key, value in LANGUAGES.items() if value == lang)
    else:
        return "Language not found"

def LanguageList(out: str = "screen", text: str = None) -> str:
    """
    Виводить в файл або на екран таблицю всіх мов, що підтримуються, та їх кодів,
    а також текст, перекладений на цю мову. Повертає ‘Ok’, якщо всі операції виконані,
    або повідомлення про помилку.
    out = “screen” (по замовченню) – вивести таблицю на екран
    out = “file” – вивести таблицю в файл. (Тип файлу на розсуд студента)
    text – текст, який необхідно перекласти. Якщо параметр відсутній, то відповідна колонка
    в таблиці також повинна бути відсутня.
    """
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

# Приклад використання:
print(TransLate("Hello", "en", "fr"))
print(LangDetect("Мене звати Андрій"))
print(CodeLang("es"))
print(LanguageList("file", "Hello"))
