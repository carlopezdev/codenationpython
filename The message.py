###### Workflow

# https://app.diagrams.net/#G1wP8MSkD7pwZ-1wuTd-U1h3nhvstyLJi6

###################

import time

#### game over function

def gameover():
    print("""
  ________                        ________                     
 /  _____/_____    _____   ____   \_____  \___  __ ___________ 
/   \  ___\__  \  /     \_/ __ \   /   |   \  \/ // __ \_  __  !
\    \_\  \/ __ \|  Y Y  \  ___/  /    |    \   /\  ___/|  | \/
 \______  (____  /__|_|  /\___  > \_______  /\_/  \___  >__|   
        \/     \/      \/     \/          \/          \/       
    
    
    """)

    print("Thanks for playing this game. We really hope you have enjoyed it.")
    print(" ")


########################


############### play again function

def play_again():
    print("Would you like to play again [Y/N]?")
    playyesno = input()
    if playyesno.upper() == "Y" or playyesno.upper() == "YES":
        print(" ")
        start_game()
    elif playyesno.upper() == "N" or playyesno.upper() == "NO":
        print(" ")
        gameover()
    else:
        print("Sorry, I don't recognize that. Please, try again.")
        play_again()

#######################################




#####################################

################ winner function

def game_win():
    print("""
                                       .''.       
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\'.   '
      *            *..*         :
jgs     *
        *)
        """)

    print("Well done! You are awesome!")

####################################

####  family member function

def poland():
    print("You honestly think that your partner might have travelled to his/her hometown in Poland to start a new life.")
    time.sleep(1)
    print("What would you do? ")
    time.sleep(1)
    choicepolad = input("Would you travel to Poland to search for him/her there? [Y/N] ")
    if choicepolad.upper() == "Y" or choicepolad.upper() == "YES":
        print("You go straight to the airport and take the first flight to the capital city of Warsaw.")
        time.sleep(1)
        print("Then, you catch a train to your partner's hometown called Lublin....")
        time.sleep(1)
        print("..........")
        print("..........")
        print("When you arrive to Lublin, you find your partner's family house and meet his/her cousin...")
        time.sleep(1)
        print("The cousin tells you that he/she has already left, planning to visit his/her Iranian ex-boyfriend/ ex-girlfriend in Tehran.")
        print("You manage to retrieve your partner's old diary and find an address in Iran which may be a clue.")
        time.sleep(1)
        iranyesno = input("Would you rather follow this clue and go to Iran to find your partner there or not? [Y/N] ")
        if iranyesno.upper() == "Y" or iranyesno.upper() == "YES":
            iran()
        elif iranyesno.upper() == "N" or iranyesno.upper() == "NO":
            print("Unfortunately, you are wrong. Your partner did actually go to Iran... Good-bye!")
            gameover()
            play_again()

        else:
            print("Sorry, I don't recognize that. Please, try again.")
            poland()


    elif choicepolad.upper() == "N" or choicepolad.upper() == "NO":
        print("You think that it's not worth it and thus, decide to find another partner.....")
        gameover()
        play_again()

    else:
        print("Sorry, I don't recognize that. Please, try again.")
        poland()


