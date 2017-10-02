####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Edwin'
strategy_name = 'betray & collude'
strategy_description = 'betray and collude.'
    
def move(my_history, their_history, my_score, their_score):
    if 'b' in their_history:
        return 'b'  
    else:
        return 'c'
