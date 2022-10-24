from operator import index
import random




class Hangman:

  def __init__(self, word_list,num_lives=5):
    self.num_lives = num_lives
    self.word_list= word_list
    self.word = random.choice(word_list)
    self.word_guessed  = []
    self.num_letters = len(self.word)
    self.list_letters = []
    output = '_ '
    i = 0
  
  
    print(f'The mystery word has {len(self.word)} characters' )
    print('_ ' * len(self.word))

  def check_letter(self,letter):
    
      if letter in self.word:
        for letter in self.word:
            print(letter)
          
            print(f'Good job {letter} is in the word'.format(letter))
      elif letter in self.word_guessed:
        print('You already tried this letter')

      else:
        
          print('Sorry {} is not in the word try again'.format(letter))
          print(self.list_letters.append , letter)

  def ask_letter(self):
    while True:
      letter = input ('Enter a letter: ')
      if len(letter) != 1 or not letter.isalpha():
        print('please, enter just one letter')
     
      else:
        print('good job you insert a valid caracther' )
        break
        
        
    

def play_game():
  word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon'] 
  game = Hangman(word_list)
  ''' while game.num_lives > 0:'''
 
  
  game.ask_letter()
  game.check_letter('')
      
  

if __name__ == '__main__':
  play_game()

