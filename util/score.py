import ast
from util.user import UserMixin

class Score(UserMixin):
    def __init__(self) -> None:
        super().__init__()
     
     
    def load(self):
        with open(self.userpath, 'r') as file:
            try:
                for lines in file:
                    user_info = ast.literal_eval(lines.strip())

                    for username, user_data in user_info.items():
                        record = user_data['Record']
                        if record['score'] == 0:
                            print(f'{username} has no games played yet. Play a game to see score')
                            break
                        else:
                            print(f"Username: {username}, Score: {record['score']}, Stage: {record['stage']}, Date: {record['date']}")
                              
            except ValueError as e:
                print(f'Error. {e}')


    def save(self, username, score, stage, date):
        with open(self.userpath, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                try:
                    user_info = ast.literal_eval(line.strip())
                    if username in user_info:
                        if user_info[username]['Record']['score'] > score:
                            return None
                        else:
                            user_info[username]['Record'] = {'score': score, 'stage': stage, 'date': date}
                            lines[i] = str(user_info) + '\n'    
                except ValueError as e:
                    print(f"{e}")

        with open(self.userpath, 'w') as file:
            file.writelines(lines)


    def top_score(self, username):
        records = {}
        with open(self.userpath) as file:
            user_info = file.readlines()
            for line in user_info:
                user_info = ast.literal_eval(line.strip())
                #store dicts in self.dict 
                self.data_base.update(user_info)
        #Extract username and records
        for username, user_info in self.data_base.items():
            #Resulting dictionary layout
            #nested dictionary sturcture of records = {username: {'score': somevalue, 'stage': somevalue, 'date': somevalue}}
            records[username] = user_info['Record']
        
        sorted_records = sorted(records.items(), key= lambda x:x[1]['score'], reverse= True)
        print('Scores:')
        i = 0
        for username, record in sorted_records:
            
            if record['score'] == 0:
                print(f'{username} has no games played yet. Play a game to see top scores.')
                break
            else:
                i +=1
                print(f"{i}. Username: {username}, Score: {record['score']}, Stage: {record['stage']}, Time: {record['date']}")
