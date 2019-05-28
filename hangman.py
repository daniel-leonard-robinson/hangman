import random

hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

secretword = words[random.randint(0, len(words) - 1)]
print(hangmanpics[0])
guess = '_' * len(secretword)
print(guess)
index = 1
guestlist = [] # guessed list lol

while True:
    char = input('Guess your next letter?\n')
    success = False

    for i in range(len(secretword)):
        if char == secretword[i]:
            guess = guess[:i] + char + guess[i+1:]
            success = True
    if char in guestlist:
        print("You've already guessed", char, 'in', guestlist)
        success = True
    if not success:
        guestlist.append(char)
        print(hangmanpics[index])
        index += 1
    if index >= len(hangmanpics):
        print('Game over')
        print('The word is', secretword)
        break
    if guess == secretword:
        print(guess)
        print("Well done :')")
        break
        
    print(guess)