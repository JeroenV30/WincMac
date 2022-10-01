# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
# part 1
leek_price = 2
leek_string = 'Leek is ' + str(leek_price) + ' ' + 'euro per kilo.'
print(leek_string)

# part 2
leek_order = 'leek 4'
leek_order_amount = int(leek_order[leek_order.find('4'):])
sum_total = leek_order_amount * leek_price
print(sum_total)

# part 3
broccoli = 2.34
broccoli_order = 'broccoli 1.6'
broccoli_order_amount = broccoli_order[broccoli_order.find(' ') +1 :]
broccoli_order_amount = float(broccoli_order_amount)
total_price = broccoli_order_amount * broccoli
print(str(broccoli_order_amount) + 'kg broccoli costs ' + str(round(total_price, 2)) + 'e')