def iran():
    print("Iran")
    print("-------")
    time.sleep(1)
    print("After a very long overnight flight you finally make it and land in Iran.")
    time.sleep(1)
    print("Once you are in Tehran, you take a taxi and ask a driver to go to the address provided.")
    time.sleep(1)
    print("When you get there, you find an abandoned house.")
    time.sleep(1)
    print("You only have an option to talk to a neighbour now in order to learn more about the place.... ")
    time.sleep(1)
    print("The neighbour, called Mohammadi, tells you that nobody has lived there for many years.")
    time.sleep(1)
    print("According to him, the last occupants were a couple but they disappeared suddenly.")
    time.sleep(1)
    print("Since then, the house has been viewed by police on many occasions, making Mohammadi very suspicious and thinking that the couple might have had a problem with the government.")
    time.sleep(1)
    print("In fact, both of them might have been... linked with the revolutionary force or....")
    time.sleep(1)
    print(".....")
    print(".....")
    print(".....")
    time.sleep(1)
    print("have even been SPIES!")
    time.sleep(1)
    print("Do you believe what the neighbour has told you? [Y/N] ")
    time.sleep(1)
    spyyesno = input()
    if spyyesno.upper() == "Y" or spyyesno.upper() == "YES":
        print("Congratulations!!! YOU HAVE RESOLVED THE MYSTERY!")
        time.sleep(1)
        print("You will never see your partner again but you are pleased with yourself since you have found the TRUTH.") 
        time.sleep(1)
        print("You can go home now in peace and live your life again as you wish.")
        time.sleep(1)
        game_win()
        print(" ")
        time.sleep(1)
        gameover()
        play_again()
    
    elif spyyesno.upper() == "N" or spyyesno.upper() == "NO":
        print("You have run out of clues and your partner has vanished. You even decide to contact police but they cannot help you either.")
        time.sleep(1)
        print("You can only go home now and enjoy being a single again.")
        time.sleep(1)
        gameover()
        play_again()


def spain():
    print("Spain")
    print("------")
    time.sleep(1)
    print("You have got an address in Mallorca.")
    time.sleep(1)
    print("You have been there with your partner before to visit his/her family on many ocassions.")
    time.sleep(1)
    print("So you are confident about going straight to your partner's family house by the sea...")
    time.sleep(1)
    print("You find your partner's retired aunt who cheerfully welcomes you.")
    time.sleep(1)
    print("You soon realize that your partner is not there and he/she has not visited her aunt for a long time.")
    time.sleep(1)
    print("You feel disappointed and let down about the whole situation since you have honestly hoped to find your partner there.")
    time.sleep(1)
    print("""The only options, which you are left with are:
    [1] To follow the hint of the Iranian ex-boyfriend/ ex-girlfriend.
    [2] To travel to your partner's hometown in Poland and try to find him/her there.
    [3] To decide to have a holiday in Spain instead and wait for your partner there. 
    """)
    time.sleep(1)
    print("What would you do? Please, select one of the options: ")
    wheninspain = input()
    if wheninspain == "1":
        iran()
    elif wheninspain == "2":
        poland()
    elif wheninspain == "3":
        print("Get real, your partner will never come back to Spain... Good-bye!")
        time.sleep(1)
        gameover()
        play_again()
    else:
        print("Sorry, I don't recognize that. Please, try again.")
        spain()

def familymember():
    print("""You have been given several hints by the family member in regards to a potential location of your partner:
    [1] Your partner has got a Polish heritage so maybe, he/she has gone to Poland.
    [2] Your partner used to have an Iranian boyfriend/ girlfriend so maybe, he/she has gone to Iran.
    [3] Your partner's extended family lives in Spain so maybe, he/she has travelled to Spain?""")
    time.sleep(1)
    print("Please, select one of the options and follow the hint: ")
    choicefamilymember = input()
    if choicefamilymember == "1":
        poland()

    elif choicefamilymember == "2":
        iran()

    elif choicefamilymember == "3":
        spain()

    else:
        print("Sorry, I don't recognize that. Please, try again.")
        familymember()

######################################



#########  work colleague function

def work_colleague():
    print("You decide to speak to your partner's work colleague.")
    time.sleep(1)
    print("The work colleague tells you lots of things, which do you believe?")
    time.sleep(1)
    
    print("""Please choose one of the options:
    [1] Your partner has quitted a job without telling you about it and has not been seen since then.
    [2] Your partner was seen while browsing foreign destinations online during the office hours.
    [3] Your partner revealed during lunch break that he/she is planning to visit a family member in Poland.""")
    print(" ")
    choice = input()

    if choice == "1":
        print("That's a lie. Don't listen to office gossipers.")
        time.sleep(1)
        print("You have run out of clues. Good-bye.")
        time.sleep(1)
        gameover()
        play_again()

    elif choice == "2":
        print("That's not a big deal. Everyone does it!")
        time.sleep(1)
        print("But you find out that he/she has been fired because of it.")
        time.sleep(1)
        print("That unfortunately,leaves you with no further clues to follow. Good-bye.")
        time.sleep(1)
        gameover()
        play_again()
        
    else:
        print("Let's go to Poland!")
        time.sleep(1)
        poland()

