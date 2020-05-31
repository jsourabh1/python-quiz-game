''' started on the thrusday 29 may.2020
author@saurabh jain 
'''
import math
import operator
import sys


def begineer():
    
    
    
    
      
    score=0
# 1st questiion
    print('\n 1) Among the top 10 highest peaks in the world, how many lie in Nepal?')
    print('\n 1.6 \t\t 2.7 \n\n 3.8 \t\t 4.9')
     
    option=int(input('your answer is--'))
    
    if option==3:
        print('______________________')
        print(' \nEXCELLENT! you  got answer is correcT')
        score+=1
      
     
    else:
      print('OOPS!you got answerr is wrong')
      
# 2nd question
    print("\n 2) Who developed Python language?")
    print("\n\n 1.Alan Turing\t\t 2.Guido van Rossum \n\n 3.Dennis Ritchie\t\t 4.Paul Allen")
    option=int(input('your answer is--'))
     
    if option==2:
        
        print('______________________')
        print('\nEXCELLENT! you got the right answer')
        score+=1
      
     
    else:
      print('OOPS! you got wrong answer ')
#3rd question
    print("\n\n 3) Which of the following is a Palindrome number?") 
    print("\n\n 1.42042\t\t  2.101010\n\n 3.23232\t\t  4.01234")
   
    if int(input('your answer is--'))==3:
        print('______________________')
        print('\nEXCELLENT! you got the right answer')
        score+=1
    else:
        print('OOPS! you got wrong answer ')
#4th question
    print("\n\n\n 4) who developed Java?") 
    print("\n\n 1.Bjarne Stroustrup \t\t 2.James Gosling\n\n 3.Bill Joy\t\t  4.Bill Gates")
    
    if int(input('your answer is--'))==2:
        print('______________________')
        print('\nEXCELLENT! you got the right answer')
        score+=1
    else:
        print('OOPS! you got wrong answer ')
        
        

    print('\nYour score is ',score)
    m=score


    if m>=3:
        
       print('\ncongratulation! you egligible or the second round')
       advance()
    
    
    else:
        print('\nsorry! you are not egligible or the second round')
        print('\npress o to play  the game again')
        if str(input('your answer'))=='o':
            homepage()
            
        else:
            print('\nwrong input')
            
        
    
    
    
    
    

totalscore=0
    
def advance():
    print('\nwelcome to the next level of the quiz')
    
    
    score1=0
# 1st question    
    print("\n 1) What is the National Game of England?")
    print("\n\n 1.Football \t\t 2.Basketball\n\n 3.Cricket \t\t 4.Baseball")
    if int(input('your answer is--'))==3:
        print('\nEXCELLENT! you got the right answer')
        score1+=1
    else:
        print('\nOOPS! you got wrong answer')
        score1-=1

# 2nd question
    print('\n\n\n 2) Who is the founder of google?')
    print('\n\n 1.Larry Page \t\t 2.Sergey Brin \n\n 3.Ken Thompson\t\t 4.Santoshi Nakamoto')    
    if int(input('your answer is--'))==1:
        print('\nEXCELLENT! you got the right answer')
        score1+=1
        
    else:
        print('\nOOPS! you got wrong answer')
        score1-=1
# 3rd question
        
    print("\n\n\n 3) The Laws of Electromagnetic Induction were given by?")
    print("\n\n 1.Faraday \t\t 2.Tesla \n\n 3.Maxwell \t\t 4.Coulomb")
    
    if int(input('your answer is--'))==1:
        
        print('\nEXCELLENT! you got the right answer')
        score1+=1
    else:
        print('\nOOPS! you got wrong answer')
        score1-=1
# 4th question
        
    print("\n\n\n 4) In what unit is electric power measured?")
    print("\n\n 1.Coulomb \t\t 2.Watt \n\n 3.Power \t\t 4.Units")
    
    if int(input('your answer is--'))==2:
        
        print('\nEXCELLENT! you got the right answer')
        score1+=1
    else:
        print('\nOOPS! you got wrong answer')   
        score1-=1
# 5th question
    print("\n\n\n 5) aWhich element is found in Vitamin B12?")
    print("\n\n 1.Zinc \t\t 2.Cobalt \n\n 3.Calcium \t\t 4.Iron")

    if int(input('your answer is--'))==2:
        
        print('\nEXCELLENT! you got the right answer')
        score1+=1
    else:
        print('\nOOPS! you got wrong answer')
        score1-=1

# 6th question
    print("\n\n\n 6) What is Git?")
    print("\n\n 1.Distributed version control system \t\t 2.friendly version control system \n\n 3.Website \t\t 4.Web Application")
        
    if int(input('your answer is--'))==1:
       
        print('\nEXCELLENT! you got the right answer')
        score1+=1
    else:
        print('\nOOPS! you got wrong answer')
        score1-=1

# 7th questio
    print("\n\n\n 7) How many times a piece of paper can be folded at the most?")
    print("\n\n 1.6 \t\t 2.7 \n\n 3.8 \t\t 4.Depends on the size of paper")
    
    if int(input('your answer is--'))==2:
       
        print('\nEXCELLENT! you got the right answer')
        score1+=1
    else:
        print('\nOOPS! you got wrong answer')
        score1-=1
        
