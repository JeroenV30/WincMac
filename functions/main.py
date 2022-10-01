# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
def greet(name):
    result = f'Hello, {name}!'
    return result

print(greet('Jeroen'))

def add(x, y, z):
    sum_total = x + y + z
    return sum_total

def positive(x):
    if x > 0:
        return True
    else:
        return False
    
def negative(x):
    if x >= 0:
        return False
    else:
        return True