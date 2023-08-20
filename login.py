import sys, os, time
from werkzeug.security import generate_password_hash, check_password_hash

delete_value=0
log={}

def mlog_page():
    print('------------------------------------------')
    print('                   Login                 ')
    print('------------------------------------------')
    user_log=input('\tPlease enter your username: ')
    pass_log=input('\tPlease enter your password: ')
    if user_log not in log:
        print(f'\n\t{user_log} doesnt exist. Please try again')
        time.sleep(2)
        os.system('cls')
        mlog_page()
    elif not check_password_hash(log[user_log], pass_log):
        print('\n\tInvalid password')
        time.sleep(2)
        os.system('cls')
        mlog_page()
    else:
        print('\n\tLogin succesful. Going to mian page')
        time.sleep(2)
        os.system('cls')
        main_page()
        
def delete_user(username):
    delete_value=1
    if delete_value!=0:
        if username in log:
            del log[username]
            sys.stdout(f'The username {username} has been removed')
            time.sleep(2)
            os.system('cls')
            main_page()
        else:
            sys.stdout(f'The user {username} doesnt exist or was previously removed')
            time.sleep(2)
            os.system('cls')
            main_page()

def register():
    print('\t\t-----------------------------------------------------------')
    print('\t\t                        Register                        ')
    print('\t\t-----------------------------------------------------------')
    user=input('Insert an username: ')
    password=input('Insert a password: ')
    if user not in log:
        hash=generate_password_hash(password)
        log[user]=hash
        
        print(f'The user {user} has been registered')
        print('\tGoing to login page')
        time.sleep(2)
        os.system('cls')
        mlog_page()
    if user in log:
        print(f'The user {user} already exists. Please enter a new one.')
        print('\t!--->Try again')
        time.sleep(2)
        os.system('cls')
        register()

def main_page():
    print('----------------------------------------------------------------------------')
    print('                                  Main page')
    print('----------------------------------------------------------------------------')
    option=int(input('Choose an option:\n1.-Stop program\n2.-Return to first page\n3.-Delete an username\n\n----> '))
    if option==1:
        os.system('cls')
        sys.exit()
    elif option==2:
        os.system('cls')
        main()
    elif option==3:
        user_del=input('Insert the username to be removed: ')
        delete_user(user_del)
    else:
        print('That option doesnt exist')
        time.sleep(2)
        os.system('cls')
        main_page()

def main():
    os.system('cls')
    print('----------------------------------------------------------')
    print('                            Welcome')
    print('----------------------------------------------------------')
    print('Choose an option:\n1.-Login\n2.-Register\n3.-Exit')
    option=int(input('----->'))
    try:
        if option==1:
            os.system('cls')
            mlog_page()
        elif option==2:
            os.system('cls')
            register()
        elif option==3:
            os.system('cls')
            sys.exit()
        else:
            print('Invalid option. Try again')
            time.sleep(2)
            os.system('cls')
            main
    except ValueError:
        raise SystemExit('Invalid type of number')
    
if __name__=='__main__':
    main()