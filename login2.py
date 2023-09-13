import sys, os, time


column=0
#---------------------------Database--------------------
matrixu=[["","","","","","","","",],["","","","","","","","",],["","","","","","","","",],["","","","","","","","",],["","","","","","","","",],["","","","","","","","",],["","","","","","","","",],["","","","","","","","",],]
matrixp=[["","","","","","","","",],["","","","","","","","",],["","","","","","","","",],["","","","","","","","",],["","","","","","","","",],["","","","","","","","",],["","","","","","","","",],["","","","","","","","",],]
iD=0
#----------------------------Database-----------------------------

def fill_db(username,password,ident):
    print(ident+1)
    nombre=list(username)
    passwd=list(password)
    matrixu[ident]=nombre
    matrixp[ident]=passwd
    for i in range(ident+1):
        print(matrixu[i], matrixp[i])
    ident+=1
    register(ident)

def register(ident):
    print('---------------------------------------------------------------------------')
    print('                                  Register')
    print('---------------------------------------------------------------------------')
    try:
        user=input('Inserta algo: ')
        passwd=input('Inserta algo: ')
        fill_db(user, passwd,ident)
    except IndexError:
        print('No hay espacio')

def login():
    print('------------------------------------------------------')
    print('                         Login')
    print('------------------------------------------------------')
    try:
        option=int(input('Choose your option:\n1.-Login\n2.-Go to register page\n---->'))
        
        if option==1:
            username = input("Username: ")
            password = input("Password: ")
            if valid_user_and_pass(user=username, passwd=password)==True:
                print('login sucessfull')
                print('Redirecting to landing page')
                time.sleep(2)
                os.system('cls')
                landing_page()
            else:
                print('Login unsucessfull. User or password doesnt exist')
                time.sleep(2)
                os.system('cls')
                login()
        elif option==2:
            print('Redirecting to register page')
            time.sleep(2)
            os.system('cls')
            register()
    except ValueError:
        os.system('cls')
        login()

def landing_page():
    print('----------------------------------------------------------')
    print('                      Landing page')
    print('----------------------------------------------------------')
    print('\nFelicidades! Te haz logueado correctamente')

def valid_user_and_pass(user, passwd):
    pass

def main():
    print('-------------------------------------------------------')
    print('                        Main page')
    print('-------------------------------------------------------')
    try:
        option=int(input('Choose your option:\n1.-Register\n2.-Login\n3.-Exit\n---->'))
        if option==1:
            print('Redirection to register page...')
            os.system('cls')
            register()
        if option==2:
            print('Redirection to login page..')
            os.system('cls')
            login()
        if option==3:
            print('Exiting..')
            time.sleep(2)
            os.system('cls')
            sys.exit()
    except ValueError:
        os.system('cls')
        main()

if __name__=='__main__':
    register(iD)