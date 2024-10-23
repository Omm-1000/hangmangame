import random

def display(lives):
    stages = [
        '''
            +---+
            |   |
            0   |
           /|\\  |
           / \\  |
                |
          =========
        ''', '''
            +---+
            |   |
            0   |
           /|\\  |
           /    |
                |
          ''', '''     
            +---+
            |   |
            0   |
           /|\\  |
                |
                |
          ''', '''
            +---+
            |   |
            0   |
           /|   |
                |
                |
          ''', '''     
            +---+
            |   |
            0   |
           /    |
                |
                |
          ''', '''     
            +---+
            |   |
            0   |
                |
                |
                |
          ''', '''      
            +---+
            |   |
                |
                |
                |
                |
                ''']
    
    return stages[lives]

word_list = ["apple", "beautiful", "potato","omm"]
chosen_word = random.choice(word_list)
#print(chosen_word)
lives = 6
display_list = ['_'] * len(chosen_word)
print(display_list)
game_over = False

while not game_over:
    gussed_letter = input("Guess a letter: ").lower()
    
    if gussed_letter in display_list:  
        print("You've already guessed that letter.")
        continue
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == gussed_letter:
            display_list[position] = gussed_letter
    
    print(display_list)
    
    if gussed_letter not in chosen_word:
        lives -= 1
        print(display(lives))
        if lives == 0:
            game_over = True
            print("You lose!! The word was:", chosen_word)
    
    if '_' not in display_list:
        game_over = True
        print("You win!! The word was:", chosen_word)


    
         
