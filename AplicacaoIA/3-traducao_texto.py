from deep_translator import GoogleTranslator

# 1 - Idiomas Disponiveis
langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
#print(langs_dict)

# 2 - Tradução de Pt para En
text = 'Estaos estudando Processamento de Linguagem Natural'
translated = GoogleTranslator(
    source= 'pt',
    target= 'en'
).translate(text=text)
print(translated)

# 3 - Traução em itens de uma lista
texts = [
    "Estou aprendendo automação com python",
    "Estou gostando muito",
    "Quero aorender a desenvolver sistemas em python"
]
translated_itens = GoogleTranslator(
    source= 'pt',
    target= 'en'
).translate_batch(texts)
print(translated_itens)