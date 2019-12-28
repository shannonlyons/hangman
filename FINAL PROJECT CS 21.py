#Shannon Lyons and #Hannah Minns
#CS21
#Hangman

#main function
def main():
    #print statement with directions, all letters are lowercase 
    print("Welcome to Hangman!")
    print("")
    print("The goal of this game is to guess the letters of an unknown word until you either fill in the entire word correctly, or run out of tries.")
    print("")
    print("There are three levels, 1 for beginner, 2 for intermediate, and 3 for master.")
    keep_playing = 'y'
    while keep_playing == 'y' or keep_playing == 'Y':
        #Ask for level (beginner, intermediate, hard)
        print("What level do you want to play?")
        #while True:
        try:
            level = int(input("Enter 1, 2, or 3: "))
            if level ==1 or level ==2 or level ==3:
                print('')
            else:
                print("Invalid input. Please enter an integer between 1 and 3.")
                continue
        except ValueError:
            print("Invalid input, must be an integter. Please enter an integer between 1 and 3.")
            continue

        #select 1 random word from the list
        final=[]
        randword = randomword(level)
        histogram1 = histogram(randword)
        for ch in histogram1:
            print(ch, end='')
        print('')
        tries = (len(histogram1) + 5)
        MIN_TRIES = 0
        print('You have', tries, 'tries to correctly guess the word. Good luck!')
        guess = str(input("Enter a letter: "))
        #while True:
        if guess.isalpha():
            print('')
        else:
            guess = str(input("Please enter a letter: "))
        used = []
        win = True
        while tries > MIN_TRIES and win == True:
            if guess in randword:
                while True:
                    try:
                        index_r = randword.index(guess)
                        histogram1[index_r]= guess
                        randword[index_r] = ('_')
                        print('')
                    except ValueError:
                        break
                #while True:
                for ch in histogram1:
                    print(ch, end='')  
                print('')
                dash = '_'

                if dash not in histogram1:
                    print('Congratulations, you win!')
                    win = False
                    break
                    
                else:
                    guess = str(input("Enter a letter: "))
                    
                    if guess.isalpha():
                        win==True
                    else:
                        guess = str(input("Please enter a letter: "))
                        


            if guess not in randword:
              
                while tries > MIN_TRIES:
                    tries -= 1
                    if tries == MIN_TRIES:
                        print('Sorry, you are out of tries. You lose.')
                        break
                    else:
                        print('Sorry, your guess was incorrect. You have', tries, 'tries left.')
                        guess = str(input('Enter a letter: '))
                        break


                    
            
        keep_playing = (input('Would you like to play again? Please enter y or n: '))


        while True:
            try:
                if keep_playing == 'y' or keep_playing == 'n':
                    break
                else:
                    print("Please enter y or n.")
                    keep_playing = (input('Would you like to play again? Please enter y or n: '))  
            except ValueError:
                print("Please enter y or n.")
                break

def randomword(level):
    import random
    
    master= ['abruptly','absurd''abyss','bagpipes','bandwagon','banjo','buckaroo','buffalo','buffoon','buzzing','buzzwords','crypt','dirndl','disavow','dizzying','duplex','dwarves','embezzle','flapjack','frizzled','fuchsia','funny','gabby','galaxy','galvanize','gazebo','giaour','gizmo','glowworm','glyph','gnarly','gnostic','gossip','grogginess','haiku','haphazard','hyphen','iatrogenic','icebox','injury','ivory','jaundice','jawbreaker','jaywalk','jazziest','jazzy','jelly','jigsaw','jinx','jiujitsu','jockey','jogging','joking','jovial','joyful','juicy','jukebox','jumbo','kayak','kazoo','keyhole','khaki','kilobyte','kiosk','mystify','naphtha','nightclub','nowadays','numbskull','nymph','onyx','ovary','oxidize','oxygen','pajama','peekaboo','phlegm','pixel','pizazz','pneumonia','polka','pshaw','psyche','puppy','puzzling','quartz','queue','quips','quixotic','quizzes','quorum','razzmatazz','rhubarb','rhythm','rickshaw','schnapps','sphinx','squawk','stronghold','stymied','subway','swivel','syndrome','thriftless','thumbscrew','topaz','transcript','vaporize','vixen','vodka','voodoo','vortex','zephyr','zigzagging','zilch','zipper','zodiac','zombie']
    beginner = ['quilt','fat','thin','short','gut','belly','live','toes','head','now','rat','mat','hem','red','read','shoe','boot','sad','happy','cute','for','yes','trust','give','load','lobby','lob','pop','mouse','xray','get','quit','just','blow','ash','tree','fish','mom','cat','dad']
    intermediate = ['icy','committee','report','love','few','produce','ablaze','enter','bury','club','egg','chivalrous','materialistic','chicken','nappy','cannon','sore','plough','fetch','excite','worry','arrogant','jobless','heat','base','farm','giraffe','confuse','flippant','teeth','incredible','drain','robust','spray','dad','frame','glass','bent','fierce','bashful','tin','spoon','silly','grip','potato','control','toys','windy']

    wordlist = []
    if level == 1:
        word = random.choice(beginner)

    elif level == 2:
        word = random.choice(intermediate)

    elif level == 3:
        word = random.choice(master)

    for ch in word:
        wordlist.append(ch)
        
    return wordlist

#use _ to display letters
def histogram(wordlist):
    histogram_list = []

    num = len(wordlist)

    for i in range (0,num):
        histogram_list.append("_")
    return histogram_list


main()
