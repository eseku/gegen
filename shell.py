from gegen import run
from simple_chalk import chalk, green, red


while True: 
    text = input(green.bold('gegen $ '))
    result, error = run('<stdin>', text)
    
    if error: print(red.bold(error.as_string()))
    else: print(result)