########################



################## neighbour function

def neighbour():
    print("You start your investigation by talking to your neighbours....")
    time.sleep(1)
    print("Hopefully, you can get a hint that could help you to find your partner...")
    time.sleep(1)
    print("You approach your closest neighbour and ask him whether he knows anything about your missing partner.")
    time.sleep(1)
    print("The neighbour recalls that...")
    time.sleep(1)
    print("Your partner was seen carrying a SUITCASE and talking over the phone in POLISH language...")
    time.sleep(1)
    print("...and then, catching a TAXI...")
    time.sleep(1)
    print("That means then your partner may have gone to the airport and travelled to Poland!")
    choiceneighbour = input ("Should you then follow this clue and travel to Poland as well? [Y/N] ")
    if choiceneighbour.upper() == "Y" or choiceneighbour.upper() == "YES":
        poland()
    elif choiceneighbour.upper() == "N" or choiceneighbour.upper() == "NO":
        print("Unfortunately, your partner did go to Poland. You have missed him/ her... Good-bye!")
        time.sleep(1)
        gameover()
        play_again()
    else:
        print("Sorry, I don't recognize that. Please, try again.")
        neighbour()

########################

########  secondary choice function

def secondarychoice():
    
    print("""At this point you are left with three options:
    [1] To talk to a neighbour.
    [2] To speak with a family member.
    [3] To visit your partner's workplace.
    """)
    time.sleep(1)
    print("What would you do? Please, select one of the options: ")
    wheretogo = input()
    if wheretogo == "1":
        neighbour()
    elif wheretogo == "2":
        familymember()
    elif wheretogo == "3":
        work_colleague()
    else:
        print("Sorry, I don't recognize that. Please, try again.")
        secondarychoice()

####################

################ initial choice function

def initialchoice():
    print("You wake up in the morning and find that your partner is not there and instead, you find a note next to you: I'll be back. Don't call police.") 
    time.sleep(1)
    print("""
          ,
     __  _.-"` `'-.
    /||/'._ __{)_(
    ||||  |'--.__/
    |  L.(   ^_\^
    \ .-' |   _ |
    | |   )\___/
    |  \-'`:._]
jgs \__/;      '-.
    """)
    print("  ")
    print("Do you decide then to call police or not? [Y/N]")
    response = input()
    time.sleep(1)
    if response.upper() == "Y" or response.upper() =="YES":
        print("It would be better to keep it quiet and stay away from police in this matter. Good-bye.")
        gameover()
        play_again()
    elif response.upper() == "N" or response.upper() == "NO":
        secondarychoice()
    else:
        print("Sorry, I don't recognize that. Please, try again.")
        initialchoice()


########################


###############   Start game function


def start_game():

    print("""

    _____|~~~\_____ _    _____________
  _-~               \    |    /
  _-    | )     \    |__/   \   /
  _-         )   |   |  |     \  /
  _-    | )     /    |--|      |  |
 __-_______________ /__/_______|  |_________
(                |----         |  |
 `---------------'--///\      .`--'
                              `||||
    """)

    time.sleep(1)
    print("This is a story of a mysterious person, who disappears in the middle of the night.")
    time.sleep(1)
    print("Hello and welcome to the game of surprises!")
    global name
    name = input ("What is your name? ")
    time.sleep(1)
    print("Hello {}, it's very nice to meet you.".format(name))
    time.sleep(1)
    response = input ("Are you ready to solve this puzzle [Y/N]?") 
    if response.upper() == "Y" or response.upper() == "YES":
        print("Great. Let's start then!")
        time.sleep(1)
        initialchoice()
    elif response.upper() == "N" or response.upper() == "NO":
        print("OK then. I hope to see you another time.")
        time.sleep(1)
        gameover()
        play_again()
    else:
        print("Sorry, I don't recognize that. Please, try again.")
        start_game()

########################################################

start_game()  