import numpy as np
import os
from pynput import keyboard
from datetime import datetime
save_path = 'text files'

write_to_text = input("Write results to textfile? \nNOTE: For each time you repeat the program without closing it, you will record your combo in the program.\nOnce finished, a text file will be combine the combos into one\nUse this feature to keep combos such as 'BnB p1 side' and p2 side in the same text file\nWrite to textfile? (Y/N)\n> ")
while write_to_text != 'y' and write_to_text != 'n':
    write_to_text = input('Please put either y or n.\nWrite to textfile? (Y/N)\n> ')

if write_to_text == 'y':
    write_to_text = True
    time_started = datetime.now().strftime('20%y;%m(month);%d(day) - %H;%M')
    to_write = []
else:
    write_to_text = False
    
while True:
    attempts = []
    def on_press(key):
        try:
            global attempts 
            if key.char == ('9'):
                print('Successful attempt recorded!')
                attempts.append(True)
                return False
            if key.char == ('0'):
                print('Unsuccessful attempt recorded!')
                attempts.append(False)
                return False
        except AttributeError:
            pass

    def on_release(key):
        if key == keyboard.Key.esc:
            return False


    combo_name = input("Combo training - Hotkey version! Whats the name of the route? (optional, can be blank)\n> ").title()
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

    print('\n ------------------ Begin! ------------------ \n')

    if not combo_row:
        for attempt in range(combo_amount):
            
            with keyboard.Listener(
                    on_press=on_press,
                    on_release=on_release) as listener:
                listener.join()
                
        successful_attempts = np.count_nonzero(attempts)
        print('\nAll done! Out of ' + str(combo_amount) + ' attempts for ' + combo_name+', you successfully hit ' + str(successful_attempts) + '! ('+str(successful_attempts)+'/'+str(combo_amount)+')' +'\nYou had a success rate of ' + str(int(successful_attempts/combo_amount*100))+'%!\nYou missed ' + str(combo_amount - successful_attempts) + '!')

    else:
        for attempt in range(combo_amount):
            
            with keyboard.Listener(
                    on_press=on_press,
                    on_release=on_release) as listener:
                listener.join()
             
        if np.count_nonzero(attempts) != combo_amount:
            while np.count_nonzero(attempts[-combo_amount:]) != combo_amount:

                with keyboard.Listener(
                        on_press=on_press,
                        on_release=on_release) as listener:
                    listener.join()
             
        successful_attempts = np.count_nonzero(attempts)
        print('\nNice work, you successfully hit ' + combo_name , str(combo_amount) + ' times in a row! Out of ' + str(len(attempts)) + ' attempts, you successfully hit ' + str(successful_attempts) + '! ('+str(successful_attempts)+'/'+str(len(attempts))+')' +'\nYou had a success rate of ' + str(int(successful_attempts/len(attempts)*100))+'%!\nYou missed ' + str(len(attempts) - successful_attempts) + '!')

    if write_to_text:
        to_write.append(combo_name + ' - ' + str(successful_attempts)+'/'+str(len(attempts))+'. Success rate of ' + str(int(successful_attempts/len(attempts)*100))+'%.')
        
    again = input("\nRepeat the program? (NOTE: N will close the program and create text file if specified) (Y/N)\n> ")
    while again != 'y' and again != 'n':
        again = input('Please put either y or n.\nRepeat the program? (NOTE: N will close the program) (Y/N)\n> ')
    if again == 'n':
        if write_to_text:
            text_filename = os.path.join(save_path, time_started)
            text_file = open(text_filename + ".txt", "w")
            for combo_information in to_write:
                text_file.write(combo_information + '\n')
            text_file.close()
        break

