import json
from deep_translator import GoogleTranslator

def read_config(config_file):
    with open(config_file, "r") as file:
        config = json.load(file)
    return config

def translate_file(input_file, output_file, config_file):
    config = read_config(config_file)

    with open(input_file, "r", encoding="utf-8") as infile, \
         open(output_file, "w", encoding="utf-8") as outfile:

        for line in infile:
            translated_line = GoogleTranslator(source="auto", target=config['target_language']).translate(line.strip())
            outfile.write(translated_line + "\n")

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    config_file = "config.json"

    translate_file(input_file, output_file, config_file)
