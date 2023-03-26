# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.

# Student ID: 20211154
# Date:15/03/2022 


# Multiple Outcomes & Histogram

#(03)

pass_credits  = 0
defer_credits = 0                                  #intializing the variables to zero
fail_credits  = 0

prog_count    = 0
mod_tra_count = 0
mod_ret_count = 0                                #intializing the counter variables to zero
ex_count      = 0

condition = True                              #assingning the true value to the condition variable


print("--WELCOME TO THE STAFF VERSION-- \n")

while True:                                    #starting the looping process
     while condition:
        try:
            pass_credits = int(input("Enter your total PASS credits:\n"))             #getting user input for the pass credits            
            if pass_credits % 20 == 0 and 0 <= pass_credits <= 120:
                break
            else:
                print("Not in the range")                                             #handling the not in the range and integer required errors in pass credits
        except ValueError:
            print("Integer required")

     while condition:
        try:
            defer_credits = int(input("Enter your total DEFER credits:\n"))           #getting user input for the defer credits
            if defer_credits % 20 == 0 and 0 <= defer_credits <= 120:
               break
            else:
                print("Not in the range")
        except ValueError:                                                            #handling the not in the range and integer required errors in defer credits
            print("Integer required")

     while condition:
        try:
            fail_credits = int(input("Enter your total FAIL credits:\n"))             #getting user input for the fail credits
            if fail_credits % 20 == 0 and 0 <= fail_credits <= 120:
                break
            else:
                print("Not in the range")
        except ValueError:                                                            #handling the not in the range and integer required errors in fail credits
            print("Integer required")

     while condition:
        total = (pass_credits,defer_credits,fail_credits)               
        tot_credits = sum(total)                                                      #handling the total incorrect error
        if tot_credits != 120:
            print("Total incorrect")
            break
        else:
            if pass_credits == 120:                                
                print("Progress")
                prog_count = prog_count + 1
                break
            elif pass_credits == 100:
                print("Progress(Module trailer)")                                                             #conditional statements to show the respective grade/progression outcome the user got
                mod_tra_count = mod_tra_count + 1                                                             ##incrementing  the counter variables
                break
            elif 0 <= pass_credits <= 80 and 0 <= defer_credits <= 120 and 0 <= fail_credits <= 60:
                print("Do not progress – module retriever")
                mod_ret_count = mod_ret_count + 1
                break
            elif 0 <= pass_credits <= 40 and 0 <= defer_credits <= 40 and 80 <= fail_credits <= 120:
                print("Exclude")
                ex_count = ex_count + 1
                break


     while condition:
        print("Would you like to enter another set of data?")
        user_option = input("Enter 'y' for yes or 'q' to quit and view results:\n")                           #asking the user option whether to quit using q or continue the programme using y 
        user_option = user_option.lower()
        if user_option == 'y':
            break
        elif user_option == 'q':
            condition = False
            
            print("*" * 60)
            print("---Horizontal Histogram---")
            print()
            print(f"Progress {prog_count}:", prog_count * "*")
            print(f"Module_trailer {mod_tra_count}:", mod_tra_count * "*")                                  #formatting and printing out the horizontal histogram 
            print(f"Module_retriever {mod_ret_count}:", mod_ret_count * "*")
            print(f"Exclude {ex_count} :", ex_count * "*")
            print()
            print(prog_count + mod_tra_count + mod_ret_count+ ex_count,"outcomes in total \n")
            break


        else:
            print("You entered an invalid input.")                                                   #handling the error if user inputs a character other other than y or q               
            condition = False                                                                        #looping stops and the programme ends












