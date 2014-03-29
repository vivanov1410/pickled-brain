dictionary = {
  'merry': 'god',
  'christmas': 'jul',
  'and': 'och',
  'happy': 'gott',
  'new': 'nytt',
  'year': 'er'
}

def translate(words):
  translation = ''

  for word in words:
    translation += dictionary.get(word, word) + ' '

  return translation

print( translate(['merry', 'christmas', 'moya', 'happy', 'popa', 'Svetochka', ':)']) );