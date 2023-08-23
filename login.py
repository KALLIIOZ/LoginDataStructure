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

    
#Crea un hash de la misma forma que la contraseña registrada y las compara, si es igual el hash te loguea, sino, te regresa
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


def register():
    print('\t\t-----------------------------------------------------------')
    print('\t\t                        Register                        ')
    print('\t\t-----------------------------------------------------------')
    user=input('Insert an username: ')
    password=input('Insert a password: ')
    if len(user) != 8:
        print('\nUser length must be 8. Try again')
        time.sleep(2)
        os.system('cls')
        register()
    else:
        if len(password) != 8:
            print('\nPassword length should be 8. Please try again')
            time.sleep(2)
            os.system('cls')
            register()
        else:
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
                print('\n\n!--->Try again')
                time.sleep(2)
                os.system('cls')
                register()

def main_page():
    print('----------------------------------------------------------------------------')
    print('                                  Main page')
    print('----------------------------------------------------------------------------')
    option=int(input('Choose an option:\n1.-Stop program\n2.-Return to first page\n\n----> '))
    if option==1:
        os.system('cls')
        sys.exit()
    elif option==2:
        os.system('cls')
        main()
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
    print('Choose an option:\n1.-Login\n2.-Register\n3.-Finish program')
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