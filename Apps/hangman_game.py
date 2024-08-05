      import random

      import hangman_art
      from hangman_words import wordList

      print(f"WELCOME TO . . . \n{hangman_art.title}")
      begin = input("Are you ready to play? (Press Enter to play)\n"
                    "Type 'exit' at anytime to quit.\n")
      if begin == "":
        cont = 1
      else:
        cont = 0
        print("Maybe Next Time! :)")
        quit()

      ### Setup ###
      while cont == 1:
        wordSelect = random.choice(wordList)
        wordLength = len(wordSelect)
        playerGuess = ""
        wordDisplay = []
        guesses = []
        art = [hangman_art.zero,hangman_art.one,hangman_art.two
           ,hangman_art.three,hangman_art.four,hangman_art.five
           ,hangman_art.six]
        lives = len(art)
        loopNbr = 0
        artNum = 0
        guessNum = lives
        for s in range(len(wordSelect)):
          wordDisplay.append("_")

        ### Game ###
        while guessNum > 0 or playerGuess == "exit":
          print(art[artNum])
          print(f"\nYour Word: {wordDisplay}")
          print(f"\nGuesses: {guesses}")
          life = "life" if guessNum == 1 else "lives"  
          playerGuess = input(f"\nYou have {guessNum} {life} available.\n"
                              "Guess a letter: ").lower()
          if playerGuess == "exit":
            print("Game Over - Thanks For Playing!")
            quit()
          guesses.append(playerGuess)
          if playerGuess in wordSelect:
            for pos in range(wordLength):
              letter = wordSelect[pos]
              if letter == playerGuess:
                wordDisplay[pos] = letter
            print("\nCorrect!!")
            guessNum = guessNum - 1
          elif playerGuess not in wordSelect or playerGuess in guesses:
            artNum = artNum + 1
            guessNum = guessNum - 1
            if guessNum > 0:
              print("\nSorry, Wrong Guess! Try Again!")

        ### End ###
        if "_" not in wordDisplay:
          finish = input("\nWell Done!! You Won!!\n"
                        "Do you want to try again? (Press Enter to play)")
          if finish != "":
            print("Game Over - Thanks For Playing!")
            quit()
          else:
            cont = 1
        else:
          finish = input("\nSo Sorry, But You Lost!!\n"
                         f"The Word Was: '{wordSelect}'\n"
                        "Care to try your luck again? (Press Enter to play)")
          if finish != "":
            print("Game Over - Thanks For Playing!")
            quit()
          else:
            cont = 1