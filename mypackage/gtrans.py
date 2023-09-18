from module1 import TransLate, LangDetect, CodeLang, LanguageList

def main():
    text_to_translate = "Привіт"

    translated_text = TransLate(text_to_translate, src="uk", dest="en")
    print(f"Translated Text: {translated_text}")

    detected_language = LangDetect(text_to_translate, set="lang")
    print(f"Detected Language: {detected_language}")

    code = CodeLang("en")
    print(f"Language Code: {code}")

    result = LanguageList(out="screen", text="Привіт, мене звати Петухов Андрій")
    print(result)

if __name__ == "__main__":
    main()
