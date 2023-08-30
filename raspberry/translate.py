from googletrans import Translator

def trans(word : str):
    translator = Translator()
    return translator.translate(word).text

def trans_en(word : str):
    translator = Translator()
    result = translator.translate(word, dest="ko")
    return result.text