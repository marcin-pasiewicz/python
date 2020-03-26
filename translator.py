from translate import Translator

translator = Translator(to_lang="ja")

try:
    with open('./test.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('./test=py.txt', mode="w") as my_file_ja:
            my_file_ja.write(translation)
except FileNotFoundError as err:
    print(f'file not found: {err}')
