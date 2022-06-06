import random
import time
import mlbgame

DEBUG = 1
end_of_season = False
GM = random.randrange(1,30)
d = 1
w = 2
c = 3
b = 4
money = None
team = None

POSITIONS = ['C', 'P', '1B', '2B', 'SS', '3B', 'LF', 'CF', 'RF']

class Team(object):
    def __init__(self, info):
        self.players = []
        self.money = 300000000000
        self.info =  info
        self.lineup = {}
    def print_players(self):
        for player in self.players:
            print(player)
    def set_lineup(self, player, pos):
        self.lineup[pos] = player
        

def get_team_id(current_team=None):
    teams = mlbgame.teams()
    id = None
    for team in teams:
        if DEBUG >= 2:
            print(f'{team.club_common_name}')
        if team.club_common_name.lower() == current_team:
            print(f'Found {current_team} id is {team.team_id}')
            team_obj = team
            break
    return team_obj

def get_roster(team_id):
    roster = mlbgame.roster(team_id)
    return roster
    
def show_players(roster):
    player_list = []
    for  player in roster.players:
        player_list.append(player.name_full)
    return player_list
    
def return_your_team(gm):
    return mlbgame.teams()[gm] 

call_ups = 0
your_team = Team(return_your_team(GM))
print(your_team.info.club_common_name)
print('Your players are: ')
your_team.players = show_players(get_roster(your_team.info.team_id))
for pos in POSITIONS:
   print(f'Who do you want to play {pos}?')
   for idx, player in enumerate(your_team.players):
       print(f'{idx + 1}.  {player}')
   pp = input('Select a number above: ')
   your_team.set_lineup(your_team.players[int(pp) - 1], pos)
   
print('Your lineup is:')
for k,v in your_team.lineup.items():
    print(f'{k}:  {v}') 
rand_player =  random.randrange(0,8)
bench_player = input(f'{list(your_team.lineup.values())[rand_player]}'
                     'is 0-10 would you like to bench him?   ')
if bench_player == "yes":
    print("okay we will bench him")
    playing = input("who do you to play?  ")
    print(playing)
    print("okay we will play him.")
else:
    send_down = input("do you want send him down?  ")
    if send_down == "yes":
        print("okay we will send him down")
    else:
        print("okay we will not send him down")

    close_call = input("there was a close call at first base"
                       "the call was safe do you want to check the call?   ")
    if close_call == "yes":
        print("okay we will check it")
        final_call = random.randrange(1,2)
        if final_call == 1:
            print("the call is out")
        elif final_call == 2:
            print("the call is safe")
                
        
    
rand_player = random.randrange(0,8) 
playing = input(f'{list(your_team.lineup.values())[rand_player]}'
                ' is injuryed who do you want to play?   ')
print(playing)
print("okay we will play him")

print(f'{list(your_team.lineup.values())[rand_player]}'
                 'is back' )
rand_player = random.randrange(0,8)
trade = input(f "{list(your_team.lineup.values())[rand_player]} and cubs will trade nick madrigal and nico horner do you want say yes to the trade")
if trade == "yes":
    print("the trade is done")
else:
    print("the trade is off")


close_call = input("there was close call at home plate the call was out"
                   "do you want to check the call?    ")
if close_call == "yes":
    print("okay we will check the call")
    final_call = random.randrange(1,2)
    if final_call == 1:
        print("the call is out")
    elif final_call == 2:
        print("the call is safe")
rand_player = random.randrange(1,2)
slumps = input('{list(your_team.lineup.values())[rand_player]} is hitting .179 on'
          ' the season do you want to send him down to AAA')
if slumps == "yes":
    print("okay we will send him down")
    call_ups = input("who do you want to play")
    print(call_ups)
    print("okay we will play him")
else:
    print("okay we will not send him down")



close_call = input("there was close call at second base"
                   "the call was out do you want to check the call")
        
if close_call == "yes":
    print("okay we will check the call")
    final_call = random.randrange(1,2)
    if final_call == 1:
        print("the call is out")
    elif final_call == 2:
        print("the call is out")
else:
    print("okay we will not check the call")

close_call = input("there was a close call at first base"
                   "the call was out would you like to check the call")
if close_call == "yes":
    print("okay we will check the call")
    final_call = random.randrange(1,2)
    if final_call == 1:
        print("the call is out")
    elif final_call == 2:
        print("the call is out")
else:
    print("okay we will not check the call")

end_of_season = True
if end_of_season:
    p = random.randrange(1,5)
    if p == 1:
        r = random.randrange(1,2)
        if r == 1:
            print("you finshed in first place and a record of 101-61")
        elif r == 2:
            print("you finshed in first place and a record of 99-63")
    if p == 2:
        r = random.randrange(1,2)
        if r == 1:
            print("you finshed in second place and a record of 90-72")
        elif r == 2:
            print("you finshed in second place and a record of 88-74")

    if p == 3:
        r = random.randrange(1,2)
        if r == 1:
            print("you finshed in third place and a record of 82-80")
        elif r == 2:
            print("you finshed in third place and a record of 81-81")           
    
    if p == 4:
         
        r = random.randrange(1,2)
        if r == 1:
            print("you finshed in fourth place and a record of 74-88")
        elif r == 2:
            print("you finshed in fourth place and a record of 70-92")   


    if p == 5:
        r = random.randrange(1,2)
        if r == 1:
            print("you finshed in fifth place and a record of 54-109")
        elif r == 2:
            print("you finshed in fifth place and a record of 61-101")

    print("the season is over")

    print("spring training has started")


    print("the season has started")
    close_call = input("there was a close call at home plate the call is out do you want to check it")
    if close_call == "yes":
        print("okay we will check the call")
        final_call = random.randrange(1,2)
        if final_call == 1:
            print("the call is out")
        elif final_call == 2:
            print("the call is safe")
            

    








exit()
