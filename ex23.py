# Strings, Bytes and character encodings

# download a text file called languages.txt(https://
#learnpythonthehardway.org/python3/languages.txt) 
# to run:
# python utf-8 languages.txt

import sys
#sys.stdout.write("utf-8")
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<======>", cooked_string)

languages = open("languages.txt", encoding="utf=8")

main(languages, encoding, error)