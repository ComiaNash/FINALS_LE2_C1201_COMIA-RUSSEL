import time
import sys
from util.game import DiceGame
from util.user import UserMixin
from util.score import Score
class Mangager:
    def __init__(self) -> None:
        pass
        
    def logout(self):
        self.main()

    def menu(self, username):
        print(f"\nWelcome {username}")
        print("1. Start game")
        print("2. Show top scores")
        print('3. Load scores')
        print("4. Log out")

        while True:
            try:
                choice = input("\nEnter choice: ")

             
                if choice =='1':
                    game = DiceGame()
                    game.play(username)
                    self.menu(username)
                    break
                if choice =='2':
                    score = Score()
                    score.top_score(username)
                    self.menu(username)
                    break
                if choice == '3':
                    score = Score()
                    score.load()
                    self.menu(username)
                    break
                if choice =='4':
                    self.logout()
                    self.main()
                    break

            except ValueError as e:
                print(f'Error. {e}')

    def main(self,):

        while True:
            try:
                print("\nWelcome to Dice Roll game ")
                print("1. Register")
                print("2. Login")
                print('3. Exit')

                user = UserMixin()
                choice = input("Enter your choice: ")
                if choice =='1':
                    username = user.Register()
                    if username == None:
                        continue
                    else:
                        self.menu(username)
                        break
                elif choice =='2':
                    username = user.Login()
                    if username == None:
                        continue
                    else:
                        self.menu(username)
                        break
                elif choice =='3':
                    time.sleep(1)
                    sys.exit("Terminating program...")
                else:
                    print("Invalid choice Pleae try again.")
            except ValueError as e:
                print(f"Invalid Input. {e}")
        