from googletrans import Translator
translator = Translator()

x = translator.translate('good', dest='hi')
print(x.text)
