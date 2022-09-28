while True:
  letter = input ('Enter a letter: ')
  if len(letter) != 1 :
    print('please, enter just one letter')
  elif len(letter) == 1 and not letter.isdecimal():
    print('good')
    break

  else:
            print('please , enter a character')
