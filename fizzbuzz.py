num = 1

while num <= 100:
    
    # Parameters
    fizzparam = num / 3.0
    buzzparam = num / 5.0
    
    if fizzparam.is_integer() or buzzparam.is_integer():
        # Checks if either are true.
        if fizzparam.is_integer() and buzzparam.is_integer():
            # Both are correct, fizz buzz!
            print('Fizzbuzz')
        elif fizzparam.is_integer():
            print ('Fizz')
        else:
            print('Buzz')
    else:
        print(num)
        
    num += 1