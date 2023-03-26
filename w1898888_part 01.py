# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.

# Student ID: 20211154
# Date:10/03/2022 


#Validation


#(02)

pass_credits  = 0
defer_credits = 0              #intializing the variables to zero
fail_credits  = 0

prog_count    = 0
mod_tra_count = 0
mod_ret_count = 0              #intializing the counter variables to zero
ex_count      = 0

condition = True               #assisnging the true value to the condition variable

print("--WELCOME TO THE STUDENT VERSION-- \n")

i = 0                                              #intializing the i varaible to zero
while i<1:
     while condition:                                                     
        try:
            pass_credits = int(input("Please enter your credits at pass:\n"))              #getting user input for the pass credits
            if pass_credits % 20 == 0 and 0 <= pass_credits <= 120:                                                    
                 break
            else:
                print("Not in the range")
        except ValueError:                                                                #handling the not in the range and integer required errors in pass credits
            print("Integer required")

     while condition:
        try:
            defer_credits = int(input("Please enter your credit at defer:\n"))           #getting user input for the defer credits                                   
            if defer_credits % 20 == 0 and 0 <= defer_credits <= 120:
               break
            else:
                print("Not in the range")
        except ValueError:                                                              #getting user input for the fail credits
            print("Integer required")

     while condition:
        try:
            fail_credits = int(input("Please enter your credit at fail:\n"))          
            if fail_credits % 20 == 0 and 0 <= fail_credits <= 120:
                break
            else:
                print("Not in the range")
        except ValueError:                                                             #handling the not in the range and integer required errors in fail credits
            print("Integer required")

     while i<1:
        total = (pass_credits,defer_credits,fail_credits)                              #handling the total incorrect error
        tot_credits = sum(total)
        if tot_credits != 120:
            print("Total incorrect")
            break
        else:
            if pass_credits == 120:                                  
                print("Progress")
                break
            elif pass_credits == 100:                                                 #conditional statements to show the respective grade/progression outcome the user got
                print("Progress(Module trailer)")                                                                                       
                break
            elif 0 <= pass_credits <= 80 and 0 <= defer_credits <= 120 and 0 <= fail_credits <= 60:
                print("Do not progress – module retriever")
                break
            elif 0 <= pass_credits <= 40 and 0 <= defer_credits <= 40 and 80 <= fail_credits <= 120:
                print("Exclude")
                break

     i = i+1         #incrementing
     
i=i+1                #incrementing
