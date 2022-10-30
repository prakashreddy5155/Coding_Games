# lets create a game which can generate a random number 
# its me Prakash Reddy
import sys
import random 
import time as t



def printing_with_time_delay(str):
    for i in str:
        print(i,end = "")
        sys.stdout.flush()
        t.sleep(0.009)



def four_level(initial,final):
    comp = random.randint(initial,final)

    count = 1
    usrnum = 0
    while(comp!=usrnum):
        
        bs1 = "Enter the user number(range (1 ,",final,")"
        printing_with_time_delay(bs1)
        usrnum = int(input(" :"))

        if(usrnum> comp):
            low = "Provide a lower number ! \n"
            printing_with_time_delay(low)
                
        elif(usrnum < comp):
            high = "Provide a Higher number ! \n"
            printing_with_time_delay(high)
                

        elif(usrnum == comp):
            guess  = "you guessed in ",count," Attempts!\nEnjoy\n"
            printing_with_time_delay(guess)
                
        count+=1
        
    adv = "Enter (advanced) to play the advanced level: "
    printing_with_time_delay(adv)
    advan = input()
    if(advan == 'advanced'):
        advanced_level()



def advanced_level():
    basic3 = "Now you know how to play the game\nTO make game even more intreasting \n"
    printing_with_time_delay(basic3)
    bs3 = "Input the maximum range(ENter any integer number) "
    printing_with_time_delay(bs3)
    max_range = int(input(" :"))
    comp = random.randint(1,max_range)
    count = 0
    usrnum = 0
    while(comp!=usrnum):
        # usrnum = int(input(f"Enter the user number(range (1,{max_range}) ): "))
        val = "Enter the user number(range(1, ",max_range," )"
        printing_with_time_delay(val)
        usrnum = int(input(": "))
        if(usrnum> comp):
            low = "Provide a lower number !\n"
            printing_with_time_delay(low)
        elif(usrnum < comp):
            high = "Provide a Higher number !\n"
            printing_with_time_delay(high)
        elif(usrnum == comp):
            equal = "you guessed in ",count," Attempts!\nEnjoy\n"
            printing_with_time_delay(equal)

        count+=1
        if(count >= 20):
            # show = input("ENter 'reveal' to reveal the number: ")
            show1 = "Enter 'reveal' to reveal the number "
            show = input(" :")
            if(show == 'reveal'):
                # print(f"THe number computer assumed is {comp}")
                de = "The number computer assumed is ",comp
                printing_with_time_delay(de)
                print()
                print()
                break;




intro = "---------Welcome to the Number guessing game--------\n"
printing_with_time_delay(intro)

   

basic = "****This game contains Three levels ranging from easy to hard****\n"
printing_with_time_delay(basic)


basic2 = '''Enter level1 to play level1 \nEnter level2 to play level2\nEnter level3 to play level3\nEnter level4 to play level4(insane level)'\n'''
printing_with_time_delay(basic2)

    
bs = "Type one option among them"
printing_with_time_delay(bs)
level = input(" :")
if(level == 'level1'):
    four_level(1,11)
elif(level == 'level2'):
    four_level(1,21)
elif(level == 'level3'):
    four_level(1,31)
elif(level == 'level4'):
    four_level(1,101)





