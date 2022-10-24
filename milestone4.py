from operator import index
import random








class Hangman:

  def __init__(self, word_list,num_lives=5):
    self.num_lives = num_lives
    self.word_list= word_list
    self.word = random.choice(word_list)
    self.word_guessed  =['_ '] * len(self.word)
    self.num_letters = len(self.word)
    self.list_letters = []
    
  
    print(f'The mystery word has {len(self.word)} characters' )
    print('_ ' * len(self.word))

  def check_guess(self,guess):
        
        if guess in self.word:              
            print(f'Good job {guess} is in the word'.format(guess))
            for adx in range(len(self.word)):
                if guess == (self.word[adx]):
                    self.word_guessed[adx] = guess
            print(self.word_guessed)                   
        elif guess in self.word_guessed or self.list_letters:
            print('You already tried this letter')
            self.list_letters.append(guess)
            print(self.word_guessed)            
        else:
            print('Sorry {} is not in the word try again'.format(guess))
            self.list_letters.append(guess)
            self.num_lives = self.num_lives-1
            print('You have {} lives left'.format(self.num_lives))

  def ask_for_input(self):
    while True:
      guess = input ('Enter a letter: ')
      if len(guess) != 1 or not guess.isalpha(): 
        print('please, enter just one letter')
      elif guess in self.list_letters:
        print('you already called that letter')
        print(self.list_letters)
        self.ask_for_input()  
      else:
        print('good job you insert a valid character' )
        self.check_guess(guess)
        
        
def play_game():
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon'] 
    
    game = Hangman(word_list)
    
    while game.num_lives >= 0:
        game.ask_for_input()
    print('Sorry you lost')
    
    
    
        
    
        


        
 
 
  


  
      
  

if __name__ == '__main__':
  play_game()