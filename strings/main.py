# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player1 = 'Ruud Gullit'
player2 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = player1 + ' ' + str(goal_0) + ', ' + player2 + ' ' + str(goal_1)
print(scorers)

report = f"{player1} scored in the {goal_0}nd minute\n{player2} scored in the {goal_1}th minute"
print(report)

player = "Ruud Gullit"

first_name = player[:player.find(' ')]
print(first_name)

last_name_len = len(player[player.find(' ')+1:])

name_short = player[0] + '.' + player[player.find(' '):]
print(name_short)

chant = (first_name + '! ') * (len(first_name)-1) + first_name + '!'
print(chant)

good_chant = chant[-1] != ' '
print(good_chant)

