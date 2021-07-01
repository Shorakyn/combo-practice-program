import numpy as np
while True:
    combo_name = input("Combo training! Whats the name of the route? (optional, can be blank)\n> ").title()
    if combo_name == '' or combo_name.strip() == '':
        combo_name = "<combo_name>"
        
    combo_amount = input("How many times would you like to attempt it?\n> ")
    while not combo_amount.isdecimal():
        combo_amount = input('Please enter a non-decimal number.\nHow many times would you like to attempt it?\n> ')
    combo_amount = int(combo_amount)

    combo_row = input("In a row? (Y/N)\n> ").lower()
    while combo_row != 'y' and combo_row != 'n':
        combo_row = input('Please put either y or n.\nIn a row? (Y/N)\n> ')
            
    if combo_row == 'y':
        combo_row = True
    else:
        combo_row = False

    attempts = []
    print('\n ------------------ Begin! ------------------ \n')

    if not combo_row:
        for attempt in range(combo_amount):
            attempt_result = input("Success? (Y/N)\n> ").lower()
            while attempt_result != 'y' and attempt_result != 'n':
                attempt_result = input('Please put either y or n.\nSuccess? (Y/N)\n> ').lower()
                
            if attempt_result == 'y':
                attempt_result = True
            else:
                attempt_result = False
                
            attempts.append(attempt_result)
            
        successful_attempts = np.count_nonzero(attempts)
        print('All done! Out of ' + str(combo_amount) + ' for ' + combo_name+', you successfully hit ' + str(successful_attempts) + '! ('+str(successful_attempts)+'/'+str(combo_amount)+')' +'\nYou had a success rate of ' + str(int(successful_attempts/combo_amount*100))+'%!\nYou missed ' + str(combo_amount - successful_attempts) + '!')

    else:
        for attempt in range(combo_amount):
            attempt_result = input("Success? (Y/N)\n> ").lower()
            while attempt_result != 'y' and attempt_result != 'n':
                attempt_result = input('Please put either y or n.\nSuccess? (Y/N)\n> ').lower()
                
            if attempt_result == 'y':
                attempt_result = True
            else:
                attempt_result = False

            attempts.append(attempt_result)
        
        if np.count_nonzero(attempts) != combo_amount:
            while np.count_nonzero(attempts[-combo_amount:]) != combo_amount:
                attempt_result = input("Success? (Y/N)\n> ").lower()
                while attempt_result != 'y' and attempt_result != 'n':
                    attempt_result = input('Please put either y or n.\nSuccess? (Y/N)\n> ').lower()
                    
                if attempt_result == 'y':
                    attempt_result = True
                else:
                    attempt_result = False

                attempts.append(attempt_result)

        successful_attempts = np.count_nonzero(attempts)
        print('\nNice work, you successfully hit ' + combo_name , str(combo_amount) + ' times in a row! Out of ' + str(len(attempts)) + ' attempts, you successfully hit ' + str(successful_attempts) + '! ('+str(successful_attempts)+'/'+str(len(attempts))+')' +'\nYou had a success rate of ' + str(int(successful_attempts/len(attempts)*100))+'%!\nYou missed ' + str(len(attempts) - successful_attempts) + '!')

    print("You're doing great! Keep it up!")
    again = input("\nRepeat the program? (NOTE: N will close the program) (Y/N)\n> ")
    while again != 'y' and again != 'n':
        again = input('Please put either y or n.\nRepeat the program? (NOTE: N will close the program) (Y/N)\n> ')
            
    if again == 'n':
        break

