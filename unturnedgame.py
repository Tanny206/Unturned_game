



import sys, time


def type(str, speed):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(speed)
    print()



type('Hello there, welcome to unturned', 0.07)

x= input("What is your name- ",)
type('Hi, I will give you a brief description of this game. This is a story based adventure game in which you will come across various adventures and you have to cross them to win the game. Tom will help you in between the game with some instructions and tips. So good luck!', 0.07)

type('The game starts', 0.07)
type('You are a criminal and you are walking on a deserted road. A few meters ahead u saw that the road was diverging. The right side went to the jungle and the left to the desert. You cant go back as the police is waiting there to catch you and put you behind the bars', 0.07)

user_input = input('Where would you like to go (right/left): ')

if(user_input=='right'):

  type("Okayyy, so lets go ahead in the game and see wether your choice is game winning or not", 0.07)
  type('You are walking on the road and suddenly it begins to rain. You do not have an umbrella and at this point of time you only have 1 option, to take shelter beneath a tree or you shall die in the rain.', 0.07)

  user_input_2 = input('What will you do(stay there/take shelter): ')

  if (user_input_2=='take shelter'):
   type('Okayyy so you went towards the tree and slept there.', 0.07)
   print('\U0001F4A4 \U0001F4A4 \U0001F4A4')
   type('When you opened your eyes you saw yourself lying inside a jungle. A tribal group brought you in the jungle and now you have no option to run from there. You have to fight with them to survive. Right now they have gone to get their lunch and you have some time to prepare for the fight. A few minutes later they came back. You still acted as if you are sleeping. They were 3 and you alone and it is impossible to kill all of them at the same time. So you waited a little more. After some time 2 of them went near the river to get some water. This was the correct time for you to attck the 1 person and you did so. You have 2 options kick and punch. Kick will kill the person in 2 moves and punch will kill him in 3 moves. But the kick will make him alert and he will attck you too.', 0.07)
   user_input_3 = input('What will you do (kick/punch): ')
   if(user_input_3=='punch'):
     type('You went near that person and punched him in his face and after giving him 2 punches he was dead.You found a gun in the dead persons clothes which only had 2 bullets. You went back to that tree and acted as if you were sleeping. The other 2 persons were returning with a pot of water in their hand.', 0.07)
     type('Before they find the dead body of their friend you have to kill them also otherwise you are a dead man.  You had a gun which had 2 bullets but you had very poor aim. So now its on you wether you want to use a gun to kill them or use your karate skills. ', 0.07)
     type('Tom- I think you should go for the second option as you have a poor aim and if u miss even 1 shot then they will get to know and will kill you.',0.07)
     user_input_4 = input("What will you like to do(gun or your skills): ")
     if user_input_4=='gun':
       type('You missed your shot and they killed you. Game Over!',0.07)
       print('\U0001F480 \U0001F480 \U0001F480')
     elif user_input_4=='your skills':
       type('You went towards them slowly and silently killed both of them one by one. You managed the way out of the jungle and after walking for few minutes you reached your home. Game Over!',0.07)
   elif (user_input_3=='kick'):
    type('You went near that guy and kicked him but after that he attacked you and killed you with his gun. Game Over!',0.07)
    print('\U0001F480 \U0001F480 \U0001F480')

  elif(user_input_2=='stay there'):
   type('Bad choice. A few minutes later you died. GAME OVER!', 0.07)
   print('\U0001F480 \U0001F480 \U0001F480')

  
  else:
   type('Invalid option', 0.07)
  

elif(user_input=='left'):
  type('Okayyy, so lets go ahead in the game and see wether your choice is game winning or not', 0.07)
  type('You went towards the left road and after walking for a few minutes you saw that the road went towards a desert. You have no other option but to go in the desert and find a way out of the desert and reach your home. You saw camels and snakes everywhere in the desert. You were sleepy and went towards a tree and slept there for few minutes.', 0.07)
  type('When you opened your eyes you saw that a man was standing in front of you with a gun in his hand. Your biggest enemy Dan was standing in front of you. He was there to take you to the police and win the price which was put on your head. You have 2 options either fight him or go with him without any violence to the police station.',0.07)
  user_input_5= input('What would you like to do(fight/go with him): ')
  if user_input_5=='fight':
    type('The most important thing for you was to take his gun otherwise he will kill you. You took some sand in your hand and threw it in his eyes and took that gun and killed him.',0.07)
    type('You went ahead and saw that the desert was diverging. Now you have to choose where you want to go.',0.07)
    user_input_6 = input('Where would you go now(right/left): ')
    if user_input_6=='right':
      type('You went ahead and saw that the right side was the home of animals. They all saw you and attacked you. GAME OVER!', 0.07)
      print('\U0001F480 \U0001F480 \U0001F480')
    elif user_input_6=='left':
      print('Hooooorah! After walking for a few minutes you came across the main road and went to your home. GAME OVER!',0.07)
  elif user_input_5=='go with him':
    type('You went with him to the police station and you were put behind the bars. GAME OVER!')
    print('\U0001F480 \U0001F480 \U0001F480')

else:
  type('Invalid option', 0.07)





