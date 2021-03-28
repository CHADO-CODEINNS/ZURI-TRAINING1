import datetime
date = datetime.datetime.now()
welcome = f'Welcome to ZURI ATM. \nYou logged in at {date}'
print(welcome)

name = input('\nWhat is your name? \n')
allowedUsers = ['Seyi', 'Daniel', 'Tade']
allowed_Password = ['passwordSeyi', 'passwordDaniel', 'passwordTade']

if name in allowedUsers:
    password = input('Password: \n')
    userID = allowedUsers.index(name)

    if password == allowed_Password[userID]:
        print(f'\nWelcome {name.title()}. '
              'These are the available options:'
              '\n1. Withdrawal'
              '\n2. Cash deposit'
              '\n3. Complaint\n')

        selected_option = int(input('Please select an option: \n'))

        if selected_option == 1:
            message_1 = (f'Your selected option is: {selected_option}')
            print(message_1)
            
            message_2 = int(input('\nHow much would you like to withdraw?\n'))
            message_3 = ('\nKindly take your cash'
                         '\nThank you for banking with us.')
            print(message_2,
                  message_3)
            
            
        elif selected_option == 2:
            message_3 =(f'Your selected option is: {selected_option}')
            print(message_3)

            message_4 = int(input('How much would you like to deposit?\n'))
            balance = message_4 + 50000
            message_5 = ('\nDeposit successful.'
                         f'\nYour current balance is {balance} naira.'
                         '\nThank you for banking with us.')
            print(message_4,
                  message_5)

            
        elif selected_option == 3:
            print(f'Your selected option is: {selected_option}')
            message_6 = input(('What issue will you like to report?\n'))
            message_7 = ('\nReport received. \nThank your contacting us.')
            print(message_6, message_7)
    
        else:
            print('Invalid option selected, pleasebtry again')
            
    else:
        print('Password Incorrect, please try again')

else:
    print('Username not found, please try again')
