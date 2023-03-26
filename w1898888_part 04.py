# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.

# Student ID : 20211154
# Date:13/04/2022 


#Validation

#(02)

pass_credits  = 0
defer_credits = 0                        #intializing the variables to zero
fail_credits  = 0

prog_count    = 0
mod_tra_count = 0
mod_ret_count = 0                        #intializing the counter variables to zero
ex_count      = 0
Max           = 0

list_prog     = []                          #making 4 empty lists for the respective progresion outcomes
list_mod_ret  = []
list_mod_tra  = []
list_ex       = []
 
condition = True                        #assisnging the true value to the condition variable


 
print("WELCOME TO THE STAFF VERSION")
while True:
    while condition:
        try:
            pass_credits = int(input("Please enter your credits at pass:\n"))          #getting user input for the pass credits
            if pass_credits % 20 == 0 and 0 <= pass_credits <= 120:
                break
            else:
                print("Not in the range")
        except ValueError:                                                             #handling the not in the range and integer required errors in pass credits
            print("Integer required")

    while condition:
        try:
            defer_credits = int(input("Please enter your credits at defer:\n"))        #getting user input for the defer credits              
            if defer_credits % 20 == 0 and 0 <= defer_credits <= 120:
               break
            else:
                print("Not in the range")
        except ValueError:                                                             #handling the not in the range and integer required errors in defer credits
            print("Integer required")

    while condition:
        try:
            fail_credits = int(input("Please enter your credits at fail:\n"))          #getting user input for the fail credits         
            if fail_credits % 20 == 0 and 0 <= fail_credits <= 120:
                break
            else:
                print("Not in the range")
        except ValueError:                                                             #handling the not in the range and integer required errors in fail credits
            print("Integer required")

    while condition: 
        total = (pass_credits,defer_credits,fail_credits)                              #handling the total incorrect error          
        tot_credits = sum(total)
        if tot_credits != 120:                                                           
            print("Total incorrect")
            break
        else:
            if pass_credits == 120:                                                        
                print("Progress")
                prg  =f"progress - {pass_credits},{defer_credits},{fail_credits}"
                list_prog.append(prg)
                prog_count = prog_count + 1
                break
            elif pass_credits == 100:
                print("Progress(Module trailer)")
                tra =f"Progress (module trailer) - {pass_credits},{defer_credits},{fail_credits}"               #conditional statements to show the respective grade/progression outcome the user got
                list_mod_tra.append(tra)                                                                               
                mod_tra_count = mod_tra_count + 1                                                               #formatting and appending user inputs to the respective lists
                break
            elif 0 <= pass_credits <= 80 and 0 <= defer_credits <= 120 and 0 <= fail_credits <= 60:
                print("Do not progress – module retriever")                                                     #incrementing  the counter variables
                ret  =f"Module retriever - {pass_credits},{defer_credits},{fail_credits}"
                list_mod_ret.append(ret)                                                                                 
                mod_ret_count = mod_ret_count + 1
                break
            elif 0 <= pass_credits <= 40 and 0 <= defer_credits <= 40 and 80 <= fail_credits <= 120:
                print("Exclude")
                ex  =f"Exclude – {pass_credits},{defer_credits},{fail_credits}"
                list_ex.append(ex)
                ex_count = ex_count + 1
                break

    while condition:
        print("Would you like to enter another set of data?")
        user_option = input("Enter 'y' for yes or 'q' to quit and view results:\n")                       #asking the user option whether to quit using q or continue the programme using y
        user_option = user_option.lower() 
        if user_option == 'y':
            break
        elif user_option == 'q':
            condition = False
            print("*" * 60)
            print("--VERTICAL HISTOGRAM--")
            Max = max(prog_count, mod_tra_count, mod_ret_count, ex_count)                                 #equalizing the 4 progression outcomes to the max function       
            print("Progress|Trailing|Retriever|Excluded")
            for i in range(Max):
                if prog_count > 0:
                    prog_count = prog_count - 1
                    print("   *    ", end=" ")
                else:
                    print('  ', end=" ")
                if mod_tra_count > 0:
                    mod_tra_count = mod_tra_count - 1        
                    print("   *    ", end=" ")
                else:                                                                                  #printing out the vertical histogram using for loop
                    print('  ', end=" ")                                    
                if mod_ret_count > 0:
                    mod_ret_count = mod_ret_count - 1
                    print("    *      ", end=" ")        
                else:
                    print('  ', end=" ")
                if ex_count > 0:
                    ex_count = ex_count - 1
                    print("   *      ", end=" ")
                else:
                    print('  ', end=" ")
                print()
        else:
             print("You entered an invalid input.")                    #handling the error if user inputs a character other other than y or q 
             condition = False                                         #looping stops and the programme ends                     
             
        print()
        print("*" * 60)
        print("--LIST--")

        for i in range(0,len(list_prog)):
            print(list_prog[i])
        for i in range(0,len(list_mod_tra)):
            print(list_mod_tra[i])
        for i in range(0,len(list_mod_ret)):                           #printing the 4 lists for the respective progression outcomes using for loop
            print(list_mod_ret[i])
        for i in range(0,len(list_ex)):
            print(list_ex[i])

            

        f = open("myfile.txt","w")                                     #opens the text file
        for i in range(0,len(list_prog)):
            a = list_prog[i]                       
            f.write(a)                                      
            f.write('\n')
        for i in range(0,len(list_mod_tra)):         
            b = list_mod_tra[i]                                       #writing the 4 lists for the respective progression outcomes according to the user inputs
            f.write(b)     
            f.write('\n')
        for i in range(0,len(list_mod_ret)):
            c = list_mod_ret[i]
            f.write(c)
            f.write('\n')
        for i in range(0,len(list_ex)):
            d = list_ex[i]                                          
            f.write(d)
            f.write('\n')
        f.close()                                                     #closes the text file
        f = open("myfile.txt","r")                                    #opens the text file
        f.readline()                                                  #reading the text file
        f.close()                                                     #closes the text file
        
        

