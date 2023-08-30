import sys, os, time, random


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
    os.system('cls')
    column=0
    while True:
        print('\nInserte number 1 to exit')
        user=input('Insert your username: ')
        password=input('Insert your password: ')
        if 8<=len(password)>=16:
            print('Tamaño de contraseña incorrecto. Contraseña debe ser minimo de 8 caracteres')
            time.sleep(2)
            os.system('cls')
            register()
        if user=='1' or password=='1':
            break
        else:
            user_db(user,column)
            pass_db(password, column)
            os.system('cls')
    print('Redirection to main page...')
    time.sleep(2)
    os.system('cls')
    main()

def login():
    print('------------------------------------------------------')
    print('                         Login')
    print('------------------------------------------------------')
    username = input("Username: ")
    password = input("Password: ")

    if valid_user_and_pass(user=username, passwd=password)==True:
        print('login sucessfull')
        print('Redirecting to landing page')
        time.sleep(2)
        os.system('cls')
        landing_page()
    else:
        print('Login unsucessfull. Try again')
        time.sleep(2)
        os.system('cls')
        login()


def landing_page():
    print('----------------------------------------------------------')
    print('                      Landing page')
    print('----------------------------------------------------------')
    print('\nFelicidades! Te haz logueado correctamente')
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

def valid_user_and_pass(user, passwd):
    for i in range(len(matrixu)):
        if matrixu[i][0] == user and matrixp[i][0] == passwd:
            return True
    return False

def main():
    print('-------------------------------------------------------')
    print('                        Main page')
    print('-------------------------------------------------------')
    option=int(input('Choose your option:\n1.-Register\n2.-Login\n3.-Exit\n---->'))
    if option==1:
        print('Redirection to register page...')
        register()
    if option==2:
        print('Redirection to login page..')
        login()
    if option==3:
        print('Exiting..')
        time.sleep(2)
        os.system('cls')
        sys.exit()
    
if __name__=='__main__':
    main()