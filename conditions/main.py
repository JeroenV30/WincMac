# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(weather, time_of_day, cow_milking_status, location_of_cows, season, slurry_tank, grass_status):
    if cow_milking_status == True and location_of_cows == 'pasture':
        return('take cows to cowshed\nmilk cows\ntake cows back to pasture')
    elif grass_status == True and season == 'spring' and weather == 'sunny' and location_of_cows == 'pasture':
        return('take cows to cowshed\nmow grass\ntake cows back to pasture')
    elif location_of_cows == 'pasture' and slurry_tank == True:
        return ('take cows to cowshed\nfertilize pasture\ntake cows back to pasture')
    elif location_of_cows == 'pasture' and time_of_day == 'night' and weather == 'rain':
        return('take cows to cowshed')
    elif cow_milking_status == True and location_of_cows == 'cowshed':
        return('milk cows')
    elif slurry_tank == True and location_of_cows and weather != 'sunny' and weather != 'windy':
        return('fertilize pasture')
    elif grass_status == True and season == 'spring' and weather == 'sunny':
        return('mow grass')
    else: return('wait')

print(farm_action('sunny', 'night', False, 'cowshed', 'spring', False, True)) 
    