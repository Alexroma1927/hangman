from operator import index
import random
import sys




class Hangman:

  def __init__(self, word_list,num_lives=5):
    self.num_lives = num_lives
    self.word_list= word_list
    self.word = random.choice(word_list)
    self.word_guessed  =['_ '] * len(self.word)
    self.num_letters = len(self.word)
    self.list_letters = []
    
    print('Start Game')

    print(f'The mystery word has {len(self.word)} characters' )

    print('_ ' * len(self.word))

  def check_guess(self,guess):
        
        if guess in self.word:              
            print(f'Good job {guess} is in the word')
            for adx in range(len(self.word)):
                if guess == (self.word[adx]):
                    self.word_guessed[adx] = guess
            self.num_letters -= 1
            print(self.word_guessed)                   
        elif guess in self.list_letters:
            print('You already tried this letter')
            self.list_letters.append(guess)
            print(self.list_letters)            
        else:
            print(f'Sorry {guess} is not in the word try again')
            self.list_letters.append(guess)
            self.num_lives = self.num_lives-1
            #while self.num_lives == 0:
            print(f'You have {self.num_lives} lives left')
            
          
  def ask_for_input(self):
    while True:
      guess = input('Enter a letter: ')
      if len(guess) != 1 or not guess.isalpha(): 
        print('please, enter just one letter')
      elif guess in self.list_letters:
        print('you already called that letter')
        print(self.list_letters)
        #self.ask_for_input()  
      else:
        print('good job you insert a valid character' )
        self.check_guess(guess)
        break
        
        
def play_game():
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon'] 
    game = Hangman(word_list)
    while True:
      if game.num_lives == 0:
        print(f'You have {game.num_lives} lives left GAME OVER','YOU LOST')
        break
      elif game.num_letters > 0:
        game.ask_for_input()
      else:
        print('Congratulation','YOU WIN!!')
        break
    sys.exit()
  
        
if __name__ == '__main__':
  play_game()