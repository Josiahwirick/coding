import time


def collatz(): # The function that does the math
    counter = 0
    print('Input a number:')
    good = True
    while good:
        try: # Check if input works as an integer
            number = int(input())
            print(number)
            int(number)
            good = False
        except ValueError:
            print('Try again with a whole number:')
            continue # Return back to input
        
        while number != 1: # Run the following until the number variable is equal to 1
        
            if (number % 2) == 0: # Check if the number variable is even
                number = (number//2)
                print(number)
                counter = counter + 1
                time.sleep(0.3)
    
            elif (number % 2) == 1: # Check if number variable is odd
                number = (number*3 + 1)
                print(number)
                counter = counter + 1
                time.sleep(0.3)
            
    print('Finished in ' + str(counter) + ' calculations')
collatz()
