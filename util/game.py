import random
from util.user import UserMixin 
from util.score import Score
from datetime import datetime


class DiceGame(UserMixin):
    
    def __init__(self) -> None:
        
        super().__init__()
    
    def play(self, username):
       
        game_stage = 0
        player_score = 0
        while True:

            turn = 0
            player_turn_score = 0
            cpu_turn_score = 0

            while turn < 3:
             
                player = random.randint(1,6)
                cpu = random.randint(1,6)

                print(f'Player rolled: {player}')
                print(f"CPU rolled: {cpu}")

                turn += 1
                
                if player > cpu:
                    print(f"\nYou won this round {username}.\n")
                    player_turn_score += 1
                if cpu > player:
                    print("\nCpu won this round.\n")
                    cpu_turn_score += 1
                if cpu == player:
                    print('\n Its a tie')

            if player_turn_score > cpu_turn_score:
                game_stage += 1
                player_score += 3

                print(f"\nPlayer wins this stage. Score :{player_score} Stage: {game_stage}") 

                while True:
                    try:
                        choice = input("\nDo you want to continue to the next stage (1 for Yes, 0 for No): ").lower().strip()
                        if choice == '1':
                            break
                        elif choice =='0':
                            instance = Score()
                            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            #print(username, player_score, game_stage, current_time)
                            instance.save(username, player_score, game_stage, current_time)
                            return
                        else:
                            print('Invalid Input. Please enter 1 for Yes or 0 for No.')
                    except ValueError as e:
                            print(f"Invalid input {e} ")

            else:
                game_stage = 0
                player_score = 0
                print(f"You lost this stage {username}.\nCpu wins. Game over. You didn't win any stage.")
                break
          
            

   
        

#instance = DiceGame()
#instance.top_score()

                
