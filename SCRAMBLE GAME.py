name = input("Enter Player name: ")
print("============================================================================")
intro = input("""Welcome to Guess The Scramble Words!
type YES to enter the game and type NO to exit: """)
points = 0

if intro == 'YES' or intro == 'yes':
    ch = input("Choose difficulty to enter[EASY/HARD]:")#CONDITION FOR CHOOSING DIFFICULTY
    print("========================================================================")
    if ch == 'EASY' or ch == 'easy':#EASY MODE
        print("Let's proceed! Guess the following words to get points!")
        g1 = input("1. Guess this word 'MPIKUPN': ")#1st Question
        if g1 == 'PUMPKIN' or g1 == 'pumpkin':
            print("Correct! The answer is Pumpkin.")
            points += 1 #If the statement is true , you will get 1 point
        else:
            print("Incorrect! ")
        g2 = input("2. Guess this word 'MPUTREOC': ")#2nd Question
        if g2 == 'COMPUTER' or g2 == 'computer':
            print("Correct! The answer is Computer.")
            points += 1 #If the statement is true , you will get 1 point
        else:
            print("Incorrect!")
        g3 = input("3. Guess this word 'CEHARTE': ")#3rd Question
        if g3 == 'TEACHER' or g3 == 'teacher':
            print("Correct! The answer is Teacher.")
            points += 1 #If the statement is true , you will get 1 point
        else:
            print("Incorrect!")
        print("The total points yo uget is: ",points,"Point/s")#Calculating the total points
        feed = input("Did you enjoy the game[Y/N]? ")
        if feed == 'Y' or feed == 'y':
                print("I'm happy to hear that! Thanks for playing this game",name,"!")
        else:
             print("""Oh sorry to hear that! Thanks for your feedback we will improve this right soon. Thank you for playing this game""",name,"!")
        print("========================================================================")
#---------------------------------------------------------------------------------------
    else: #NESTED ELSE STATEMENT
        if ch == 'HARD' or ch == 'hard':#HARD MODE
            print("Let's proceed! Guess the following words to get points! ")
            h1 = input("Guess this word 'YPSYCGOLO': ")#1st question
            if h1 == 'PYSHOCOLOGY' or h1 == 'psychology':
                print("Correct! The answer is Psychology.")
                points += 1 #If the statement is true , you will get 1 point
            else:
                print("Incorrect! ")
            h2 = input("2. Guess this word 'LPYOSIPHHO': ")#2nd Question
            if h2 == 'PHILOSOPHY' or h2 == 'philosophy':
                print("Correct! The answer is Philosophy. ")
                points += 1 #If the statement is true , you will get 1 point
            else:
                print("Incorrect! ")
            h3 = input("3. Guess this word 'OIGYOBL': ")#3rd question
            if h3 == 'BIOLOGY' or h3 == 'biology':
                print("Correct! The answer is Biology. ")
                points += 1  #If the statement is true , you will get 1 point
            else:
                print("Incorrect!")
            print("The total points yo uget is: ",points,"Point/s")#Calculating the total points
            feed = input("Did you enjoy the game[Y/N]? ")
            if feed == 'Y' or feed == 'y':
                print("I'm happy to hear that! Thanks for playing this game",name,"!")
            else:
                print("""Oh sorry to hear that! Thanks for your feedback we will improve this right soon. Thank you for playing this game""",name,"!")
            print("========================================================================")
            
else:
    print("Oh! Sorry to hear that. Thanks for entering this game.")