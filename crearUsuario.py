import os
import sys
import getpass

def checkRoot():
    if not os.getuid() == 0:
        print('You are not root')
        sys.exit(1)

def username():
    while True:
        name = input('User: ')
        fichero = open('/etc/passwd')
        contenidoFichero = fichero.read()
        if name in contenidoFichero:
            print('User already exists')
        else:
            break
    return name

def password():
    while True:
        clave = getpass.getpass()
        repClave = getpass.getpass('Retype Password: ')
        if clave != repClave:
            print('Password do not match')
        else:
            break
    return clave

if __name__ == '__main__':
    checkRoot()
    usuario = username()
    laclave = password()
    os.system(f'useradd -p {laclave} {usuario}')
