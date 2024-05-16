import os
import ast
class UserMixin:

    def __init__(self) -> None:
        self.data_base = {}
        self.userpath = os.path.join('Txt', 'User.txt')
        self.directory = 'Txt'

    def file_setup(self):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

        if not os.path.isfile(self.userpath):
            with open(self.userpath, 'w') as file:
                file.write('')

    def Register(self):
        
        self.file_setup()
        
        while True:
          
            username = input("\nEnter username (at least 4 characters), or leave blank to cancel: ").strip()

            if not username:
                return None
            while len(username) < 4:
                print("Username needs to be at least 4 characters.")
                username = input("Enter your name: ").strip()

            username_exist = False
            with open(self.userpath, 'r') as file:
                for line in file:
                    try:
                        user_info = ast.literal_eval(line.strip())

                        if  username in user_info:
                            username_exist = True
                            break

                    except ValueError as e:
                        print(f"Error {e}")

            if username_exist:
                print("Username already exist. Please try again")
                continue

            password = input("Enter password (at least 6 characters), or leave blank to cancel: ")
            if not password:
                return None
            
            while len(password) < 6:
                print("Passowords must atleast be 6 characters (leave blank to cancel).")
                password = input("Enter password: ")
                if not password:
                    return None

            verify_pass = input("Verify password: ")
            while verify_pass != password:
                print("Passwords do not match. Please try again")
                verify_pass = input("Re-enter your password: ")

            user_info = { username: {'Password': password, 'Record' : {'score': 0, 'stage': 0, 'date': 0}}}
            self.data_base[username] = user_info  
        
            with open(self.userpath, 'a') as file:
                user_info_str = str(self.data_base[username]) + '\n'
                file.write(user_info_str) 
            
            print("\nRegistration Succeessful.")

            return username
    
    def Login(self):

        self.file_setup()

        while True:
            
            username = input("Enter username (leave blank to cancel): ")
            if not username:
                return None
            
            userame_exist = False
            with open(self.userpath, 'r') as file:
                for line in file:
                    try:
                        user_info = ast.literal_eval(line.strip())
                        if username in user_info:
                            userame_exist = True
                            
                            password = input("Enter password (leave blank to cancel): ")
                            if not password:
                                return None
                            
                            while password != user_info[username]['Password']:
                                print("Invalid credentials. Please try again")
                                password = input('Re-enter your password (leave blank to cancel): ')
                                if not password:
                                    return None

                            print(f"Login Succesful. Welcome {username}.")

                            return username
                    
                    except ValueError as e:
                        print(f"Error. {e}")
            
            if not userame_exist:
                print("\nUser Does not exist. Please try again. (Press Enter to return to main menu.)")
                continue

