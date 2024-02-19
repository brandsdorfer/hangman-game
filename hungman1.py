from os import path

def Hangman_pattern_1():
    '''
    return the The opening screen
    rtype: str
    '''
    HANGMAN_ASCII_ART = str("""welcome to the "hangman" game!
        
    _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                        |___/ \n""")
    return HANGMAN_ASCII_ART

def hangman_pattern(index):
    '''
    Display the hanging step by number by a dict
    :parma index: number of level
    :type index: int
    :return: the hanging step by number
    :rtype: str
    '''
    HANGMAN_PHOTOS = {
    1:"""
        x-------x""",

    2:"""
        x-------x
        |
        |
        |
        |
        |""",

    3:"""
        x-------x
        |       |
        |       0
        |
        |
        |""",

    4:"""
        x-------x
        |       |
        |       0
        |       |
        |
        |""",

    5:"""
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |""",

    6:"""
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |""",

    7:"""
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |"""
    }

    print(HANGMAN_PHOTOS[index])
 
def is_valid_input(letter_guessed):
    """Checks if the input is an alphabetic letter and that it is not greater than 1.
    :param letter_guessed: input from user
    :type letter_guessed: int or str
    :return: The result of the check
    :rtype: bool
    """
    return letter_guessed.isalpha() and len(letter_guessed) == 1

def check_valid_input(letter_guessed, old_letters_guessed):
    """Checks if the input is valid and didn't guess him before.
    :param letter_guessed: input from user
    :type letter_guessed: int or str
    :parma old_letters_guessed: list of guessed letters
    :type old_letters_guessed: list
    :return: The result of the check
    :rtype: bool
    """
    return is_valid_input(letter_guessed) and letter_guessed not in old_letters_guessed
    
def try_update_letter_guessed(letter_guessed,  old_letters_guessed):
    """The function will update the list if the input is correct,
    if the input is not correct the function will return a sorted list of the guessed letters.
    :param letter_guessed: input from user
    :type letter_guessed: int or str
    :parma old_letters_guessed: list of guessed letters
    :type old_letters_guessed: list
    :return: The result of the check and list
    :rtype: bool, list.
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())

    else:
        the_list1 = sorted(old_letters_guessed)
        the_list1 = " -> ".join(the_list1)
        print("X", '\n', the_list1)
        return False
    
def show_hidden_word(secret_word, old_letters_guessed):
    """Returns the word dashed so that only the guessed letters are visible.
    :param secret_word:The word the user has to guess 
    :type secret_word: str
    :parma old_letters_guessed: list of guessed letters
    :type old_letters_guessed: list
    :return: word dashed
    :rtype:str
    """
    output_hidden_word = str()
    for i in secret_word:
        if i.lower() in old_letters_guessed:
           output_hidden_word += i

        else:
            output_hidden_word += "_"
    return output_hidden_word.replace("", " ")

def check_win(secret_word, old_letters_guessed):
    """The function checks if the user has guessed all the letters that make up the word.
    :param secret_word:The word the user has to guess 
    :type secret_word: str
    :parma old_letters_guessed: list of guessed letters
    :type old_letters_guessed: list
    :return: if the letters are in the list of guessed letters
    :rtype:bool
    """
    word = show_hidden_word(secret_word, old_letters_guessed).replace(" ", "")
    return word == secret_word

def choose_word(file_path, index):
    """The function choose a word acording to index in the file.
    :param file_path: The path to the file from which the word is selected
    :type secret_word: str
    :parma index: The location in file from which the word will be selected
    :type index: int
    :return: word acording to index in the file
    :rtype: str
    """
    words = open(file_path, 'r').read().split()
    index = (int(index) % len(words)) - 1

    return(words[index])

def get_correct_path_and_index():
    """
    : get the path and index from the player
    : var path_of_file: get the path of the file
    : type path_of_file: link
    : var index_for_file: get the location in the file where the word will be defined
    : type index_for_file: int
    : return: the path of the file and index
    : rtype: link and int
    """
    path_of_file = input("Please enter the path of the word file: ")
    
   # Check if file path is correct
    while path.isfile(path_of_file) == False:
        print("I did not find the file at "+str(path_of_file)+'. Please check the directory path, spelling, and try again.: ')
        # update the path
        path_of_file = input("Please enter the path of the word file: ")
    
    index_for_file = input("Please enter the index of the file: ")

    # Check if file index is correct
    while index_for_file.isdigit() == False:
            print("'"+index_for_file+"' is not a nomber.")
            # update var index_for_file
            index_for_file = input("Please enter the index of the file: ")
    
    return (path_of_file, index_for_file)

def defines_word_by_file():
    """
    : The function will define the word according to the correct link received in the function
    : var path_of_file: the path of the file
    : type path_of_file: link
    : var index_for_file: get the location in the file where the word will be defined
    : type index_for_file: int
    : var word: word selected according to the received file
    : type word: str
    : return: the secret word
    : rtype: str
    """
    result = get_correct_path_and_index()
    path_of_file = result[0]
    index_for_file = result[1]

    # choose word from this file having get at "path_of_file"
    word = choose_word(path_of_file, index_for_file)
        
    while word.isalpha() == False:
        print("The word that is in this index in file "+path_of_file+" is invalid")
        # update the variabls
        result = get_correct_path_and_index()
        path_of_file = result[0]
        index_for_file = result[1]
        word = choose_word(path_of_file, index_for_file)

    return word


def main():
    # variables
    MAX_TRIES = 6 
    old_letters_guessed = []
    nom_of_treis = 0

    # LEVEL 1: opening the game
    print(Hangman_pattern_1(), MAX_TRIES)
    
    # LEVEL 2: Defines the word by taking a link to the user's file and its index
    secret_word = defines_word_by_file()
    
    # Shows the opening state
    hangman_pattern(1)
    
    # the game is starting!
    while True:
        print(show_hidden_word(secret_word, old_letters_guessed))
        
        # get the letter guessed by user
        letter = input("guese a letter of the secret word :")
            
        if try_update_letter_guessed(letter, old_letters_guessed) is False:
            pass
        
        else:
            if letter.lower() not in list(secret_word.lower()):
                        nom_of_treis += 1
                        print("):")
                        hangman_pattern(nom_of_treis + 1)

            # When the player has successfully guessed the entire word    
            if check_win(secret_word, old_letters_guessed):
                    print("WIN")
                    break

            # When there was no success in guessing after 6 attempts   
            if nom_of_treis == 6:
                    print("LOSE")

                    # Gives the player the option to continue or to start over after the loss
                    the_choose = int(input("""Unfortunately you could not guess the word.
                                                If you want to try again, enter the number 1,
                                                If you want to change the secret word enter the number 2.\n :"""))
                    # gives more chances
                    if the_choose == 1:
                        nom_of_treis = 0

                    # start over
                    elif the_choose == 2:
                        nom_of_treis == 0
                        old_letters_guessed = []
                        secret_word = defines_word_by_file()

                    else:
                        break

if __name__ == "__main__":
    main()