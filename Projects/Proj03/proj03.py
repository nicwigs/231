####################################################
#  Computer Project 03 - Children Addition Game
# Prompt for difficulty and number of problems
# if valid inputs
#     loop for correct number of problems
#        loop for each problem
#           create random number
#           print the random to be summed
#        prompt for answer
#        check if right answer
#     print final score
# say invalid input if needed
#################################################
import random

dif = 0             #difficulty
prob_amt = 0        #amount of problems desired
rand = 0            #random int
upper = 0           # upper range for random int selection
prob_cnt = 0        # counts what problem you are on
add_cnt = 0         # counts what value in each problem your on ex--> 12 + 13 + 60, 13 then added_count = 2
cor_ans = 0         # correct answer
user_ans = 0        #user answer
score = 0           # overal score
percent = 0         # score percent

# all values are integers except percent

dif = int(input("Input difficulty (int>=2): "))
prob_amt = int(input("Number of problems (int>= 1): "))
print()                                                 #formating

if dif >= 2 and prob_amt >= 1:                          #if valid input
    
    for prob_cnt in range(prob_amt):                    #number of problems loop
        print("Problem", prob_cnt + 1, end = ": ")
        add_cnt,cor_ans = 0,0                           #re-initalize after each problem
        
        for add_cnt in range(dif):                      #number of values summed in each problem loop
            upper = 10**dif - 1                         #creates upper bound for random int, 4-> 9999
            rand = random.randint(0,upper)              # random value to be summed
            if add_cnt < dif - 1:                       #if its not the last term, have a "+" after it
                print(rand,end = "+")
            else:                                       #if its the last term, do not include "+"
                print(rand,end = " ")
            cor_ans += rand                             #continue to compute the sum
            
        user_ans = int(input("Your answer: "))          #prompt for answer  
        if user_ans == cor_ans:                         #if correct, say correct, add 1
            print("Correct!")
            score += 1                                
        else:                                           #if wrong, tell correct answer
            print("Wrong, the sum was :", cor_ans)            
        print()                                         #formatting
        
    percent = score/prob_amt * 100                   
    print("You solved", score, "problems out of", prob_amt, " problems which is", round(percent,1),"percent" ) 

else:                                                   #throw error messages when invalid input
    if dif < 2:
        print("Difficulty out of range.")   
    if prob_amt < 1:
        print("Number of problems is not big enough.")

                