possibility = 0
initial = ''
monkey = [
  'hello',
  'test',
  'testo'
]
def request(text):
  for monkeyA in monkey:
    if monkeyA in text:
      print('monkey: ' + initial + monkeyA)
      max_possibility =+ 1
      if max_possibility == possibility:
        pass
      else:
        break