# 8th question
    print("\n\n\n 8) Who developed Git?")
    print("\n\n 1.Steve Ballmar \t\t 2.Mosh Hamedani \n\n 3.Junio Hamano \t\t 4.Larry Page")    
    
    if int(input('your answer is--'))==3:
       
        print('\nEXCELLENT! you got the right answer')
        score1+=1
    else:
        print('\nOOPS! you got wrong answer')
        score1-=1    
    
    print('\nyour final score is',score1)
    if score1>0:
        m=score1*100000
        print('\ncongratulation ! You won the prize money of Rs.',m)
    else:
        print('\nbad luckkk! next time')
        
    totalscore=score1
    leaderboard()
    











def helpinghand():
    print('_____________________________________')
    print('1)  There are two rounds in the game first is Begineers round and second is experienced round.')
    print('\n2) In the begineers round Three question will be asked ,each question will be of 1 marks and there is no negative marking. ')
    print('\n3) But to enter in the experienced round to your score at least is equal to greater than 8 marks.')
    print('\n4) If you will be unable to get the minimum marks then you will not enter in the experienced round.')
    print('\n5) Then in the experienced round there are Nine question. ')
    print('\n6) But there is twist in the round that the negative marking is involved in this round.')
    print('\n7) Right answerr will give you Rs.1 lacs.')
    print('\n8) And wroung answer will deduct your Rs.50K from your total earning.')
    print('\n')
    
    print('press 2 to go the home page')
    print('press 3 to quit the game')
    choice=int(input('enter youur choice \t'))
    
    if choice==2:
        
       homepage()
       
    else:
        
       sys.exit('you come out form the game')

def mainmenu():
    print('_______________________')
    print('\n')
    print('1) press s to start the game ')
    print('2) press l to see the leadboard')
    
    choice2=str(input('enter the choice \t'))
    
    if choice2=='s':
        print('\nLets start the game')
        begineer()
    
    else:
        print('\nThis is the leaderboard')
        leaderboard()
        


# designing the home 
def homepage():
    
    
    a='\n press h for the help or instruction for the game'
    print(a.upper())
    b='\n press m for the main menu of the game' 
    print(b.upper())
    c ='\n press q to quit the game'
    print(c.upper())
    choice=str(input('ENTER YOUR CHOICE'))
    
    if choice=='H':
       print('THIS IS THE INSTRUCTION  FOR THE GAME')
       helpinghand
    
    
    elif choice=='M':
        print('THIS IS MAIN MENU FOR THE GAME ')
        mainmenu()
    
    elif choice=='Q':
         sys.exit('YOUU COME OUT FROM THE GAME')
    else:
         print('YOU ENTER THE WRONG INPUT')
   


def leaderboard():
    
    sm=int(input('what is your final score--'))
    m=str(sm)
    
    f=open('first quiz.txt','a')
    f.writelines('\nname of participant\t\t\t\ttotalscore')
    f.writelines('\n')
    f.writelines(n)
    f.writelines('\t\t\t\t\t\t\t\t\t')
    f.write(m)
    #f.writelines()
    f.close()
    f=open('first quiz.txt','r')
    for x in f:
        print(x)
    f.close     
     
    
    
    

print('WELCOME TO THE PYTHON PROGRAMMING GAME!')
print('\nHOPE YOU WILL ENJOY THE GAME ')
print('  \nWIN THE PRIZE MONEY  ')
print('____________________________________')
n=str(input('ENTER YOUR NAME\t'))
print('___________________________________')
print('\nWe welcome '+n+' in the game')
a='\n press h for the help or instruction for the game'
print(a.upper())
    
b='\n press m for the main menu of the game' 
    
print(b.upper())
    
c='\n press q to quit the game'
    
print(c.upper())
    
choice1=str(input('ENTER YOUR CHOICE \t'))
    
if choice1=='H':
    
    print('THIS IS THE INSTRUCTION  FOR THE GAME')
    helpinghand()
elif choice1=='M':
    print('THIS IS MAIN MENU FOR THE GAME ')
    mainmenu()
    
elif choice1=='Q':
    
    sys.exit('YOU COME OUT FROM THE GAME')
else:
    print('YOU ENTER THE WRONG INPUT')
    print('WELCOME TO THE PYTHON PROGRAMMING GAME!')
    print('\nHOPE YOU WILL ENJOY THE GAME ')
    print('  \nWIN THE PRIZE MONEY  ')
    print('____________________________________')
    n=str(input('ENTER YOUR NAME\t'))
    print('\nYOUR NAME IS' ,n)
    a='\n press h for the help or instruction for the game'
    print(a.upper())
    b='\n press m for the main menu of the game' 
    print(b.upper())
    c ='\n press q to quit the game'
    print(c.upper())
    choice=str(input('ENTER YOUR CHOICE'))
    if choice=='H':
       print('THIS IS THE INSTRUCTION  FOR THE GAME')
       mainmenu()
    elif choice=='M':
         print('THIS IS MAIN MENU FOR THE GAME ')
         helpinghand()
    elif choice=='Q':
         sys.exit('YOUU COME OUT FROM THE GAME')
    else:
         print('YOU ENTER THE WRONG INPUT')
 

     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
        
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




















