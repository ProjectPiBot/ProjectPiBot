from googletrans import Translator

def trans(word : str):
    translator = Translator()
    #print(translator.translate(word).text)
    return translator.translate(word, src='ko', dest='en').text

def trans_en(word : str):
    translator = Translator()
    result = translator.translate(word, dest="ko")
    return result.text