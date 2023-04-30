from googletrans import Translator

def trans(word : str):
    translator = Translator()
    print(translator.translate(word).text)
    return translator.translate(word).text