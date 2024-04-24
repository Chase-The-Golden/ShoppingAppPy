import psycopg2
from config import load_config
from login import connect
from catalog import admin_auth

def main():
    """ Main module for shopping app """
    print("Welcome to the Demo Marketplace")

    isLogin = False
    while not isLogin:
        user = input("Username: ")
        password = input("Password: ")
        loginTuple = (config, user, password)

        if user == 'quit':
            return
        elif connect(*loginTuple):
            isLogin = True
    
    admin_auth(*loginTuple)


if __name__ == '__main__':
    config = load_config()
    main()