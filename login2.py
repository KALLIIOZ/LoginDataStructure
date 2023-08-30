import sys, os, time


column=0
#---------------------------Database--------------------
matrixu=[]
matrixp=[]
def user_db(username, column):
    column+=1
    for a in range(1):
        line=[]
        for b in range(column):
            line.append(username)
        matrixu.append(line)

def pass_db(password, column):
    column+=1
    for a in range(1):
        line=[]
        for b in range(column):
            line.append(password)
        matrixp.append(line)
#----------------------------Database-----------------------------

def show_db(db):
    for row in db:
        for element in row:
            print(element, end=' ')
        print()

def register():
#    if registered==8:
#        print('Maximum of users and passwords has been registered')
#        print('Redirecting to login page')
#        time.sleep(2)
#        os.system('cls')
#        login()
    print('---------------------------------------------------------------------------')
    print('                                  Register')
    print('---------------------------------------------------------------------------')
    
    
    try:
        option=int(input('Choose an option:\n1.-Register\n2.-Login\n---->'))
        if option==1:
            try:        
                user=input('Insert your username: ')
                
                for username in matrixu:
                    for element in username:
                        if user==element:
                            print('El usuario ya existe, ingrese uno nuevo')
                            time.sleep(2)
                            os.system('cls')
                            register()
                if len(user)>8:
                    print('Tamaño de usuario o contraseña incorrecto. Contraseña debe ser maximo de 8 caracteres')
                    print('Intente de nuevo')
                    time.sleep(2)
                    os.system('cls')
                    register()
                if user=='':
                    print('\nWe dont accept empty characters')
                    time.sleep(2)
                    os.system('cls')
                    register()
                
                password=input('Insert your password: ')
                
                if len(password)!=8:
                    print('Tamaño de usuario o contraseña incorrecto. Contraseña debe ser maximo de 8 caracteres')
                    print('Intente de nuevo')
                    time.sleep(2)
                    os.system('cls')
                    register()
                elif password=='':
                    print('\nWe dont accept empty characters')
                    time.sleep(2)
                    os.system('cls')
                    register()

                else:
                    print(f'User {user} has been registered')
                    print(f'Password {password} has been registered')
                    user_db(user,column)
                    pass_db(password, column)
                    os.system('cls')
                    #registered+=1
            except ValueError:
                os.system('cls')
                register()
        elif option==2:
            print('Redirecting to login page')
            time.sleep(2)
            os.system('cls')
            login()

    except ValueError:
        os.system('cls')
        register()
    os.system('cls')
    register()

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
    try:
        option=int(input('Elige la opcion deseada:\n1.-Mostrar las bases de datos\n2.-Salir\n---->'))
        if option==1:
            print('[User database]')
            show_db(matrixu)
            print('\n[Password database]')
            show_db(matrixp)
            time.sleep(10)
            os.system('cls')
            landing_page()
        elif option==2:
            os.system('cls')
            sys.exit()
        else:
            print('Incorrect Value\nTry again')
            time.sleep(2)
            os.system('cls')
            landing_page()
    except ValueError:
        os.system('cls')
        landing_page()

def valid_user_and_pass(user, passwd):
    for i in range(len(matrixu)):
        if matrixu[i][0] == user and matrixp[i][0] == passwd:
            return True
    return False

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
    main()